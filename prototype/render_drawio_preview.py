"""Render the uncompressed JobShield draw.io file to review PNGs.

This lightweight renderer is intentionally limited to the shapes used by the
project diagram.  It exists so the repository can perform visual QA without
uploading the confidential concept to an external diagram service.
"""

from __future__ import annotations

import html
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


FONT_REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\leelawdb.ttf")
SCALE = 1.0


def parse_style(raw: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for part in (raw or "").split(";"):
        if "=" in part:
            key, value = part.split("=", 1)
            result[key] = value
        elif part:
            result[part] = "1"
    return result


def clean_text(raw: str) -> str:
    value = html.unescape(raw or "")
    value = re.sub(r"(?i)<br\s*/?>", "\n", value)
    value = re.sub(r"<[^>]+>", "", value)
    # Leelawadee UI covers Thai well but lacks the arrow glyph on some Windows
    # installs. Use an ASCII fallback in review PNGs; Draw.io keeps the arrow.
    return html.unescape(value).replace("→", " > ").strip()


def color(value: str | None, fallback: str) -> str:
    if not value or value in {"none", "default"}:
        return fallback
    return value


def font(size: float, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold and FONT_BOLD.exists() else FONT_REGULAR
    return ImageFont.truetype(str(path), max(9, round(size * SCALE)))


def wrap_lines(draw: ImageDraw.ImageDraw, text: str, selected_font, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split(" ")
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if draw.textbbox((0, 0), candidate, font=selected_font)[2] <= max_width:
                current = candidate
            elif current:
                lines.append(current)
                current = word
            else:
                # Thai copy often has few spaces. Split long strings by glyph.
                chunk = ""
                for glyph in word:
                    test = chunk + glyph
                    if draw.textbbox((0, 0), test, font=selected_font)[2] <= max_width:
                        chunk = test
                    else:
                        if chunk:
                            lines.append(chunk)
                        chunk = glyph
                current = chunk
        if current:
            lines.append(current)
    return lines


def draw_label(
    draw: ImageDraw.ImageDraw,
    bounds: tuple[float, float, float, float],
    text: str,
    style: dict[str, str],
    *,
    vertical_offset: float = 0,
) -> None:
    x, y, w, h = [v * SCALE for v in bounds]
    size = float(style.get("fontSize", "14"))
    is_bold = style.get("fontStyle") == "1" or "<b>" in text.lower()
    selected_font = font(size, is_bold)
    plain = clean_text(text)
    pad = max(8, int(float(style.get("spacing", "6")) * SCALE))
    lines = wrap_lines(draw, plain, selected_font, max(10, int(w - pad * 2)))
    spacing = max(3, int(size * 0.25 * SCALE))
    heights = [draw.textbbox((0, 0), line or " ", font=selected_font)[3] for line in lines]
    total = sum(heights) + spacing * max(0, len(lines) - 1)
    ty = y + vertical_offset * SCALE + max(pad, (h - vertical_offset * SCALE - total) / 2)
    align = style.get("align", "center")
    fill = color(style.get("fontColor"), "#243630")
    for line, line_height in zip(lines, heights):
        line_width = draw.textbbox((0, 0), line, font=selected_font)[2]
        if align == "left":
            tx = x + pad
        elif align == "right":
            tx = x + w - pad - line_width
        else:
            tx = x + (w - line_width) / 2
        draw.text((tx, ty), line, font=selected_font, fill=fill)
        ty += line_height + spacing


def geometry(
    cell: ET.Element,
    by_id: dict[str, ET.Element] | None = None,
) -> tuple[float, float, float, float]:
    geo = cell.find("mxGeometry")
    if geo is None:
        return 0, 0, 0, 0
    x, y, width, height = tuple(float(geo.get(k, "0")) for k in ("x", "y", "width", "height"))
    parent_id = cell.get("parent", "")
    if by_id is not None and parent_id not in {"", "0", "1"}:
        parent = by_id.get(parent_id)
        if parent is not None:
            parent_x, parent_y, _, _ = geometry(parent, by_id)
            x += parent_x
            y += parent_y
    return x, y, width, height


def style_port(box, style, prefix):
    x, y, w, h = box
    px = float(style.get(prefix + "X", "0.5"))
    py = float(style.get(prefix + "Y", "0.5"))
    return ((x + w * px) * SCALE, (y + h * py) * SCALE)


def nearest_ports(source, target):
    sx, sy, sw, sh = source
    tx, ty, tw, th = target
    scx, scy = sx + sw / 2, sy + sh / 2
    tcx, tcy = tx + tw / 2, ty + th / 2
    if abs(tcx - scx) >= abs(tcy - scy):
        if tcx >= scx:
            return ((sx + sw) * SCALE, scy * SCALE), (tx * SCALE, tcy * SCALE)
        return (sx * SCALE, scy * SCALE), ((tx + tw) * SCALE, tcy * SCALE)
    if tcy >= scy:
        return (scx * SCALE, (sy + sh) * SCALE), (tcx * SCALE, ty * SCALE)
    return (scx * SCALE, sy * SCALE), (tcx * SCALE, (ty + th) * SCALE)


def arrow_head(draw, before, end, fill, width):
    angle = math.atan2(end[1] - before[1], end[0] - before[0])
    length = 11 * SCALE
    spread = 5 * SCALE
    back = (end[0] - length * math.cos(angle), end[1] - length * math.sin(angle))
    left = (back[0] + spread * math.sin(angle), back[1] - spread * math.cos(angle))
    right = (back[0] - spread * math.sin(angle), back[1] + spread * math.cos(angle))
    draw.polygon([end, left, right], fill=fill)


def render_page(diagram: ET.Element, output: Path) -> None:
    model = diagram.find("mxGraphModel")
    if model is None:
        raise ValueError(f"missing graph model: {diagram.get('name')}")
    page_width = int(float(model.get("pageWidth", "2400")) * SCALE)
    page_height = int(float(model.get("pageHeight", "1100")) * SCALE)
    canvas = Image.new("RGB", (page_width, page_height), "#FFFFFF")
    draw = ImageDraw.Draw(canvas)
    cells = list(model.findall("./root/mxCell"))
    by_id = {cell.get("id", ""): cell for cell in cells}
    pending_edge_labels: list[tuple[tuple[float, float], str, str, float]] = []

    # Draw lane backgrounds first. Connectors then stay visible inside lanes,
    # while ordinary nodes are drawn last and keep their interiors clean.
    for cell in cells:
        if cell.get("vertex") != "1":
            continue
        style = parse_style(cell.get("style", ""))
        if "swimlane" not in style:
            continue
        x, y, w, h = geometry(cell, by_id)
        bounds = (x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE)
        stroke = color(style.get("strokeColor"), "#7B8B86")
        fill = color(style.get("fillColor"), "#FFFFFF")
        width = max(1, round(float(style.get("strokeWidth", "1")) * SCALE))
        draw.rounded_rectangle(bounds, radius=12 * SCALE, fill=fill, outline=stroke, width=width)
        band_height = float(style.get("startSize", "36")) * SCALE
        band_fill = color(style.get("swimlaneFillColor"), fill)
        draw.rounded_rectangle((bounds[0], bounds[1], bounds[2], bounds[1] + band_height + 6), radius=12 * SCALE, fill=band_fill)
        draw.rectangle((bounds[0], bounds[1] + band_height / 2, bounds[2], bounds[1] + band_height), fill=band_fill)
        draw.line((bounds[0], bounds[1] + band_height, bounds[2], bounds[1] + band_height), fill=stroke, width=width)
        title_style = dict(style)
        title_style["align"] = "left"
        title_style["fontStyle"] = "1"
        draw_label(draw, (x, y, w, float(style.get("startSize", "36"))), cell.get("value", ""), title_style)

    for cell in cells:
        if cell.get("edge") != "1":
            continue
        source = by_id.get(cell.get("source", ""))
        target = by_id.get(cell.get("target", ""))
        if source is None or target is None:
            continue
        edge_style = parse_style(cell.get("style", ""))
        source_box, target_box = geometry(source, by_id), geometry(target, by_id)
        if any(k in edge_style for k in ("exitX", "exitY")):
            start = style_port(source_box, edge_style, "exit")
        else:
            start, _ = nearest_ports(source_box, target_box)
        if any(k in edge_style for k in ("entryX", "entryY")):
            end = style_port(target_box, edge_style, "entry")
        else:
            _, end = nearest_ports(source_box, target_box)
        geo = cell.find("mxGeometry")
        explicit: list[tuple[float, float]] = []
        if geo is not None:
            points = geo.find("./Array[@as='points']")
            if points is not None:
                explicit = [
                    (float(point.get("x", "0")) * SCALE, float(point.get("y", "0")) * SCALE)
                    for point in points.findall("mxPoint")
                ]
        if explicit:
            path = [start, *explicit, end]
        elif abs(start[1] - end[1]) < 3 or abs(start[0] - end[0]) < 3:
            path = [start, end]
        else:
            middle_x = (start[0] + end[0]) / 2
            path = [start, (middle_x, start[1]), (middle_x, end[1]), end]
        stroke = color(edge_style.get("strokeColor"), "#6E807A")
        width = max(1, round(float(edge_style.get("strokeWidth", "1")) * SCALE))
        if edge_style.get("dashed") == "1":
            for a, b in zip(path, path[1:]):
                segment_len = max(1, math.dist(a, b))
                steps = max(1, int(segment_len / (10 * SCALE)))
                for i in range(0, steps, 2):
                    p0 = (a[0] + (b[0] - a[0]) * i / steps, a[1] + (b[1] - a[1]) * i / steps)
                    p1 = (a[0] + (b[0] - a[0]) * min(i + 1, steps) / steps, a[1] + (b[1] - a[1]) * min(i + 1, steps) / steps)
                    draw.line([p0, p1], fill=stroke, width=width)
        else:
            draw.line(path, fill=stroke, width=width, joint="curve")
        if edge_style.get("endArrow", "block") != "none" and len(path) >= 2:
            arrow_head(draw, path[-2], path[-1], stroke, width)
        label = clean_text(cell.get("value", ""))
        if label:
            midpoint = path[len(path) // 2]
            pending_edge_labels.append((midpoint, label, stroke, float(edge_style.get("fontSize", "12"))))

    for cell in cells:
        if cell.get("vertex") != "1":
            continue
        x, y, w, h = geometry(cell, by_id)
        style = parse_style(cell.get("style", ""))
        bounds = (x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE)
        stroke = color(style.get("strokeColor"), "#7B8B86")
        fill = color(style.get("fillColor"), "#FFFFFF")
        width = max(1, round(float(style.get("strokeWidth", "1")) * SCALE))
        is_text = "text" in style and style.get("strokeColor") == "none"
        if is_text:
            draw_label(draw, (x, y, w, h), cell.get("value", ""), style)
            continue
        if "swimlane" in style:
            continue
        elif "rhombus" in style:
            cx, cy = (bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2
            draw.polygon([(cx, bounds[1]), (bounds[2], cy), (cx, bounds[3]), (bounds[0], cy)], fill=fill, outline=stroke)
            if width > 1:
                draw.line([(cx, bounds[1]), (bounds[2], cy), (cx, bounds[3]), (bounds[0], cy), (cx, bounds[1])], fill=stroke, width=width, joint="curve")
            draw_label(draw, (x + w * 0.13, y + h * 0.13, w * 0.74, h * 0.74), cell.get("value", ""), style)
        else:
            radius = 12 * SCALE if style.get("rounded") == "1" else 2
            draw.rounded_rectangle(bounds, radius=radius, fill=fill, outline=stroke, width=width)
            draw_label(draw, (x, y, w, h), cell.get("value", ""), style)

    # Edge labels sit above node fills so short branch labels remain legible.
    for midpoint, label, stroke, size in pending_edge_labels:
        selected_font = font(size, False)
        label_box = draw.textbbox((0, 0), label, font=selected_font)
        lw, lh = label_box[2] - label_box[0], label_box[3] - label_box[1]
        lx, ly = midpoint[0] - lw / 2, midpoint[1] - lh - 5
        draw.rounded_rectangle((lx - 5, ly - 3, lx + lw + 5, ly + lh + 3), radius=4, fill="#FFFFFF")
        draw.text((lx, ly), label, font=selected_font, fill=stroke)

    canvas.save(output, format="PNG", optimize=True)


def main() -> int:
    source = Path(sys.argv[1] if len(sys.argv) > 1 else "prototype/jobshield-kplus-integration-benefits-v6.drawio")
    root = ET.fromstring(source.read_text(encoding="utf-8"))
    pages = list(root.findall("diagram"))
    stem = source.with_suffix("")
    for index, page in enumerate(pages, start=1):
        destination = stem.with_name(f"{stem.name}-page-{index}.png")
        render_page(page, destination)
        print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

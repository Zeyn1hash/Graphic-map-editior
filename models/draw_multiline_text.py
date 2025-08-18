def draw_multiline_text(text, font, color, surface, x, y, line_height=5):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        txt_surf = font.render(line, True, color)
        surface.blit(txt_surf, (x, y + i * (txt_surf.get_height() + line_height)))
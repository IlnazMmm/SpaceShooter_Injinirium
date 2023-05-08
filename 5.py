from PIL import Image

def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"

def remove_spell(src_file, dest_file, rotate_degrees=180, **colors):
    with Image.open(src_file) as img:
        img = img.rotate(rotate_degrees)
        pixels = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                pixel_color = pixels[x, y]
                hex_color = rgb_to_hex(pixel_color)
                if hex_color in colors:
                    new_hex_color = colors[hex_color]
                    new_rgb_color = hex_to_rgb(new_hex_color)
                    pixels[x, y] = new_rgb_color
        img.save(dest_file)

colors = {
    "#9dd6f3": "#ccf197",
    "#e3bdfa": "#87c6ee",
    "#ec1c24": "#af2cb6",
    "#985a2e": "#0f5682"
}
remove_spell("pictures/broomstick.png", "pictures/up_and_down.png", **colors)
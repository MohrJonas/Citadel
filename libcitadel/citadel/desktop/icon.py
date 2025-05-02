from PIL.Image import open, merge
from io import BytesIO
from typing import cast

def color_icon(image_bytes: bytes, color: tuple[int, int , int]) -> bytes:
    original_image = open(BytesIO(image_bytes)).convert("RGBA")
    r, g, b, a = original_image.split()
    grayscale_rgb = merge("RGB", (r, g, b)).convert("L")
    grayscale_image = merge("LA", (grayscale_rgb, a)).convert("RGBA")
    for y in range(grayscale_image.height):
        for x in range(grayscale_image.width):
            pixel_color = cast(list[int], grayscale_image.getpixel((x, y)))
            
            if pixel_color[3] > 0:  # Alpha channel
                new_pixel_color = (
                    int(pixel_color[0] * color[0] / 255),
                    int(pixel_color[1] * color[1] / 255),
                    int(pixel_color[2] * color[2] / 255),
                    pixel_color[3]  # Keep alpha unchanged
                )
                grayscale_image.putpixel((x, y), new_pixel_color)
    resulting_images_bytes = BytesIO()
    grayscale_image.save(resulting_images_bytes, "PNG")
    return resulting_images_bytes.getvalue()
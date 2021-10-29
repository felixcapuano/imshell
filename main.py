from PIL import Image
from statistics import mean

with Image.open('image.png', 'r') as im:
    pixels_rgb = list(im.getdata())
    image_w, image_h = im.size

pixel_size = 5
render_w = round((image_w / pixel_size) + 0.5)
render_h = round((image_h / pixel_size) + 0.5)

print("----------Details---------")
print(f"pixel {pixel_size}")
print(f"width render={render_w} image={image_w}")
print(f"height render={render_h} image={image_h}")
print("--------------------------")


def filter_max(x, y):
    maximum = 0
    for pix_y in range(0, pixel_size-1):
        for pix_x in range(0, pixel_size-1):

            if x + pix_x >= image_w or \
                    y + pix_y >= image_h:
                continue

            pos = image_w * (y + pix_y) + x + pix_x
            if pixels_bw[pos] > maximum:
                maximum = pixels_bw[pos]
    return maximum


pixels_bw = []
for pxl in pixels_rgb:
    pixels_bw.append(mean(pxl[:2]))  # * (pxl[3]/255))

render = []
for y in range(0, image_h, pixel_size):
    for x in range(0, image_h, pixel_size):
        # print(f"{x},{y}", end="\t")
        render_pixel = filter_max(x, y)
        render.append(render_pixel)
        print(render_pixel, end='')
    print()


def show(render, chars="/azertyuiopqsdfghjklmwxcvbn"):
    char_count = len(chars)

    for i, pixel_value in enumerate(render):
        print(chars[int(pixel_value / 256 * char_count)], end="")
        if i % render_w == 0:
            print()


print(f"length : {len(render)}")
show(render)

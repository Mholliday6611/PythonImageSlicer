import sys
from PIL import Image


def handle_image(image, x_amount, y_amount):
    width, height = image.size
    print(width, height)
    slice_w = width/x_amount
    slice_h = height/y_amount


    img_count = 0
    for x in range(x_amount):
        for y in range(y_amount):
            slice_section = (0 + slice_w *x, 0  +slice_h*y, slice_w + slice_w *x, slice_h +slice_h*y,)
            print(slice_section)
            region = image.crop(slice_section)

            region.save(f"./output/animal{img_count}.png")
            img_count += 1

if __name__ == "__main__":
    (infile, x_amount, y_amount) = sys.argv[1:]

    try:
        with Image.open(infile) as im:
            handle_image(im, int(x_amount), int(y_amount))
    except OSError:
        pass
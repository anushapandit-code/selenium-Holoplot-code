import argparse
import random
from PIL import Image, ImageDraw

CANVAS_SIZE = 400


def draw_image(d, hue, output_path):
    image = Image.new('RGB', (CANVAS_SIZE, CANVAS_SIZE), 'white')
    draw = ImageDraw.Draw(image)
    center = CANVAS_SIZE / 2
    draw.ellipse(
        (center - d / 2, center - d / 2, center + d / 2, center + d / 2),
        fill=f'hsv({hue}, 100%, 100%)'
    )
    draw.rectangle(
        (0, 0, 399, 399),
        outline=f'hsv({random.randint(0, 360)}, 100%, 100%)'
    )
    image.save(output_path, format='png')


def float_in_range(vmin, vmax):
    def _float_in_range(number):
        try:
            f = float(number)
        except ValueError:
            raise argparse.ArgumentTypeError(
                'Argument must be a float type number')

        if not (vmin <= f <= vmax):
            raise argparse.ArgumentTypeError(
                f'Argument must be within {vmin} <= arg <= {vmax}')

        return f

    return _float_in_range


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw a circle')
    parser.add_argument(
        '-d', type=float_in_range(0, 399), help='diameter of a circle')
    parser.add_argument(
        '-hue', type=float_in_range(0, 360),  help='hue of the HSV color of a circle')
    parser.add_argument(
        '-path', type=str, help='output path of generated image')

    args = parser.parse_args()

    draw_image(args.d, args.hue, args.path)


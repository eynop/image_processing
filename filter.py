from PIL import Image, ImageColor
import numpy as np
from stack import horizontal


def _compute_color_matrix(height, width, rgb, intensity):

    r, g, b = rgb
    
    red = np.full((height, width, 1), r) * intensity
    green = np.full((height, width, 1), g) * intensity
    blue = np.full((height, width, 1), b) * intensity

    matrix = np.uint8(np.concatenate((red, green, blue), axis=2))

    return matrix

def single_color(image, color):

    img = Image.open(image)
    rgb = ImageColor.getrgb(color)

    width, height = img.size

    pixels = np.array(img)
    intensity = np.average(pixels, axis=2).reshape((height, width, 1)) / 255

    new_pixels = _compute_color_matrix(height, width, rgb, intensity)

    return Image.fromarray(new_pixels)


def single_solid_color(image, color):

    img = Image.open(image)
    rgb = ImageColor.getrgb(color)

    width, height = img.size

    pixels = np.array(img)
    intensity = np.average(pixels, axis=2).reshape((height, width, 1))
    mean = np.mean(intensity)
    intensity = (intensity > mean).astype(int)

    new_pixels = _compute_color_matrix(height, width, rgb, intensity)

    return Image.fromarray(new_pixels)


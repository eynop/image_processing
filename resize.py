import argparse

from PIL import Image

# library local imports
import utils


def _compute_scale(width, height, new_width, new_height):
    
    if new_width is not None and height is not None:
        return new_width/width if width > height else new_height/height

    if new_width is not None:
        return new_width/width

    return new_height/height


def resize(image, width=None, height=None):

    print('Resizing ', image)

    img = utils.image(image)
    w, h = img.size
    
    scale = _compute_scale(w, h, width, height)

    nh, nw = int(h * scale), int(w * scale)
    if scale < 1:
        return img.resize((nw, nh), Image.NEAREST)
    else:
        return img.resize((nw, nh), Image.BICUBIC)


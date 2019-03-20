import argparse
import sys
import os

from PIL import Image

# library local imports
import utils


DIR = 'resized'


def resize(image, width=None, height=None):

    print('Resizing ', image)
    img = utils.image(image)
    w, h = img.size
    
    if width is not None and height is not None:
        scale = width/w if w > h else height/h
    elif width is not None:
        scale = width/w
    else:
        scale = height/h

    nh, nw = int(h * scale), int(w * scale)
    if scale < 1:
        return img.resize((nw, nh), Image.NEAREST)
    else:
        return img.resize((nw, nh), Image.BICUBIC)


def resize_save(images, width=None, height=None):

    if not os.path.exists(DIR):
        os.mkdir(DIR)

    if isinstance(images, str):
        resized = resize(images, width, height)
        resized.save(os.path.join(DIR, images))
    else:
        for i in images:
            resized = resize(i, width, height)
            resized.save(os.path.join(DIR, i))


if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument('-iw', '--width', dest='width', type=float, default=None)
    args.add_argument('-ih', '--height', dest='height', type=float, default=None)
    args, unknown = args.parse_known_args()

    if args.width is None and args.height is None:
        raise ValueError('Specify width or height or both of new image')

    resize(unknown, args.width, args.height)


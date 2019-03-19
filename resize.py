import argparse
import sys
import os

from PIL import Image


DIR = 'resized'


def resize(images, width, height):
    if not os.path.exists(DIR):
        os.mkdir(DIR)

    for i in images:
        print('Resizing ', i)
        img = Image.open(i)
        w, h = img.size
        
        if width is not None and height is not None:
            scale = width/w if w > h else height/h
        elif width is not None:
            scale = width/w
        else:
            scale = height/h

        nh, nw = int(h * scale), int(w * scale)
        if scale < 1:
            new_img = img.resize((nw, nh), Image.NEAREST)
        else:
            new_img = img.resizei((nw, nh), Image.BICUBIC)

        new_img.save(os.path.join(DIR, i))


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-iw', '--width', dest='width', type=float, default=None)
    args.add_argument('-ih', '--height', dest='height', type=float, default=None)
    args, unknown = args.parse_known_args()

    if args.width is None and args.height is None:
        raise ValueError('Specify width or height or both of new image')

    resize(unknown, args.width, args.height)


#!/usr/bin/python3
import os
import time
import argparse

import resize
import stack


DIR = 'processed'


def do_resize(args, images):
    
    for i in images:
        img = resize.resize(i, args.width, args.height)
        _save_img(img)


def do_stack(args, images):
    
    img = stack.stack(images, args.horizontal, args.vertical)
    _save_img(img)


def _save_img(img):
    
    if not os.path.exists(DIR):
        os.mkdir(DIR)

    ts = str(time.time()).replace('.', '_')
    fname = ts + '.jpg'
    fpath = os.path.join(DIR, fname)
    print('Saving file: ', fpath)
    img.save(fpath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='commands', dest='command', description='valid commands', help='sub-command help')

    # resize 
    resize_parser = subparsers.add_parser('resize', help='resize images')
    resize_parser.add_argument('-iw', '--width', dest='width', type=float, default=None)
    resize_parser.add_argument('-ih', '--height', dest='height', type=float, default=None)
    resize_parser.set_defaults(func=do_resize)

    # stack
    stack_parser = subparsers.add_parser('stack', help='stack images into strip or grid')
    stack_parser.add_argument('-sh', '--horizontal', dest='horizontal', action='store_true', help='create horizontal strip')
    stack_parser.add_argument('-sv', '--vertical', dest='vertical', action='store_true', help='create vertical strip')
    stack_parser.set_defaults(func=do_stack)

    args, unknown = parser.parse_known_args()

    args.func(args, unknown)
    
    print('Done')


import argparse
import cv2
import sys
import os


DIR = 'resized'


def resize(images, width, height):
    if not os.path.exists(DIR):
        os.mkdir(DIR)

    for i in images:
        print('Resizing ', i)
        img = cv2.imread(i)
        h, w = img.shape[:2]
        
        if width is not None and height is not None:
            scale = width/w if w > h else height/h
        elif width is not None:
            scale = width/w
        else:
            scale = height/h

        nh, nw = int(h * scale), int(w * scale)
        if scale < 1:
            new_img = cv2.resize(img, (nw, nh), cv2.INTER_AREA)
        else:
            new_img = cv2.resize(img, (nw, nh), cv2.INTER_CUBIC)

        cv2.imwrite(os.path.join(DIR, i), new_img)
        

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-iw', '--width', dest='width', type=float, default=None)
    args.add_argument('-ih', '--height', dest='height', type=float, default=None)
    args, unknown = args.parse_known_args()

    if args.width is None and args.height is None:
        raise ValueError('Specify either width or height of new image')

    resize(unknown, args.width, args.height)


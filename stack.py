import os # directory creation
import math # calculation of rows and cols amount
import time # for image name

from PIL import Image

# library local imports
import resize
import utils


DIR = 'stacked'


def stack(images, wide=False, tall=False):

    if wide and tall:
        raise ValueError('Specify either horizontal or vertical, not both')
    
    if wide:
        print('Creating horizontal strip')
        return horizontal(images)

    if tall:
        print('Creating vertical strip')
        return vertical(images)

    print('Creating grid image')
    return grid(images)


def stack_save(images, wide=False, tall=False):

    if not os.path.exists(DIR):
        os.mkdir(DIR)

    strip = stack(images, wide, tall)
    fname = '{}.jpg'.format(str(int(time.time())))
    strip.save(os.path.join(DIR, fname))


def horizontal(images):

    # get imgs as array of Image.Image objects
    imgs = utils.images(images)

    # height of the strip is minimal height of all images
    height = min([i.height for i in imgs])
    resized = [resize.resize(img, None, height) for img in imgs]
    
    # width of the strip is sum of width of all images
    width = sum([img.width for img in resized])

    # create new image for strip
    strip = Image.new('RGB', (width, height))

    # stack images by offseting them by width of previous
    x_offset = 0
    for i in resized:
        strip.paste(i, (x_offset, 0))
        x_offset += i.width

    return strip


def vertical(images):
    
    # get imgs as array of Image.Image objects
    imgs = utils.images(images)

    # width of the strip is minimal width of all images
    width = min([i.width for i in imgs])
    resized = [resize.resize(img, width, None) for img in imgs]

    # height of the strip is sum of height of all images
    height = sum([img.height for img in resized])

    # create new image for strip
    strip = Image.new('RGB', (width, height))

    # stack images by offseting them by height of previous
    y_offset = 0
    for i in resized:
        strip.paste(i, (0, y_offset))
        y_offset += i.height

    return strip


def grid(images):

    amount = len(images)
    cols = math.ceil(math.sqrt(amount))
    rows = math.ceil(amount / cols)

    # get imgs as array of Image.Image objects
    imgs = utils.images(images)
    
    strips = []
    for i in range(rows):
        lower = cols * i
        upper = lower + cols
        if upper >= amount:
            upper = amount
            sham = Image.new('RGB', imgs[upper - 1].size)
            dummies = [sham] * (cols * rows - amount)
            strip_imgs = imgs[lower:upper] + dummies 
        else:
            strip_imgs = images[lower:upper]

        strips.append(horizontal(strip_imgs))

    grid_img = vertical(strips)
    
    return grid_img

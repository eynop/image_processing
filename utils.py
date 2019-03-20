from PIL import Image


def images(images):
    
    return [image(i) for i in images]


def image(image):
    
    if isinstance(image, Image.Image):
        return image

    return Image.open(image)


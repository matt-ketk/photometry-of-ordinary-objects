# imports
import numpy as np
import exif
import rawpy
import exifread 
from PIL import Image
# modules
import directory as direc
kconstant = 4250

def get_luminance(image_name, f_stop=5.0, speed=0.01, iso=4032, k=kconstant):
    pixels = get_brightness(image_name)
    lum = np.zeros((pixels.shape[0], pixels.shape[1]))
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            lum[row][col] = luminance(pixels[row][col], f_stop, speed, iso, k)
    return lum

def get_brightness(image_name):
    pixels = convert_raw(image_name)
    # pixels = convert_image(image_name)
    bright = np.zeros((pixels.shape[0], pixels.shape[1]))
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            bright[row][col] = weighted_brightness(*pixels[row][col])
    return bright

def convert_image(image_name):
    img = Image.open(image_name)
    return np.array(img)
    
def convert_raw(image_name): # turn a raw image into a pixel array
    raw = rawpy.imread(image_name)
    return raw.postprocess()
# may be RAM intensive
def weighted_brightness(r, g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def unweighted_brightness(r, g, b):
    return sum([r, g, b]) / 3

def luminance(n, f_stop, speed, iso, k):
    return n * (f_stop ** 2 / (speed * iso * k))

def callibrate(n, f_stop, speed, iso, luminance):
    pass


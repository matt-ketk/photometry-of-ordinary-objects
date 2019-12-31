# imports
import cupy as cp
import numpy as np
# import exif
import rawpy
# import exifread 
from PIL import Image

# modules
import directory as direc
import filehandling as fh
# constants
kconstant = 4250
brightness_weights = cp.array([0.2126, 0.7152, 0.0722])
f_stop = 5.0
speed = 1/100
iso = 4032

lum_constant = (f_stop ** 2 / (speed * iso * kconstant))

def get_luminance(image_name):
    return lum_constant * get_brightness(image_name)

def get_brightness(image_name):
    pixels = fh.convert_image(image_name)
    weighted_r = pixels[:,:,0] * 0.2126
    weighted_g = pixels[:,:,1] * 0.7152
    weighted_b = pixels[:,:,2] * 0.0722
    return cp.sum(cp.dstack((weighted_r, weighted_g, weighted_b)), axis=2)

def get_wavelength(pixel):
        
    '''return np.sum(something)'''
'''
def get_brightness(image_name):
    # pixels = cp.array(convert_raw(image_name))
    pixels = convert_image(image_name)
    bright = cp.zeros((pixels.shape[0], pixels.shape[1]))
    for ind in np.ndindex(bright.shape):
        bright[ind] = cp.dot(pixels[ind], brightness_weights)
    return bright
'''

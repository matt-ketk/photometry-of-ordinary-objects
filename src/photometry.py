# imports
import numpy as np
# import exif
# import rawpy
# import exifread 
from PIL import Image

# modules
import directory as direc
import filehandling as fh
import constants 
import rgbapprox as rgba
# constants
kconstant = 4250
brightness_weights = np.array([0.2126, 0.7152, 0.0722])
f_stop = 5.0
speed = 1/100
iso = 4032

pixel_width = 3.229E-5 # m
pixel_area = pixel_width ** 2 # m^2

lum_constant = (f_stop ** 2 / (speed * iso * kconstant))

def stefan_boltzmann(pixels): # outputs irradiance per pixel
    # when temperature is -1, ignore
    wavelengths = rgba.get_wavelengths(pixels)
    temperatures = wavelength_to_temperature(wavelengths)
    temperatures_quad = np.power(temperatures, 4, where=temperatures!=0, out=np.zeros_like(temperatures))
    return np.multiply(constants.s, temperatures_quad)
    

def wavelength_to_temperature(wavelengths): # in nanometers
    return np.divide(constants.b, wavelengths * 1E-9, where=wavelengths!=0) 

def get_luminance(pixels):
    return lum_constant * get_brightness(pixels)

def get_brightness(pixels):
    weighted_r = pixels[:,:,0] * 0.2126
    weighted_g = pixels[:,:,1] * 0.7152
    weighted_b = pixels[:,:,2] * 0.0722
    return np.sum(np.dstack((weighted_r, weighted_g, weighted_b)), axis=2)

        
'''
def get_brightness(image_name):
    # pixels = cp.array(convert_raw(image_name))
    pixels = convert_image(image_name)
    bright = cp.zeros((pixels.shape[0], pixels.shape[1]))
    for ind in np.ndindex(bright.shape):
        bright[ind] = cp.dot(pixels[ind], brightness_weights)
    return bright
'''

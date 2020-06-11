# imports
import matplotlib.colors as pltcolor
import numpy as np
from skimage import color
# modules
'''
VERY ROUGH APPROXIMATION OF RGB TO WAVELENGTH
'''
value_threshold = 80

def mean_color(arr):
    return np.array([np.mean(arr[:,0]), np.mean(arr[:,1]), np.mean(arr[:,2])])


_RED = np.array([
    [193, 41, 107],
    [128, 0, 58],
    [47, 0, 19],
    [103, 0, 44],
    [21, 1, 19]
])
RED_AVG = mean_color(_RED).astype(int)

_PURPLE = np.array([
    [90, 47, 137],
    [43, 18, 73],
    [33, 18, 62],
    [17, 7, 39],
    [0, 0 ,28]
])
PURPLE_AVG = mean_color(_PURPLE).astype(int) 

_BLUE = np.array([
    [37, 48, 154],
    [0, 28, 129],
    [10, 30, 121],
    [57, 62, 158],
    [26,38,128]
])
BLUE_AVG = mean_color(_BLUE).astype(int)

_BLACK = np.array([
    [5, 1, 8],
    [10, 4, 13],
    [5, 1, 9],
    [4, 0, 9],
    [6, 1, 11]
])
BLACK_AVG = mean_color(_BLACK).astype(int)

palette = [RED_AVG, BLUE_AVG, PURPLE_AVG, BLACK_AVG] # wavelength is in nanometers, black is just wack
wavelength_palette = [685E-9, 477E-9, 415E-9, -1]

'''
for each pixel get the rough approximation of its wavelength. assume it is peak wavelength from a black-body.
''' 
# version 3

weight = 60.47873459
bias = 475.7787967
def get_wavelengths(pixels):
    hsv_values = convert_hsv(pixels)
    inverse_hsv = np.divide(1, hsv_values[:,:,0], where=(hsv_values[:,:,2]>value_threshold), out=np.zeros_like(hsv_values[:,:,0]))
    inverse_hsv -= 1
    log = np.log(inverse_hsv, where=inverse_hsv>0, out=np.zeros_like(inverse_hsv))
    log *= weight
    return np.add(log, bias, where=log!=0.0)
    # return np.sum(log, bias, where=log>0, out=np.zeros_like(log))
''' version 1
def get_wavelengths(pixels):
    comparison_matrices = []
    for color in palette:
        # np.append(comparison_matrices, color_comparison_matrix(pixels, color))        
        comparison_matrices.append(color_comparison_matrix(pixels, color))

    stacked = np.dstack(comparison_matrices)

    return np.vectorize(wavelength_palette.__getitem__)(np.argmin(stacked, axis=2))
'''   
''' version 2 
def get_wavelengths(pixels):
    hsv_values = pltcolor.rgb_to_hsv(pixels) # get hue values from rgb pixels, capped from 0 to 270
    scale = np.multiply(170E-9, hsv_values[:,:,0], where=hsv_values[:,:,2]>value_threshold,out=-np.ones_like(hsv_values[:,:,0]))
    return np.subtract(620E-9, scale, where=scale>0, out=np.zeros_like(scale))    
    # return 620 - (170 / 270 * hue_values)
'''

def convert_hsv(pixels):
    hsv_unadjusted = pltcolor.rgb_to_hsv(pixels)
    exceeded = hsv_unadjusted[:,:,0] > 270/360
    hsv_unadjusted[exceeded] = 1 - hsv_unadjusted[exceeded]
    return hsv_unadjusted

def color_comparison_matrix(pixels, compare_color):
    pixels_lab = color.rgb2lab(pixels)
    color_dec = compare_color / 255
    return np.linalg.norm(pixels_lab - compare_color, axis=2, out=-1)

    
def color_distance(pix0, pix1):
    return np.norm(pix0 - pix1)
    



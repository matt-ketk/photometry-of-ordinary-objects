# imports
import numpy as np
from skimage import color
# modules
'''
VERY ROUGH APPROXIMATION OF RGB TO WAVELENGTH
'''
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
wavelength_palette = [685, 477, 415, -1]


def get_wavelengths(pixels):
    comparison_matrices = []
    for color in palette:
        # np.append(comparison_matrices, color_comparison_matrix(pixels, color))        
        comparison_matrices.append(color_comparison_matrix(pixels, color))

    stacked = np.dstack(comparison_matrices)

    return np.vectorize(wavelength_palette.__getitem__)(np.argmin(stacked, axis=2))
    
def color_comparison_matrix(pixels, compare_color):
    pixels_lab = color.rgb2lab(pixels)
    color_dec = compare_color / 255
    return np.linalg.norm(pixels_lab - compare_color, axis=2)

    
def color_distance(pix0, pix1):
    return np.norm(pix0 - pix1)
    



# imports
import numpy as np
import exif
# modules
import directory as dir
def weighted_brightness(r, g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def unweighted_brightness(r, g, b):
    return sum([r, g, b]) / 3

def luminance(n, f_stop, speed, iso, k):
    return n * (f_stop ** 2 / (speed * iso * k))

def callibrate(n, f_stop, speed, iso, luminance):
    
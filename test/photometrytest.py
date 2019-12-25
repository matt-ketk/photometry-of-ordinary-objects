# imports
import numpy as np
# modules

def weighted_brightness(r, g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def unweighted_brightness(r, g, b):
    return sum([r, g, b]) / 3

def luminance(n, f_stop, speed, iso, k):
    return n * (f_stop ** 2 / (speed * iso * k))

def callibrate(n, f_stop, speed, iso, luminance):
    return (n * f_stop ** 2) / (luminance * speed * iso)

# the following pixels are from a patch of sky
callibrate_pix = np.array([[125,185,239],
[125,186,240],
[122,183,237],
[124,184,238],
[125,185,239]])

# sky luminance is about 4.0 cd/m^2
sky_luminance = 4.0
constants = np.array([])

for p in callibrate_pix:
    n = weighted_brightness(*p)
    constants = np.append(constants, [callibrate(n, 11, 1/80, 100, sky_luminance)])
print(constants)
print("average callibration constant: ", str(sum(constants) / constants.size))
# print(callibrate_pix)
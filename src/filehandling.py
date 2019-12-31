# imports
import cupy as cp
import numpy as np
import rawpy
import os
from PIL import Image
# modules
import directory as d

RAW_EXTENSION = '.NEF'
IMPORT_EXTENSION = '.npy'

def import_from_images(overwrite=False):
    exists = set()
    if not overwrite:
        # exists = set(file for file in os.listdir(d.RAW))
        for file in os.listdir(d.RAW):
            exists.add(os.path.splitext(file)[0])
    # to_import = set(os.listdir(d.IMAGES)).difference(exists)
    to_import = set()
    for file in os.listdir(d.IMAGES):
        if file.endswith(RAW_EXTENSION):
            to_import.add(os.path.splitext(file)[0])
    to_import = to_import.difference(exists)

    counter = 1
    for file in to_import:
        print(file)
        import_image_as_npy(d.IMAGES + file + RAW_EXTENSION, file)
        print('Importing image {} of {}'.format(str(counter), str(len(to_import))))
        counter += 1


def import_image_as_npy(image_dir, name):
    np.save(d.RAW + name + IMPORT_EXTENSION, convert_raw(image_dir))

def convert_image(image_name):
    return cp.array(Image.open(image_name))

def convert_raw(image_name):
    return rawpy.imread(image_name).postprocess()
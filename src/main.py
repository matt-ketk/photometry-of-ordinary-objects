# packages
import skimage
import skimage.feature
import skimage.viewer
import sys
import matplotlib
import matplotlib.pyplot as plt
import cupy as cp
import numpy as np
from matplotlib.colors import LogNorm 
# modules
import directory as d
import cl_interface as cl
import photometry as ph
import debugtools as db
import filehandling as fh
def main():
    # cl.main_menu()
    # cplotmesh_view(d.LUMINANCE + 'sample_1.csv')
    # import_raw()
    fh.import_from_images()



def cplotmesh_view(save_file):
    z = np.loadtxt(open(save_file, 'rb'), delimiter=',', skiprows=1)
    plt.title('Luminance of Plasma Ball (cd/m2)')
    plt.imshow(z, origin='upper')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()

'''
    Z = ph.get_luminance(d.IMAGES + 'DSC_1353.tiff')
    print(Z.shape)
    fig, (ax0, ax1) = plt.subplots(2, 1)

    c = ax0.pcolor(Z)
    ax0.set_title('default: no edges')

    c = ax1.pcolor(Z)
    ax1.set_title('no edges')

    fig.tight_layout()
    plt.show() 
'''
'''
    t0 = db.getCurrentTimeMillis()

    luminance_sample = cp.asnumpy(ph.get_luminance(d.IMAGES + 'DSC_1353.tiff'))

    print(db.getCurrentTimeMillis() - t0)
    t0 = db.getCurrentTimeMillis()

    np.savetxt(d.LUMINANCE + 'sample_1.csv', luminance_sample, delimiter=',')     
    print(db.getCurrentTimeMillis() - t0)
'''
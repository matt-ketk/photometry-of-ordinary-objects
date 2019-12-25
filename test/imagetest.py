# packages
import skimage
import skimage.feature
import skimage.viewer
import sys
# modules
import directory

filename = sys.argv[1]
sigma = float(sys.argv[2])
low_threshold = float(sys.argv[3])
high_threshold = float(sys.argv[4])

image = skimage.io.imread(fname=filename, as_gray=True)
edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold
)

viewer = skimage.viewer.ImageViewer(edges)
viewer.show()

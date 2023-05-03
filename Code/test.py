import os, glob
from skimage import io
from matplotlib import pyplot as plt
data_dir = "D:/Documents/Masters/Spring 2023/Deep Learning/DL Project/Training data/parts/"
idx = 0
mask_name = str(idx) + '_class.png'
img = io.imread(os.path.join(data_dir, 'masks/', mask_name))
io.imshow(img)
plt.show()
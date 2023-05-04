import os
from natsort import natsorted
os.getcwd()

collection = "D:/Documents/Masters/Spring 2023/Deep Learning/DL Project/Git/DL-Project/Training data/instrument/train/raw"

for i,filename in enumerate(natsorted(os.listdir(collection))):
    os.rename(collection + "/" + filename, collection + "/" + str(i) + ".png")

import os
from natsort import natsorted
os.getcwd()

collection = "../Training data/parts/parts/masks"
keyword = "class"
for i,filename in enumerate(natsorted(os.listdir(collection))):
    if keyword in filename:
        os.rename(collection + "/" + filename, collection + "/" + str(i) + "_class.png")

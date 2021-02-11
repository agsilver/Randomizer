from random import randint
import os

files = os.listdir()
directroy = os.path.dirname(os.path.realpath(__file__))
img_formats = ["bmp", "jpg", "peg", "tif", "iff", "png", "gif"]

for file in files:
    if file[-3:] in img_formats:
        rn_num = str(randint(1, 200000))
        old_name = os.path.join(directroy, file)
        file_name, file_extension = os.path.splitext(old_name)
        new_name = os.path.join(directroy, rn_num + file_extension)
        os.rename(old_name, new_name)


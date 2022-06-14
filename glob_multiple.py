# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:22:56 2022

@author: sdeni
"""

import cv2 
import glob

file_list =glob.glob ("C:/Users/sdeni/OneDrive/Belgeler/software/*.*")
print(file_list)
my_list = []

path = "C:/Users/sdeni/OneDrive/Belgeler/software/input_images/*.*"
for file in glob.glob(path):
    print(file)
    
    a =cv2.imread(file)
    my_list.append(a)
    
from matplotlib import pyplot as plt
plt.imshow(my_list[2])
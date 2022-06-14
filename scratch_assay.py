# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:28:38 2022

@author: sdeni
"""

from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import io, img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu
import glob
import cv2
from scipy.stats import linregress
time = 0
time_list =[]
area_list =[]
path="./input_images/scratch_assay/*.*"



for file in glob.glob(path):
    img = io.imread(file, cv2.COLOR_BAYER_BGGR2GRAY)
    #print(img.shape)
    img = img_as_ubyte(img)
       
    entropy_img = entropy(img,disk(10))
    thresh = threshold_otsu(entropy_img)
    binary = entropy_img <= thresh
    scratch_area = np.sum(binary == True)
    print(time,scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)

    
    print(thresh)
    print(np.sum(binary== True))
    plt.imshow(binary)
    time+=1
print(time_list,area_list)

plt.plot(time_list, area_list, 'bo')


slope, intercept, r_value, p_value, std_err = linregress(time_list,area_list)
print("y=", slope, "x=", "+" , intercept)
print("R\N{SUPERSCRIPT TWO} = ", r_value**2)


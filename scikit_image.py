# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:31:30 2022

@author: sdeni
"""

from skimage import io, restoration
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as st

img = io.imread("./input_images/microscope3_blur2.jpg", as_gray= True)

#psf = np.ones((3,3))/9
def gkern(kernlen = 21, nsig=2):
    
    lim = kernlen//2 + (kernlen%2)/2
    x = np.linspace((-lim), lim, kernlen+1)
    kern1d =np.diff(st.norm.cdf(x))
    kern2d= np.outer(kern1d, kern1d)
    return kern2d/kern2d.sum()

psf = gkern(5,3)
deconvolved, _ = restoration.unsupervised_wiener(img, psf)
plt.imsave("./output_images/microscope3_decon1.png",deconvolved, cmap="gray")
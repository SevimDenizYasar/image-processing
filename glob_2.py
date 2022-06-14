# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:46:47 2022

@author: sdeni
"""

import cv2 
import glob



path = "C:/Users/sdeni/OneDrive/Belgeler/software/input_images/*.*"
img_number =1 
for file in glob.glob(path):
    print(file)
    
    a = cv2.imread(file)
   
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imwrite("C:/Users/sdeni/OneDrive/Belgeler/software/output_images/lena_color"+str(img_number) + ".jpg",c)
    img_number +=1
    cv2.imshow('lena_color',c)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
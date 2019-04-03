# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:59:33 2019

@author: Vern Francisco
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

os.chdir("C:/Users/avern/Pictures")

image = mpimg.imread('test.jpg')

print('This is image is: ', type(image), ' with dimensions: ',image.shape)

# Grab the x and y size and make a copy of the image

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

# Define color selection criteria
red_thresh = 180
green_thresh = 180
blue_thresh = 200

rgb_thresh = [red_thresh, green_thresh, blue_thresh]

# Identify pixels below the threshold
thresholds = ((image[:,:,0] < rgb_thresh[0])
              | (image[:,:,1] < rgb_thresh[1])
              | (image[:,:,2] < rgb_thresh[2]))

color_select[thresholds] = [0,0,0]

plt.imshow(color_select)


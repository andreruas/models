from __future__ import print_function
import cv2
import os, os.path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


print (cv2.__version__)

imageDir = "Combined8-1/test_labels" #specify your path here
image_path_list = []
valid_image_extensions = [".png",".jpg"] #specify your image extension here

blue = [255,128,0]
black = [0,0,0]
purple = [255,0,128]
green = [0,255,0]

#this will loop through all files in imageDir
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

for imagePath in sorted(image_path_list):
    img = cv2.imread(imagePath)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    if img is None:
        continue
        
    height, width, _ = img.shape
    
    for i in range(height):
        for j in range(width):
            if (img[i,j] == blue).all():
                gray_image[i,j] = 0
            elif (img[i,j] == black).all():
                gray_image[i,j] = 1
            elif (img[i,j] == purple).all():
                gray_image[i,j] = 2
            elif (img[i,j] == green).all():
                gray_image[i,j] = 3
            else:
                gray_image[i,j] = 4
                


    cv2.imwrite(imagePath,gray_image)
    print("Writing " + imagePath + " ... ")

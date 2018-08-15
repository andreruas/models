from __future__ import print_function
import cv2
import os, os.path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


print (cv2.__version__)

imageDir = "Combined8-1-mn/Combined8-1-mn/images/validation" #specify your path here
image_path_list = []
valid_image_extensions = [".png",".jpg"] #specify your image extension here

#this will loop through all files in imageDir
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

for imagePath in sorted(image_path_list):
    img = cv2.imread(imagePath)
    

    if img is None:
        continue
                
    img = img[0:512,256:768]

    cv2.imwrite(imagePath,img)
    print("Writing " + imagePath + " ... ")

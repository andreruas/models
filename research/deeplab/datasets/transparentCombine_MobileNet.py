from __future__ import print_function
import cv2
import os, os.path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


print (cv2.__version__)

imageDir = "segmentation_results/" #specify your path here
image_path_list = []
valid_image_extensions = [".png",".jpg"] #specify your image extension here

#this will loop through all files in imageDir
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

for imagePath in sorted(image_path_list):
    img1 = cv2.imread(imagePath)


    imagePath2 = imagePath[:-9]
    print(imagePath2)

    img2 = cv2.imread(imagePath2+"prediction.png")
    #print(imagePath2)

    if img1 is None:
        continue

    if img2 is None:
        continue

    combined = cv2.addWeighted(img1,0.6,img2,0.4,0)
    imagePath3 = "combined/" + imagePath


    cv2.imwrite(imagePath3,combined)
    print("Writing " + imagePath3 + " ... ")

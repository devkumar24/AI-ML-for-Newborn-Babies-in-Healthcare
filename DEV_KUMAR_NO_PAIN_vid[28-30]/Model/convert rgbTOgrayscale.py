# Code to convert the RGB images into GrayScale Images

# Import necessary packages
import os
import cv2

# source and destination path where we want to store the images
source_path = "../Images/RGB/"
destination_path = "../Images/GRAY_SCALE/"


if len(os.listdir(destination_path)) == 0: # check if destination folder has its sub-category folder i.e., mild, moderate and severe
    # if the folder is empty, we have created all the 3 category folders
    for p in os.listdir(source_path):
        path = os.path.join(destination_path, p)
        os.mkdir(path = path)

else: # If category folders are present, just pass
    pass

# lambda function to get the category to which the images should be pushed.
category = lambda path : path.split("/")[-1]
# code to convert the RGB image into Gray scale and pushed to destinatio folder
for p in os.listdir(source_path):
    path = os.path.join(source_path, p) # path to sub-folder of the source folder
    if len(os.listdir(path)) == 0: # if there is no sub-folder, then pass because no use of running the code.
        pass
    else:
        try:
            for i in os.listdir(path): 
                image_path = os.path.join(path, i) # path to the particular image
                image = cv2.imread(image_path) # reading an image
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converting the image to GRAYSCALE
                des_path = os.path.join(destination_path, category(path)) # destination_path with particular category
                des_path = os.path.join(des_path, image_path.split("/")[-1]) # destination path with the corresponding image
                cv2.imwrite(des_path, gray_image) # pushed the image.
        except: # This statement will happen, if the image is already grayscale or can't be converted into grayscale.
            print("Images can't be Converted")
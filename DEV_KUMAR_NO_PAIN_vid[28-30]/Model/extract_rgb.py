# Import necessary modules
import os
import cv2
import glob

# Create 2 seperate folder for RGB as well as GRAY SCALE Images
try:
    if not os.path.exists("../Images/RGB"): # Check if RGB Folder exists or not
        os.mkdir("../Images/RGB")
    if not os.path.exists("../Images/GRAY_SCALE"): # Check if GRAYSCALE Folder exists or not
        os.mkdir("../Images/GRAY_SCALE")
except : # If the folder already exists then pass
    pass

# get the list of all videos
video_dir = glob.glob("../Videos/*.mp4")

i = 1
for video in video_dir:
    frame_no = 1 # pointer to count no. of images being created
    video_capture = cv2.VideoCapture(video) # Video file to be opened
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            i += 1
            if i%12 == 0:
                # Name of the image
                name = "../Images/RGB/{}_{}.jpg".format(video[10:-14],frame_no)
                # writing Image
                cv2.imwrite(name, frame)
                print("Creating Image {}".format(name))
                frame_no += 1
        else:
            break
    
    video_capture.release()
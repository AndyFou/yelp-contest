# import the necessary packages
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

# MAIN FUNCTION OF SCRIPT: loads a set of photos and gets SIFT & SURF keypoints
# Photo Structure: [FILENAME,PHOTO,GRAYSCALE_PHOTO,KEYPOINTS_SIFT,KEYPOINTS_SURF]
def main():
	photos = loadimages()				# load photos from folder

	for photo in photos:
		findsiftfeatures(photo)			# find sift features and save keypoints
		findsurffeatures(photo)			# find surf features and save keypoints

# LOAD PHOTOS FROM FOLDER & SAVE IN A LIST [FILENAME,PHOTO,GRAYSCALE_PHOTO]
def loadimages():
	photos = [] 					# create "photos" list
	photosdir = "photos"				# set folder name ("photosdir")

	for filename in os.listdir(photosdir):
		image = cv2.imread(os.path.join(photosdir,filename))	#read photo
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)		#convert to grayscale
		photos.append([filename, image, gray])			#append in a list of photos

	return photos

# FIND SIFT FEATURES FOR A PHOTO
def findsiftfeatures(photo):
	sift = cv2.xfeatures2d.SIFT_create()
	(kps,sift) = sift.detectAndCompute(photo[2],None)
	photo.append(kps)

# FIND SURF FEATURES FOR A PHOTO
def findsurffeatures(photo):
	surf = cv2.xfeatures2d.SURF_create()
	(kps,surf) = surf.detectAndCompute(photo[2],None)
	photo.append(kps)

# SHOW IMAGE FILE
def showimage(image):
	cv2.imshow('image',image)
	cv2.waitKey(0)

main()

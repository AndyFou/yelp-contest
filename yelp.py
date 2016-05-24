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
	photos = [] 						# create "photos" list
	photosdir = "photos"				# set folder name ("photosdir")

	for filename in os.listdir(photosdir):
		image = cv2.imread(os.path.join(photosdir,filename))	#read photo
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)			#convert to grayscale
		photos.append([filename, image, gray])					#append in a list of photos

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



# *************************************************** NOTES ********************************************************

# SYSTEM
# * load virtual environment: source cv/bin/activate
# * mv ~/Desktop/Yelp/various/train_photos/IMAGEFILE ~/Desktop/Yelp/photos/

# PYTHON
# * Find length: len(DATATYPE)

# * List: Homogenous(contains same types)	!!THE MOST CONVENIENT AND FLEXIBLE !!
# 	Tuple: Immutable(if created, nothing can be added) & Heterogenous(can contain different types)
#	Set: --einai sunola opote an exeis ena stoixeio sto sunolo den mporeis na baleis 2o idio --, Example Application: it can be used to find a distinct set of words
#	Dictionary: Works like a hashmap

# * Find item in nested list: photos[i][j]
# * Print concatenation (string & int): print "Hello ",x," ",y," World"


#Show Keypoints: showimage(cv2.drawKeypoints(photo[2],kps,None,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))

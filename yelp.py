# import the necessary packages
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import collections
import pdb
import csv

# MAIN FUNCTION OF SCRIPT: loads a set of photos and gets SIFT & SURF keypoints
# Photo Structure: [FILENAME,PHOTO,GRAYSCALE_PHOTO,KEYPOINTS_SURF]
def main():
	photos = loadimages()				# load photos from folder

	descriptors = []
	photovector = []
	for photo in photos:
		descriptors.append(findsurffeatures(photo))	# find surf features and save keypoints
		photovector.append([photo[0]])			# feed ids into photovector (to be)

	dataset = preparePOIdata(descriptors)			# create POIvector

	assignCentersPOI(dataset,min(map(len,descriptors)),photovector)		# 1st clustering step: cluster and assign centers (aka create photovector)
	#photovector is now full with the values of clusters that belong to each photo

	getRestPhoto()


##############################  2nd CLUSTERING  ######################################

# PREPARE DESCRIPTORS FOR CLUSTERING
#Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
#def preparePhotoData(photovector):


# PREPARE DESCRIPTORS FOR CLUSTERING
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def getRestPhoto():
	csv_file = open("train_photo_to_biz_ids.csv","rb")
    	reader = csv.reader(csv_file)
	bus_im = {}
	
	for item in list(reader):
		if item[1] in bus_im:
			bus_im[item[1]].append(item[0])
		else:
			bus_im[item[1]] = [item[0]]
	
	print(bus_im)

##############################  1st CLUSTERING  ######################################

#ASSIGN CENTERS IN PHOTOS
def assignCentersPOI(data,minPOI,photovector):
	clusters = collections.defaultdict(int)
	labels = clustering(data, 2048)

	for i in range(len(photovector)):
		clusters = collections.defaultdict(int)

		for j in range(minPOI*i,minPOI*(i+1)):
			clusters[labels[j]] += 1

		for cluster in clusters.keys():
			photovector[i].append(cluster)

	#print(len(photovector),len(photovector[0]),len(photovector[1]),len(photovector[6]),type(photovector[0]))

# CLUSTERING IN POI
# Load dataset, which is a list of keypoints
def clustering(data,num_clusters):
	kmeans_model = KMeans(num_clusters, random_state=1).fit(data)
	labels = kmeans_model.labels_

	return labels

# PREPARE DESCRIPTORS FOR CLUSTERING
#Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def preparePOIdata(descriptors):
	# make descriptors same size for all photos
	mindesc = min(map(len,descriptors))

	dataset = []
	for i in range(len(descriptors)):
		for j in range(mindesc):
			dataset.append(descriptors[i][j])

	return dataset

###################################  PHOTOS  ###########################################

# LOAD PHOTOS FROM FOLDER & SAVE IN A LIST [FILENAME,PHOTO,GRAYSCALE_PHOTO]
def loadimages():
	photos = [] 					# create "photos" list
	photosdir = "photos"				# set folder name ("photosdir")

	for filename in os.listdir(photosdir):
		image = cv2.imread(os.path.join(photosdir,filename))	#read photo
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)		#convert to grayscale
		photos.append([filename, image, gray])			#append in a list of photos

	return photos

# FIND SURF FEATURES FOR A PHOTO AND RETURN DESCRIPTORS
def findsurffeatures(photo):
	surf = cv2.xfeatures2d.SURF_create()
	(kps,surf) = surf.detectAndCompute(photo[2],None)
	photo.append(kps)
	descriptors = surf

	return descriptors

# SHOW IMAGE FILE
def showimage(image):
	cv2.imshow('image',image)
	cv2.waitKey(0)

###################################  OTHER  ###########################################

# PRINT IN FILE
def writeInFile(items):
	text_file = open("tmp3.txt","w")

	for item in items:
		text_file.write(str(item) + "\n")

	text_file.close()

###################################  CALL MAIN  ###########################################

main()

# import the necessary packages
import os
import numpy as np
from numpy import array
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import collections
import pdb
import csv
import re

# MAIN FUNCTION OF SCRIPT: loads a set of photos and gets SIFT & SURF keypoints
# Photo Structure: [FILENAME,PHOTO,GRAYSCALE_PHOTO,KEYPOINTS_SURF]
def main():
	photos = loadimages("sample_photos")			# load photos from folder

	descriptors = []
	photovector = []
	for photo in photos:
		descriptors.append(findsurffeatures(photo))	# find surf features and save keypoints
		photovector.append([photo[0]])			# feed ids into photovector (to be)

	dataPOI = preparePOIdata(descriptors)			# create POIvector

	assignCentersPOI(dataPOI,min(map(len,descriptors)),photovector)		# 1st clustering step: cluster and assign centers (aka create photovector)
	#photovector is now full with the values of clusters that belong to each photo
	
	dataPhoto = preparePhotoData(photovector)
	
	labels = clustering(dataPhoto,500)
	writeInFile(labels,"labels")

##############################  2nd CLUSTERING  ######################################

# PREPARE DESCRIPTORS FOR CLUSTERING
#Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def preparePhotoData(photovector):
	bus_im = getSampleRestPhoto()

	sample_ids = []	
	# create id list
	for photo in photovector:
		tmp = re.sub(".jpg","",photo[0])
		sample_ids.append(tmp)

	dataset = []
	for restaurant in bus_im:
		for image in restaurant[1]:
			if image in sample_ids:
				for img in photovector:
					#print(img,type(img[0]),len(img))
					if re.sub(".jpg","",img[0])==image:
						dataset.append(array(img[1:min(map(len,photovector))]))

	return dataset

# GET SAMPLE RESTAURANT_PHOTOS ids	
def getSampleRestPhoto():
	bus_im_list = getRestPhoto()
	
	return bus_im_list[:50]


# GET RESTAURANT_PHOTOS FROM FILE
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def getRestPhoto():
	csv_file = open("train_photo_to_biz_ids.csv","rb")
    	reader = csv.reader(csv_file)
	bus_im = {}
	bus_im_list = []
	
	for item in list(reader):
		if item[1] in bus_im:
			bus_im[item[1]].append(item[0])
		else:
			bus_im[item[1]] = [item[0]]
	
	for key,value in bus_im.iteritems():
		bus_im_list.append([key,value])

	return bus_im_list

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
def loadimages(filename):
	photos = [] 					# create "photos" list
	photosdir = filename				# set folder name ("photosdir")

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
def writeInFile(items,filename):
	text_file = open(filename+".txt","w")

	for item in items:
		text_file.write(str(item) + "\n")

	text_file.close()

###################################  CALL MAIN  ###########################################

main()

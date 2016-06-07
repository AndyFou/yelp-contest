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
	photos = loadimages("photos")				# load photos from folder
	print("sampling: done!")	

	descriptors = []
	photovector = []
	for photo in photos:
		tmp=findsurffeatures(photo)
		if tmp is not None:
			descriptors.append(tmp)			# find surf features and save keypoints
			photovector.append([photo[0]])		# feed ids into photovector (to be)
	
	print("loading: done!")

	dataPOI = preparePOIdata(descriptors)					# create POIvector
	assignCentersPOI(dataPOI,min(map(len,descriptors)),photovector)		# 1st clustering step: cluster and assign centers
	#photovector is now full with the values of clusters that belong to each photo
	print("1st clustering: done!")
	
	busid = []
	busvectorim = []
	dataPhoto = preparePhotoData(photovector,busid,busvectorim)
	busvector = assignCentersPhotos(dataPhoto,busid,busvectorim)		# 2nd clustering step: cluster and assign centers
	print("2nd clustering: done!")

	print("Congratulations! The program is finished and you are still alive!")

	writeInFile(busvector,"busvector")

##############################  2nd CLUSTERING  ######################################

# ASSIGN CENTERS IN RESTAURANTS
def assignCentersPhotos(data,busid,busvectorim):	
	#busvector = [[busid[x]] for x in range(len(busid))]
	busvector = []
	for id in busid:
		busvector.append([id])	

	# Clustering step
	labels = clustering(data, 3)

	x=0
	for i in range(len(busid)):
		clusters = collections.defaultdict(int)

		for j in range(x,(len(busvectorim[i])-1+x)):
			clusters[labels[j]] += 1
		
		for cluster in clusters.keys():
			busvector[i].append(cluster)

		x = x + len(busvectorim[i])-1

	return busvector

# PREPARE DESCRIPTORS FOR CLUSTERING
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def preparePhotoData(photovector,busid,busvectorim):
	bus_im = getRestPhoto()

	sample_ids = []	
	# create id list
	for photo in photovector:
		tmp = re.sub(".jpg","",photo[0])
		sample_ids.append(tmp)

	dataset = []
	for restaurant in bus_im:
		for image in restaurant[1]:
			if image in sample_ids:
				if restaurant[0] not in busid:
					busid.append(restaurant[0])
					busvectorim.append(['0'])
					busvectorim[busid.index(restaurant[0])].append(image)
				else:
					busvectorim[busid.index(restaurant[0])].append(image)
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

# ASSIGN CENTERS IN PHOTOS
def assignCentersPOI(data,minPOI,photovector):
	
	# Clustering step
	labels = clustering(data, 2048)

	for i in range(len(photovector)):
		clusters = collections.defaultdict(int)

		for j in range(minPOI*i,minPOI*(i+1)):
			clusters[labels[j]] += 1

		for cluster in clusters.keys():
			photovector[i].append(cluster)

# PREPARE DESCRIPTORS FOR CLUSTERING
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def preparePOIdata(descriptors):
	# make descriptors same size for all photos
	mindesc = min(map(len,descriptors))

	dataset = []
	if mindesc:
		for i in range(len(descriptors)):
			for j in range(mindesc):
				dataset.append(descriptors[i][j])

	return dataset

##################################  CLUSTERING  ##########################################

# Load dataset and train kmeans model
def clustering(data,num_clusters):
	kmeans_model = KMeans(num_clusters, random_state=1).fit(data)
	labels = kmeans_model.labels_

	return labels

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
	(kps,descriptors) = surf.detectAndCompute(photo[2],None)
	photo.append(kps)

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

# load train & combine
# create arff file

import pdb
import csv

def main():
	numclusters = 100
	numlabels = 9

	dataset = createRichDataset("test",numlabels)
	
	labels = createLabels(numclusters,numlabels)
	
	writeInFileCSV(dataset,"test-dataset4",labels)
	writeInFileARFF(dataset,"test-dataset4",numclusters,numlabels)


###############################  CREATE FILES  #######################################

# GET RESTAURANT_PHOTOS FROM FILE
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def createRichDataset(kindofdataset,numlabels):
	datafile = open(""+kindofdataset+"Dataset4.csv","r")
	dreader = csv.reader(datafile)

	# FOR TRAIN
	#labelfile = open(""+kindofdataset+".csv","rb")
	#lreader = csv.reader(labelfile)

	busids = []
	dataset = []
	# Read clustering results
	for line in dreader:
		busids.append(line[0])
		dataset.append(line[:len(line)])
	
	# FOR TEST
	for i in range(9):
		[dataset[x].append('?') for x in range(len(dataset))]
	
	# FOR TRAIN
	# Read labels data and combine with clustering results
	#for line in lreader:
	#	if line[0] in busids:
	#		for bus in dataset:
	#			if bus[0]==line[0]:
	#				for x in range(numlabels):
	#					if str(x) in line[1]:
	#						bus.append('1')
	#					else:
	#						bus.append('0')

	return dataset

# GET RESTAURANT_PHOTOS FROM FILE
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def createPlainDataset(kindofdataset):
	datafile = open(""+kindofdataset+"Dataset.csv","r")
	dreader = csv.reader(datafile)

	labelfile = open(""+kindofdataset+".csv","rb")
	lreader = csv.reader(labelfile)

	busids = []
	dataset = []
	# Read clustering results
	for line in dreader:
		busids.append(line[0])
		dataset.append(line[:len(line)])
	
	# Read labels data and combine with clustering results
	for line in lreader:
		if line[0] in busids:
			for bus in dataset:
				if bus[0]==line[0]:
					bus.append(line[1])

	return dataset

###################################  PRINT  ###########################################

# PRINT IN ARFF FILE
def writeInFileARFF(items,filename,numclusters,numlabels):
	arff_file = open(filename+".arff","w")

	arff_file.write("@relation " + filename + "\n\n")
	arff_file.write("@attribute business_id numeric\n")

	for num in range(numclusters):
		arff_file.write("@attribute cluster" + str(num+1) + " numeric\n")

	for num in range(numlabels):
		arff_file.write("@attribute label" + str(num+1) + " {0,1}\n")	

	arff_file.write("\n@data\n")	

	for item in items:
		[arff_file.write(str(item[x]) + ",") for x in range(len(item)-1)]
		arff_file.write(str(item[len(item)-1]) + "\n")

	arff_file.close()

# PRINT IN CSV FILE
def writeInFileCSV(items,filename,labels):
	csv_file = open(filename+".csv","w")

	[csv_file.write(labels[x] + ",") for x in range(len(labels)-1)]
	csv_file.write(labels[len(labels)-1] + "\n")

	for item in items:
		[csv_file.write(str(item[x]) + ",") for x in range(len(item)-1)]
		csv_file.write(str(item[len(item)-1]) + "\n")

	csv_file.close()

# CREATE LABELS FOR DATASET
def createLabels(numclusters,numlabels):
	labels = ["business_id"]

	for num in range(numclusters):
		labels.append("cluster" + str(num+1))

	for num in range(numlabels):
		labels.append("label" + str(num+1))

	return labels

main()

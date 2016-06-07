# load train & combine
# create arff file

import pdb
import csv

def main():
	#plaindataset = createPlainDataset("train")
	#writeInFileCSV(plaindataset,"plaindata")

	richdataset = createRichDataset("train",9)
	
	labels = ["business_id","cluster1","cluster2","cluster3","label1","label2","label3","label4","label5","label6","label7","label8","label9"]
	#to-add createLabels function	
	writeInFileCSV(richdataset,"richdataset",labels)


###############################  CREATE FILES  #######################################

# GET RESTAURANT_PHOTOS FROM FILE
# Structure of Dataset: List[numpy.ndarray] - 4781 POI[64 values]
def createRichDataset(kindofdataset,numlabels):
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
					for x in range(numlabels):
						if str(x) in line[1]:
							bus.append('1')
						else:
							bus.append('0')

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

# PRINT IN CSV FILE
def writeInFileCSV(items,filename,labels):
	csv_file = open(filename+".csv","w")

	[csv_file.write(labels[x] + ",") for x in range(len(labels)-1)]
	csv_file.write(labels[len(labels)-1] + "\n")

	for item in items:
		[csv_file.write(str(item[x]) + ",") for x in range(len(item)-1)]
		csv_file.write(str(item[len(item)-1]) + "\n")

	csv_file.close()

# PRINT IN ARFF FILE
def writeInFileARFF(items,filename):
	text_file = open(filename+".txt","w")

	for item in items:
		text_file.write(str(item) + "\n")

	text_file.close()

main()

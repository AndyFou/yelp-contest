import csv
import pdb

def main():
	dataset = getRestPhoto("test")	#getRestPhoto("test",50)
	writeInFileTXT(dataset[:2500],"sample_ids1")
	writeInFileTXT(dataset[2501:5000],"sample_ids2")
	writeInFileTXT(dataset[5001:7500],"sample_ids3")
	writeInFileTXT(dataset[7501:],"sample_ids4")
	#print(dataset[0])
	#print(dataset[1])

# GET PHOTO IDS
def getRestPhoto(kindofdataset):	#getRestPhoto(kindofdataset,sample)
	csv_file = open(""+kindofdataset+"_photo_to_biz.csv","rb")		#train_photo_to_biz_ids.csv / test_photo_to_biz.csv
    	reader = csv.reader(csv_file)
	bus_im = {}
	bus_im_list = []
	bus_sample_list = []	# FOR TEST ONLY
	
	for item in list(reader):
		if item[1] in bus_im:
			if item[0] not in bus_im[item[1]]:
				bus_im[item[1]].append(item[0])
		else:
			bus_im[item[1]] = [item[0]]
	
	for key,value in bus_im.iteritems():
		bus_im_list.append([key,value])

	# FOR TEST ONLY
	for item in bus_im_list:
		bus_sample_list.append([item[0],item[1][:3]])
	
	return bus_sample_list	#bus_im_list[:sample]

# PRINT IN TXT FILE
def writeInFileTXT(items,filename):
	text_file = open(filename+".txt","w")

	for item in items:
		#text_file.write(str(item) + "\n")
		[text_file.write(str(item[1][x]) + "\n") for x in range(len(item[1]))]

	text_file.close()

main()

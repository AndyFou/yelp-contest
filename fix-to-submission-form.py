import pdb
import csv

busids = []
busids2 = []
data = []
write_file = open("final-test.csv","w")

read_subm = open("sample_submission.csv","r")
dataset_subm = csv.reader(read_subm)

for line in list(dataset_subm):
	if line[0] not in busids:
		busids.append(line[0])
	
	#pdb.set_trace()

read_res = open("final2.csv","r")
dataset_res = csv.reader(read_res)

lista = list(dataset_res)

for business in busids:
	for line in lista:
		if line[0]==business:
			#write_file.write(line)
			busids2.append(line[0])
			[write_file.write(str(line[x]) + ",") for x in range(len(line)-1)]
			write_file.write(str(line[len(line)-1]) + "\n")
		#pdb.set_trace()

for business in busids:
	if business not in busids2:
		print(business)
		
read_subm.close()
read_res.close()
write_file.close()
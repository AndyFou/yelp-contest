from shutil import copyfile
import re

idfile = open("sample_ids.txt","rb")

for line in idfile:
	print(line)
	copyfile("/home/andy/Desktop/dokimes/train_photos/"+re.sub("\n","",line)+".jpg","/home/andy/Desktop/dokimes/sample_data/"+re.sub("\n","",line)+".jpg")

idfile.close()

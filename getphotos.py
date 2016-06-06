from shutil import copyfile
import re

idfile = open("id.txt","rb")

for line in idfile:
	print(line)
	copyfile("/home/andy/Desktop/Yelp/train_photos/"+re.sub("\n","",line)+".jpg","/home/andy/Desktop/Yelp/sample_photos/"+re.sub("\n","",line)+".jpg")

idfile.close()

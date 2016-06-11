from shutil import copyfile
import re

idfile = open("sample_ids4.txt","rb")

for line in idfile:
	print(line)
	copyfile("/home/andy/Desktop/dokimes/test_photos/"+re.sub("\n","",line)+".jpg","/home/andy/Desktop/dokimes/sample_data4/"+re.sub("\n","",line)+".jpg")

idfile.close()

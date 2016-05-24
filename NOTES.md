# PERSONAL NOTES

## SYSTEM
* Load virtual environment: _source cv/bin/activate_
* Move photos: _mv ~/Desktop/Yelp/various/train_photos/IMAGEFILE ~/Desktop/Yelp/photos/_

## PYTHON
* Find length: __len(__*DATATYPE*__)__
* List vs Tuple vs Set vs Dictionary: 

   **STRUCTURE** | **NOTES** 
   ------------- | --------- 
   List | Homogenous _(contains same types)_
   Tuple | Immutable _(if created, nothing can be added)_ & _Heterogenous(can contain different types)_
   Set | > Είναι σύνολα οπότε αν έχεις ένα στοιχείο στο σύνολο δεν μπορείς βα βάλεις 2ο ίδιο 
         > Example Application: it can be used to find a distinct set of words
   Dictionary | Works like a HashMap
   
* Find item in nested list: _photos[i][j]_
* Print concatenation (string & int): _print "Hello ",x," ",y," World"_

### REST
Show Keypoints: showimage(cv2.drawKeypoints(photo[2],kps,None,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))

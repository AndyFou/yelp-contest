# PERSONAL NOTES

## SYSTEM
* Load virtual environment: _source cv/bin/activate_
* Move photos: _mv ~/Desktop/Yelp/various/train_photos/IMAGEFILE ~/Desktop/Yelp/photos/_

## PYTHON
* Find length: __len(*DATATYPE*)__
* List vs Tuple vs Set vs Dictionary: 
  * __List__: Homogenous(contains same types)	!!THE MOST CONVENIENT AND FLEXIBLE !!
  * __Tuple__: Immutable(if created, nothing can be added) & Heterogenous(can contain different types)
  * __Set__: --einai sunola opote an exeis ena stoixeio sto sunolo den mporeis na baleis 2o idio --, Example Application: it can be used to find a distinct set of words
  * __Dictionary__: Works like a hashmap
* Find item in nested list: _photos[i][j]_
* Print concatenation (string & int): _print "Hello ",x," ",y," World"_

### REST
Show Keypoints: showimage(cv2.drawKeypoints(photo[2],kps,None,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))

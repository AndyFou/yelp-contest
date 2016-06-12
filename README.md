# Participation to the **Yelp** Competition of Kaggle

### DATASET

##### Training
Restaurants: 2000
Images: 234843

##### Test
Restaurants: 10000
Images: ~237000

### DEPENDENCIES

##### Dependencies for SURF & Clustering (http://mulan.sourceforge.net/)
* python 3.x
* openCV 2.4
* scikit-learn

(to make python 3 and openCV work for SURF follow the instructions in this link: http://www.pyimagesearch.com/2015/07/16/where-did-sift-and-surf-go-in-opencv-3/)

##### Dependencies for Classification 
* weka 3.7.10
* java 1.7 or higher
* mulan 1.5 (http://mulan.sourceforge.net/)

### PROCEDURE: 
- [x] Load images
- [x] Find POI (SIFT / SURF & OpenCV) & form POIVector
- [x] Clustering on POI in order to form PhotoVector
- [x] Clustering on Images in order to get form BusinessVector
- [x] Form training dataset from BusinessVector and labels
- [x] Classification & evaluation on training dataset 
- [x] Predictions on test dataset


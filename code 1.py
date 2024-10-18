
import cv2


import cv2 as cv


cam_port = 0
cam = cv.VideoCapture(cam_port) 


result, image = cam.read() 


if result: 

	
	cv.imshow("testimage", image) 

	
	cv.imwrite("testimage.png", image) 


	cv.waitKey(0) 
	cv.destroyWindow("testimage") 

else: 
	print("No image detected. Please! try again") 





import os
os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"
import json
from deepface import DeepFace
database = ["Angelina_Jolie_2_June_2014_(cropped).jpg","Angelina_Jolie-643531_(cropped).jpg","naman.jpg","nikhil.jpg","pixelcut-export.png","WhatsApp Image 2024-10-19 at 02.05.20_fb0fea45.jpg","jassa.png"]
k=0
while(True):
	
  result = DeepFace.verify(
        img1_path= "testimage.png",
        img2_path= database[k],)
  x=json.dumps(result)
  verification = x[13]
  print('attendance'+''+ verification)
  k=k+1
  if verification =='t':break

  
 
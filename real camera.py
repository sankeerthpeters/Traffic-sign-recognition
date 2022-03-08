# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:36:48 2021

@author: Sankeerth
"""

import numpy as np
import cv2
from tensorflow.keras.models import loa

#camera resolution
framewidth = 640
frameheight = 480
brightness = 180
threshold = 0.90
font = cv2.FONT_HERSHEY_SIMPLEX

#Setup video camera
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, brightness)

#load model
model = load_model("D:\\github repositories\\Traffic-sign-recognition\\my_model.h5")

def greyscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = greyscale(img)
    img = equalize(img)
    img = img/255
    return img

def getclassname(classno):
    if classno == 1: return 'Speed limit (20km/h)'
    elif classno == 2: return 'Speed limit (30km/h)' 
    elif classno == 3: return 'Speed limit (50km/h)', 
    elif classno == 4: return 'Speed limit (60km/h)', 
    elif classno == 5: return 'Speed limit (70km/h)', 
    elif classno == 6: return 'Speed limit (80km/h)', 
    elif classno == 7: return 'End of speed limit (80km/h)', 
    elif classno == 8: return 'Speed limit (100km/h)', 
    elif classno == 9: return 'Speed limit (120km/h)', 
    elif classno == 10: return 'No passing', 
    elif classno == 11: return 'No passing veh over 3.5 tons', 
    elif classno == 12: return 'Right-of-way at intersection', 
    elif classno == 13: return 'Priority road', 
    elif classno == 14: return 'Yield', 
    elif classno == 15: return 'Stop', 
    elif classno == 16: return 'No vehicles', 
    elif classno == 17: return 'Veh > 3.5 tons prohibited', 
    elif classno == 18: return 'No entry', 
    elif classno == 19: return 'General caution', 
    elif classno == 20: return 'Dangerous curve left', 
    elif classno == 21: return 'Dangerous curve right', 
    elif classno == 22: return 'Double curve', 
    elif classno == 23: return 'Bumpy road', 
    elif classno == 24: return 'Slippery road', 
    elif classno == 25: return 'Road narrows on the right', 
    elif classno == 26: return 'Road work', 
    elif classno == 27: return 'Traffic signals', 
    elif classno == 28: return 'Pedestrians', 
    elif classno == 29: return 'Children crossing', 
    elif classno == 30: return 'Bicycles crossing', 
    elif classno == 31: return 'Beware of ice/snow',
    elif classno == 32: return 'Wild animals crossing', 
    elif classno == 33: return 'End speed + passing limits', 
    elif classno == 34: return 'Turn right ahead',
    elif classno == 35: return 'Turn left ahead', 
    elif classno == 36: return 'Ahead only', 
    elif classno == 37: return 'Go straight or right', 
    elif classno == 38: return 'Go straight or left', 
    elif classno == 39: return 'Keep right', 
    elif classno == 40: return 'Keep left', 
    elif classno == 41: return 'Roundabout mandatory', 
    elif classno == 42: return 'End of no passing', 
    elif classno == 43: return 'End no passing veh > 3.5 tons'
    
while True:
    
    #read image
    success, imgoriginal = cap.read()
    
    #process image
    img = np.asarray(imgoriginal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("processed image", img)
    img = img.reshape(1, 32, 32, 1)
    cv2.putText(imgoriginal, "CLASS: ", (20,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
    cv2.putText(imgoriginal, "PROBABILITY: ", (20,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
    
    #predict image
    
    predictions = model.predict(img)
    probabilityvalue = np.amax(predictions)
    
    if probabilityvalue > threshold:
        cv2.putText(imgoriginal, str(classindex)+" "+str(getclassname(classindex)), (120,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(imgoriginal, str(round(probabilityvalue*100,2))+ "%", (180,75), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        
    cv2.imshow("result", imgoriginal)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

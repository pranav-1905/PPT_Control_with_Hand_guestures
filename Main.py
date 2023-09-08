# from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np

# Parameters
width, height = 1280, 720
# gestureThreshold = 300
folderPath = "Presentation"


# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


# Variables
imgList = []
delay = 30
buttonPressed = False
counter = 0
drawMode = False
imgNumber = 0
delayCounter = 0
annotations = [[]]
annotationNumber = -1
annotationStart = False
hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image


# Get list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

while True:
    # Get image frame
    success, img = cap.read()
    # img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    cv2.imshow("Image",img)
    cv2.imshow("Slides", imgCurrent )
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
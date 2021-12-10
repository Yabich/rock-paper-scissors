import cv2.cv2 as cv2
import mediapipe as mp
import numpy as np
import sys
from Geometry import *

handsDetector = mp.solutions.hands.Hands()
image = cv2.imread("1.jpg")
image = np.fliplr(image)
results = handsDetector.process(image)
width = image.shape[1]
height = image.shape[0]
if results.multi_hand_landmarks is not None:
    print('No hands on the picture')
    sys.exit()
elif len(results.multi_hand_landamarks) > 1:
    print('There is only one hand on the picture')
else:
    hand1 = results.multi_hand_landmarks[0].landmark
    hand2 = results.multi_hand_landmarks[1].landmark
    thumb1 = Vector(hand1[1].x, hand1[1].y, hand1[4].x, hand1[4].y)
    thumb2 = Vector(hand2[1].x, hand2[1].y, hand2[4].x, hand2[4].y)
    thumb1.x *= width
    thumb1.y *= height
    thumb2.x *= width
    thumb2.y *= height
    index1 = Vector(hand1[5].x, hand1[5].y, hand1[8].x, hand1[8].y)
    index2 = Vector(hand2[5].x, hand2[5].y, hand2[8].x, hand2[8].y)
    index1.x *= width
    index1.y *= height
    index2.x *= width
    index2.y *= height
    middle1 = Vector(hand1[9].x, hand1[9].y, hand1[12].x, hand1[12].y)
    middle2 = Vector(hand2[9].x, hand2[9].y, hand2[12].x, hand2[12].y)
    middle1.x *= width
    middle1.y *= height
    middle2.x *= width
    middle2.y *= height
    ring1 = Vector(hand1[13].x, hand1[13].y, hand1[16].x, hand1[16].y)
    ring2 = Vector(hand2[13].x, hand2[13].y, hand2[16].x, hand2[16].y)
    ring1.x *= width
    ring1.y *= height
    ring2.x *= width
    ring2.y *= height
    pinky1 = Vector(hand1[17].x, hand1[17].y, hand1[20].x, hand1[20].y)
    pinky2 = Vector(hand2[17].x, hand2[17].y, hand2[20].x, hand2[20].y)
    pinky1.x *= width
    pinky1.y *= height
    pinky2.x *= width
    pinky2.y *= height

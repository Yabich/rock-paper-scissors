from cv2 import cv2
import mediapipe as mp
import numpy as np
from Geometry import *
import math


def get_points(landmark, shape):
    points = []
    for mark in landmark:
        points.append([mark.x * shape[1], mark.y * shape[0]])
    return np.array(points, dtype=np.int32)


handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, image = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(image)
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    results = handsDetector.process(flippedRGB)
    width = image.shape[1]
    height = image.shape[0]
    if results.multi_hand_landmarks is None:
        cv2.putText(flippedRGB, 'no hands', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
    elif len(results.multi_hand_landmarks) < 2:
        hand1 = results.multi_hand_landmarks[0].landmark
        point0 = Point(hand1[0].x * width, hand1[0].y * height)
        point5 = Point(hand1[5].x * width, hand1[5].y * height)
        palm = math.hypot(point0.x - point5.x, point0.y - point5.y)
        point12 = Point(hand1[12].x * width, hand1[12].y * height)
        point16 = Point(hand1[16].x * width, hand1[16].y * height)
        fingertip = math.hypot(point12.x - point16.x, point12.y - point16.y)
        point4 = Point(hand1[4].x * width, hand1[4].y * height)
        point20 = Point(hand1[20].x * width, hand1[20].y * height)
        fulldist = math.hypot(point4.x - point20.x, point4.y - point20.y)
        (x, y), r = cv2.minEnclosingCircle(get_points(results.multi_hand_landmarks[0].landmark, flippedRGB.shape))
        if 2 * r / palm > 1.4 and 2 * r / fingertip > 3 and 2 * r / fulldist < 2.3:
            cv2.putText(flippedRGB, 'paper', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
        elif 2 * r / palm < 1.8 and 2 * r / fingertip > 4:
            cv2.putText(flippedRGB, 'rock', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
        elif 2 * r / palm < 2.6 and 2 * r / fingertip < 3 and 2 * r / fulldist > 2.3:
            cv2.putText(flippedRGB, 'scissors', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
        else:
            cv2.putText(flippedRGB, 'nothing', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=2)
    else:
        res1 = False
        res2 = False
        hand1 = results.multi_hand_landmarks[0].landmark
        hand2 = results.multi_hand_landmarks[1].landmark
        point0 = Point(hand1[0].x * width, hand1[0].y * height)
        point5 = Point(hand1[5].x * width, hand1[5].y * height)
        palm = math.hypot(point0.x - point5.x, point0.y - point5.y)
        point0 = Point(hand2[0].x * width, hand2[0].y * height)
        point5 = Point(hand2[5].x * width, hand2[5].y * height)
        palm2 = math.hypot(point0.x - point5.x, point0.y - point5.y)
        point12 = Point(hand1[12].x * width, hand1[12].y * height)
        point16 = Point(hand1[16].x * width, hand1[16].y * height)
        fingertip = math.hypot(point12.x - point16.x, point12.y - point16.y)
        point12 = Point(hand2[12].x * width, hand2[12].y * height)
        point16 = Point(hand2[16].x * width, hand2[16].y * height)
        fingertip2 = math.hypot(point12.x - point16.x, point12.y - point16.y)
        point4 = Point(hand1[4].x * width, hand1[4].y * height)
        point20 = Point(hand1[20].x * width, hand1[20].y * height)
        fulldist = math.hypot(point4.x - point20.x, point4.y - point20.y)
        point4 = Point(hand2[4].x * width, hand2[4].y * height)
        point20 = Point(hand2[20].x * width, hand2[20].y * height)
        fulldist2 = math.hypot(point4.x - point20.x, point4.y - point20.y)
        (x, y), r = cv2.minEnclosingCircle(get_points(results.multi_hand_landmarks[0].landmark, flippedRGB.shape))

        if 2 * r / palm < 2.6 and 2 * r / fingertip < 3 and 2 * r / fulldist > 2.3:
            cv2.putText(flippedRGB, 'scissors', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
            res1 = 'scissors'
        elif 2 * r / palm > 1.5 and 2 * r / fingertip > 3:
            cv2.putText(flippedRGB, 'paper', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
            res1 = 'paper'
        elif 2 * r / palm < 1.5 and 2 * r / fingertip > 4:
            cv2.putText(flippedRGB, 'rock', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
            res1 = 'rock'
        else:
            cv2.putText(flippedRGB, 'nothing', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=2)
            res1 = False

        if 2 * r / palm2 < 2.6 and 2 * r / fingertip2 < 3 and 2 * r / fulldist2 > 2.3:
            cv2.putText(flippedRGB, 'scissors', (500, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
            res2 = 'scissors'
        elif 2 * r / palm2 > 1.5 and 2 * r / fingertip2 > 3:
            cv2.putText(flippedRGB, 'paper', (500, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
            res2 = 'paper'
        elif 2 * r / palm2 < 1.5 and 2 * r / fingertip2 > 4:
            cv2.putText(flippedRGB, 'rock', (500, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
            res2 = 'rock'
        else:
            cv2.putText(flippedRGB, 'nothing', (500, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=2)
            res2 = False
        if (res1=='rock' and res2 == 'scissors') or (res1=='scissors' and res2 == 'paper') or (res1 == 'paper' and res2 == 'rock'):
            cv2.putText(flippedRGB, 'Player 1 won', (200, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
        elif (res2=='rock' and res1 == 'scissors') or (res2=='scissors' and res1 == 'paper') or (res2 == 'paper' and res1 == 'rock'):
            cv2.putText(flippedRGB, 'Player 2 won', (200, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
        elif res1 == False or res2 == False:
            pass
        else:
            cv2.putText(flippedRGB, 'Draw', (200, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2)
    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hands", res_image)
handsDetector.close()

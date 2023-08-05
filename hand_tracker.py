import cv2
import mediapipe as mp

from gestures import Gestures


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
hands_landmark = mpHands.HandLandmark
mpDraw = mp.solutions.drawing_utils

class HandTracker():
	def __init__(self) -> None:
		while True:
			_, img = cap.read()
			imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			ready_hands = hands.process(imgRGB)
				
			if ready_hands.multi_hand_landmarks:
				for hand in ready_hands.multi_hand_landmarks:
					
					mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
					Gestures.left_click(hand, img)
					Gestures.right_click(hand, img)
			
			cv2.imshow("Hands tracker", img)
			if cv2.waitKey(1) == ord('q'):
				break
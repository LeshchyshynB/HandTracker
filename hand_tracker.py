import cv2
import mediapipe as mp


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
					print(hand.x)
					mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
					lmlist = []
					for id, lm in enumerate(hand.landmark):
						h, w, c = img.shape
						cx, cy = int(lm.x*w), int(lm.y*h)
						lmlist.append([id,cx,cy])

					if lmlist[4][2] - lmlist[8][2] <= 15 and lmlist[4][1] - lmlist[8][1] <= 10:
						print("Yes")
			
			cv2.imshow("Hands tracker", img)
			if cv2.waitKey(1) == ord('q'):
				break
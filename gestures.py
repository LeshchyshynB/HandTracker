import pyautogui as pg
import time

class Gestures():

	@classmethod
	def landmarks(self, hand, img):
		lmlist = []
		for id, lm in enumerate(hand.landmark):
			h, w, c = img.shape
			cx, cy = int(lm.x*w), int(lm.y*h)
			lmlist.append([id,cx,cy])
		return lmlist

	@classmethod
	def left_click(self, hand, img):
		lmlist = self.landmarks(hand, img)

		if (lmlist[4][2] - lmlist[8][2] <= 15 and lmlist[4][2] - lmlist[8][2] >= 0) and (lmlist[4][1] - lmlist[8][1] <= 10 and lmlist[4][1] - lmlist[8][1] >= 0):
			print(time.strftime('%M, %S'), "click")
			return pg.click()

	@classmethod
	def right_click(self, hand, img):
		lmlist = self.landmarks(hand, img)

		if (lmlist[4][2] - lmlist[20][2] <= 5 and lmlist[4][2] - lmlist[20][2] >= -5) and (lmlist[4][1] - lmlist[8][1] <= 5 and lmlist[4][1] - lmlist[8][1]>= -5):
			print(time.strftime('%M, %S'), "LO")
			return pg.click()
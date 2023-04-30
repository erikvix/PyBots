import pyautogui as bot
import keyboard
from time import sleep
import schedule
import cv2
import numpy as np
import pyscreenshot as ImageGrab


tela = cv2.imread('imgtest.png')
ref = cv2.imread('gc2.png')

result = cv2.matchTemplate(tela, ref, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = ref.shape[1]
h = ref.shape[0]

cv2.rectangle(
    tela, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)

threshold = 0.8

yloc, xloc = np.where(result >= threshold)
for (x, y) in zip(xloc, yloc):
    cv2.rectangle(
        tela, (x, y), (x + w, y + h), (0, 255, 255), 2)

cv2.imshow("ola", tela)
cv2.imshow("2", result)
cv2.waitKey(0)

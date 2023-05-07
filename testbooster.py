import keyboard
from time import sleep
import win32api
import win32con
import schedule
import threading
from tkinter import Image
import cv2
import numpy as np
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode


tela = cv2.imread('imgtest.png')
ref = cv2.imread('gc.png')
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
result = cv2.matchTemplate(tela, ref, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = ref.shape[1]
h = ref.shape[0]

cv2.rectangle(
    tela, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)

threshold = .60

yloc, xloc = np.where(result >= threshold)
for (x, y) in zip(xloc, yloc):
    cv2.rectangle(
        tela, (x, y), (x + w, y + h), (0, 255, 255), 2)
# tela.resize()

cv2.imshow("ola", tela)
cv2.waitKey(0)

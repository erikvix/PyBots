import pyautogui as bot
import keyboard
from time import time
import schedule
import cv2
import numpy as np
import pyscreenshot as ImageGrab

loop_time = time()
while True:
    im = ImageGrab.grab()
    im = np.array(im)
    im = im[:, ::, ::-1].copy()

    cv2.imshow("tela", im)

    cv2.waitKey(1)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

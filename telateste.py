import pyautogui as bot
import keyboard
from time import time
import schedule
import cv2
import numpy as np
import pyscreenshot as ImageGrab
import win32con
import win32gui
import win32ui
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode
mouse = MouseController()


def window_capture():
    w = 1600
    h = 900

    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img


def GoldenCookie():
    upgradeDisplayGC = window_capture()
    img = upgradeDisplayGC, 0
    template = cv2.imread('goldencookietransp.png', 0)
    gh, gw = template.shape
    # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    img2 = cv2.cvtColor(upgradeDisplayGC, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = max_loc

    bottom_right = (location[0] + gw, location[1] + gh)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.namedWindow('Golden_Cookie_Match', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Golden_Cookie_Match', 960, 540)
    cv2.imshow('Golden_Cookie_Match', img2)
    GCx, GCy = max_loc
    mouse.position = (GCx + 50, GCy + 50)
    mouse.click(Button.left, 1)


schedule.every(3).seconds.do(GoldenCookie)

loop_time = time()
while True:
    schedule.run_pending()
    screenshot = window_capture()

    # cv2.imshow("tela", screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

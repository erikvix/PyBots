import pyautogui as bot
import keyboard
from time import sleep
import win32api
import win32con
import win32ui
import win32gui
import schedule
import numpy as np
import cv2


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def upgradeCapture():
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


def ClickerUpgrade():
    bot.moveTo = (1252, 195)
    bot.doubleClick()
    bot.moveTo = (289, 440)
    bot.doubleClick()


def clickCookie(c):
    for x in range(int(c)):
        bot.doubleClick(277, 419)


def goldencookie():
    upgradeDisplayGC = upgradeCapture()
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
    # mouse.position = (GCx + 50, GCy + 50)
    # mouse.click(Button.left, 1)


def buyupgrade():
    if bot.locateOnScreen('xd2.png', grayscale=False, confidence=0.8):
        for a in range(3):
            for x in range(8):
                click(1322, 300+x*50)
                sleep(0.5)
        bot.moveTo(277, 423)


# schedule.every(1.5).minutes.do(ClickerUpgrade)
# schedule.every(2).seconds.do(buyupgrade)

bot.hotkey('alt', 'tab')
while keyboard.is_pressed('q') == False:
    # schedule.run_pending()
    clickCookie(50)

    if bot.locateOnScreen('xd2.png', grayscale=False, confidence=0.7):
        for a in range(3):
            click(1252, 187)
            for x in range(10):
                click(1322, 300+x*65)

    # position = bot.locateOnScreen(
    #     'gc2.png', grayscale=True, confidence=0.8)
    # if position:
    #     bot.moveTo(position[0] + 30, position[1] + 30)
    #     bot.doubleClick()

# *! GOLDEN COOKIE: var newShimmer=new Game.shimmer("golden");

# *? TO-DO-LIST:
# *? LOCALIZAR UPGRADE
# *? DESENHAR UM RETÂNGULO VERDE EMCIMA DO UPGRADE
# *? SE LOCALIZAR UPGRADE: CLIQUE

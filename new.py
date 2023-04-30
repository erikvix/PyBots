import pyautogui
import time
pyautogui.pause = 0


def clickCookie(c):
    for x in range(int(c)):
        pyautogui.click(290, 487)


def buyUpgrades():
    pyautogui.click(1635, 256)
    pyautogui.click(1635, 256)
    pyautogui.click(1635, 256)

    pyautogui.click(1908, 996)
    pyautogui.click(1908, 996)
    pyautogui.click(1908, 996)
    for a in range(3):
        for x in range(11):
            pyautogui.click(1850, 1000-x*65)
        pyautogui.click(1908, 135)


count = 100

while True:
    time.sleep(1)
    clickCookie(count)
    count = count*1.1
    buyUpgrades()

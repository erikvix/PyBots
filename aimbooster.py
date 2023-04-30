import pyautogui as bot
import keyboard
from time import sleep
import win32api
import win32con
import schedule


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def clickCookie(c):
    for x in range(int(c)):
        bot.doubleClick(277, 419)


def goldencookie():
    position = bot.locateOnScreen(
        'gc2.png', grayscale=True, confidence=0.8)
    if position:
        bot.moveTo(position[0] + 30, position[1] + 30)
        bot.doubleClick()


def buyupgrade():
    if bot.locateOnScreen('xd2.png', grayscale=False, confidence=0.8):
        click(1251, 191)
        for a in range(3):
            for x in range(3):
                click(1322, 300+x*65)


bot.hotkey('alt', 'tab')
while keyboard.is_pressed('q') == False:
    clickCookie(20)

    if bot.locateOnScreen('xd2.png', grayscale=False, confidence=0.7):
        click(1251, 191)
        for a in range(3):
            for x in range(3):
                click(1322, 300+x*65)
        click(1322, 715)

    position = bot.locateOnScreen(
        'gc2.png', grayscale=True, confidence=0.8)
    if position:
        bot.moveTo(position[0] + 30, position[1] + 30)
        bot.doubleClick()

# *! GOLDEN COOKIE: var newShimmer=new Game.shimmer("golden");

# *? TO-DO-LIST:
# *? LOCALIZAR UPGRADE
# *? DESENHAR UM RETÂNGULO VERDE EMCIMA DO UPGRADE
# *? SE LOCALIZAR UPGRADE: CLIQUE

import pyautogui as bot
import keyboard
from time import sleep
import win32api
import win32con

bot.hotkey('alt', 'tab')
bot.moveTo(x=559, y=428)
bot.click()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    if bot.pixel(430, 378)[0] == 0:
        click(430, 378)
    if bot.pixel(513, 378)[0] == 0:
        click(513, 378)
    if bot.pixel(608, 378)[0] == 0:
        click(608, 378)
    if bot.pixel(691, 378)[0] == 0:
        click(691, 378)

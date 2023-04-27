import pyautogui as bot
import keyboard
from time import sleep
import win32api
import win32con

sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


iml = bot.screenshot(region=(100, 100, 1400, 800))
iml.save(r"C:\Users\Sejus\Desktop\pyautogui\saveimg.png")

# while keyboard.is_pressed('q') == False:
#     pic = bot.screenshot(region=(100, 100, 1400, 800))
#     width, height = pic.size

#     for x in range(0, width, 5):
#         for y in range(0, height, 5):

#             r, g, b = pic.getpixel((x, y))
#             if r == 255:
#                 click(x+100, y+100)

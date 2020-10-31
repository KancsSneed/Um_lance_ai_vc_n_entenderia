import pyautogui
import time

while True:
    time.sleep(0.5)
    if pyautogui.locateOnScreen("dispensar.py") != None:
        pyautogui.click("dispensar.py")
    if pyautogui.locateOnScreen("entrar.py") != None:
        pyautogui.click("entrar.py")
        break
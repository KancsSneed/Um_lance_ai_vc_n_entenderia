import pyautogui
import time
import os

while True:
    time.sleep(0.5)
    if pyautogui.locateOnScreen("dispensar.py", grayscale=True, confidence = 0.8) or pyautogui.locateOnScreen("entrar.py", grayscale=True, confidence = 0.8) != None:
        time.sleep(0.5)
        print(pyautogui.position('dispensar.py'))
        time.sleep(1)
        pyautogui.position(pyautogui.click('entrar.py'))
    else:
        time.sleep(0.5)
        print('Eu não vejo')
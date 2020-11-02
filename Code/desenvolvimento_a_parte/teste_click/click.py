import pyautogui
import time
import os

os.startfile('https://meet.google.com/ozk-wrjk-zcy?pli=1&authuser=1')
while True:
    time.sleep(0.5)
    if pyautogui.locateOnScreen("dependencias/dispensar.py", grayscale=True, confidence = 0.8) != None:
        time.sleep(0.5)
        pyautogui.click("dispensar.py")
    time.sleep(0.5)
    if pyautogui.locateOnScreen("dependencias/entrar.py", grayscale=True, confidence = 0.8) != None:
        time.sleep(0.5)
        pyautogui.click("entrar.py")
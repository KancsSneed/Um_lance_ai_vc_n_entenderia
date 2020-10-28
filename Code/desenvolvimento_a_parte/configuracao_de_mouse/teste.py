import pyautogui
from time import sleep
from pathlib import Path

while True:
    x, y = pyautogui.position()
    sleep(1)
    print(int(x),int(y))
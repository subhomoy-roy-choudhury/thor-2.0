import os 
import pyautogui
from plyer import notification

notification.notify(
title = "Hacker",
message = "You are hacked",
timeout = 10
)
os.system("start cmd") 
os.system("pip install pyautogui")
pyautogui.alert('you are hacked')

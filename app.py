import pyautogui
import keyboard

start = False    
while True:
    if keyboard.is_pressed('f4'):
        start = ~start
        if start:
            pyautogui.moveTo(-1280, 720, duration = 0.5)
            pyautogui.click(button='left')
            pyautogui.mouseDown(button = "left")
        else:
            pyautogui.mouseUp(button = "left")
    if keyboard.is_pressed('f8'):
        break
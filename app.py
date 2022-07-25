import pyautogui
import keyboard
import win32gui

wf_winobj = win32gui.FindWindowEx(None, None, None, "Warframe")
rect = win32gui.GetWindowRect(wf_winobj)
x = rect[0]
y = rect[1]
w = rect[2] - x
h = rect[3] - y

print("press 'f4' to start/stop firing")
print("press 'f8' to stop program")

start = False    
while True:
    if keyboard.is_pressed('f4'):
        start = ~start
        if start:
            pyautogui.moveTo(x + w / 2, y + h / 2, duration = 0.5)
            pyautogui.click(button='left')
            pyautogui.mouseDown(button = "left")
        else:
            pyautogui.mouseUp(button = "left")
    if keyboard.is_pressed('f8'):
        break
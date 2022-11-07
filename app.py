import pyautogui
from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
import win32gui
import time
from pynput import keyboard

app = Application().connect(title = "Warframe")
wf_winobj = win32gui.FindWindowEx(None, None, None, "Warframe")
rect = win32gui.GetWindowRect(wf_winobj)
x = rect[0]
y = rect[1]
w = rect[2] - x
h = rect[3] - y

print("press 'f4' to start firing")
print("press 'f8' to stop program")

start = False
exit_program = False

def on_press(key):
    global start, exit_program
    if key == keyboard.Key.f8:
        exit_program = True
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['f4']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        start = ~start
        if start:
            print("started")
            pyautogui.moveTo(x + w / 2, y + h / 2)
            pyautogui.click(button='left')
            pyautogui.click(button='left')
            app.window().send_keystrokes('f13')
        else:
            print("paused")
            pyautogui.moveTo(x + w / 2, y + h / 2)
            pyautogui.click(button='left')
            pyautogui.mouseDown(button = "left")
            pyautogui.mouseUp(button = "left")

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

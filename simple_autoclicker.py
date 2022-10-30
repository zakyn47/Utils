import pyautogui
from pynput.keyboard import *
import time
import random


print("SHITTEST AUTOCLICKER EVER")
print("**v intervalu zadávat desetinnou TEČKU!**")

zpozdeni = float(input("zadej interval klikání: "))
resume_key = Key.f1
pause_key = Key.f2
quit_key = Key.esc

pause = True
klikam = True


def on_press(key):
    global klikam, pause

    if key == resume_key:
        pause = False
        print("**Klikám**")

    elif key == pause_key:
        pause = True
        print("**Pauza**")

    elif key == quit_key:
        klikam = False
        print("**Stačilo...Končím...**")

def controls():
    print(30*"#")
    print("Bots are ruining Runescape!")
    print(30*"#")
    print("interval = " + str(zpozdeni) + " vteřin")
    print("F1 = Klikej!!")
    print("F2 = Pauza")
    print("esc = Konec")

def main():
    ls = Listener(on_press=on_press)
    ls.start()

    controls()
    while klikam:
        if not pause:
            pyautogui.click(pyautogui.position())
            time.sleep(zpozdeni)

    ls.stop()

if __name__ =="__main__":
    main()

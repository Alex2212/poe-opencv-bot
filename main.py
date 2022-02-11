
from capture import WindowCapture
from utils import Utils
import numpy as np
import os
import keyboard
import time
from threading import Thread
from pynput import keyboard
import cv2 as cv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture("Path of Exile")


currentLife = None
maxLife = None
currentMana = None
maxMana = None

ahk = Utils()


manaParity = 1
lifeParity = 1


def bot():

    global currentLife, maxLife, currentMana, maxMana, lifeParity, manaParity
    while True:
        currentTime = time.time()
        # ==========================================LIFE===================================
        Life = wincap.get_screenshot(93, 816, 117, 19)
        # cv.imshow("Life", Life)
        maxLife, currentLife = Utils.getCurrentAndMaxValue(Utils.readNumbers(Life))
        print("Life:{}/{}".format(currentLife, maxLife))

        # maxLife = 57 #hardcoded

        if (currentLife <= (np.random.uniform(0.65, 0.75) * maxLife)) and (0 != currentLife):

            if lifeParity % 2 != 0:
                ahk.press("1")

                print("*1**Main health port**1*")
                time.sleep(np.random.uniform(0.5, 1))
                lifeParity = lifeParity + 1
                continue
            else:
                ahk.press("3")

                print("*3**Main health port**3*")
                time.sleep(np.random.uniform(0.5, 1))
                lifeParity = lifeParity + 1
                continue

        # ==========================================MANA====================================
        Mana = wincap.get_screenshot(1793, 838, 119, 19)
        # cv.imshow("Mana", Mana)
        maxMana, currentMana = Utils.getCurrentAndMaxValue(Utils.readNumbers(Mana))
        print("Mana:{}/{}".format(currentMana, maxMana))

        # maxMana = 56 #hardcoded

        if (currentMana <= (np.random.uniform(0.25, 0.35) * maxMana)) and (currentMana != 0):
            # mainManaPort = wincap.get_screenshot()
            if manaParity % 2 != 0:
                ahk.press("2")

                print("*2**Main mana port**2*")
                time.sleep(np.random.uniform(0.5, 1))
                manaParity = manaParity + 1
                continue
            else:
                ahk.press("4")

                print("*4**Main mana port**4*")
                time.sleep(np.random.uniform(0.5, 1))
                manaParity = manaParity + 1
                continue
        # =========tickrate 5 times a rsecond======

        time.sleep(0.2)

        if cv.waitKey(1) == ord("-"):
            cv.destroyAllWindows()
            break

    print("Done!")


def macros():
    def on_key_release(key):
        if key == keyboard.Key.space:
            # print("space has been relased")
            ahk.press("r")
            time.sleep(np.random.uniform(0.25, 0.3))
            ahk.press("e")

    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()


if __name__ == "__main__":
    Thread(target=bot).start()
    # Thread(target=macros).start()

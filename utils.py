import cv2 as cv
import numpy as np
from ahk import AHK
import keyboard
import time
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Utils:
    ahk = None

    def __init__(self):
        self.ahk = AHK()

    @staticmethod
    def readNumbers(screen):
        rez = []
        for i in range(0, 11, 1):
            digit = cv.imread((str(i) + ".png"), cv.IMREAD_GRAYSCALE)
            screen2 = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
            thresh = 200
            screen_bw = cv.threshold(screen2, thresh, 255, cv.THRESH_BINARY)[1]
            digit_bw = cv.threshold(digit, thresh, 255, cv.THRESH_BINARY)[1]

            # cv.imshow((str(i)+'.png'),digit_bw)
            # cv.imshow('screen',screen_bw)

            result = cv.matchTemplate(screen_bw, digit_bw, cv.TM_CCOEFF_NORMED)
            treshold = 0.90
            locations = np.where(result >= treshold)  # fint multiple occurances
            locations = list(zip(*locations[::-1]))  # tupplyfy
            for t in locations:
                if t != []:
                    # print('('+str(t[0])+','+str(t[1])+')')
                    rez.append((i, t[0]))
        rez.sort(key=lambda tup: tup[1])
        number = ""
        for i in range(0, len(rez), 1):
            # number += (10 ** (len(rez) - i - 1)) * rez[i][0]
            if rez[i][0] == 10:
                number = number + "/"
            else:
                number = number + str(rez[i][0])
        return str(number)

    @staticmethod
    def getCurrentAndMaxValue(number: str):
        a = 0
        b = 0
        if len(number.split(sep="/")) == 2:
            if number.split(sep="/")[0]:
                a = int(number.split(sep="/")[0])
            if number.split(sep="/")[1]:
                b = int(number.split(sep="/")[1])

        return (b, a)

    @staticmethod
    def KeyPress(key: str):
        time.sleep(np.random.uniform(0.13, 0.32))
        keyboard.press(key)
        time.sleep(np.random.uniform(0.13, 0.32))
        keyboard.release(key)

    def press(self, key: str):
        time.sleep(np.random.uniform(0.13, 0.32))
        self.ahk.key_down(key)
        time.sleep(np.random.uniform(0.13, 0.32))
        self.ahk.key_up(key)

    def getCapsLockState(self):
        return self.ahk.key_state("CapsLock", mode="T")

    def remapKey(self, key: str):
        self.ahk.remapKey(key)
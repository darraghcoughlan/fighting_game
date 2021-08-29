import pygame


class timer():
    def setup():
        global time, framecount, counted
        time = 0
        framecount = 0
        counted = False

    def count(countto):
        global time, framecount, counted
        framecount = framecount + 1
        if framecount >= 60:
            framecount = 0
            time = time + 1
        if time >= countto:
            counted = True

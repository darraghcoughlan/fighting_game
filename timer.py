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

    def setupcountdown(countfrom):
        global countdowntime, countdownframecount, go
        countdowntime = countfrom
        countdownframecount = 0
        go = False

    def countdown(countfrom):
        global countdowntime, countdownframecount, counted, go
        countdownframecount = countdownframecount +1
        if countdownframecount >= 60:
            countdownframecount = 0
            countdowntime = countdowntime - 1
        if countdowntime == 0:
            counted = True
            go = True
        if countdowntime != 0:
            counted = False
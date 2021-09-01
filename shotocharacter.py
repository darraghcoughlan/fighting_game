import pygame

class variables():
    size = HEIGHT, WIDTH = 1080, 1920
    floor = 0
    crouchingfloor = 96
    movementspeed = 1
    jumpheight = HEIGHT / 8
    jumpspeed = 75

class hurtbox():
    size = HEIGHT, WIDTH = 1080, 1920
    standingwidth = WIDTH / 9
    standingheight = HEIGHT / 2.5
    crouchingwidth = WIDTH / 7
    crouchingheight = HEIGHT /4.5

class standingpuchhitbox():
    width = 1000
    height = 50
    y = - 85
    x = 0

class crouchingpunchhitbox():
    width = 225
    height = 50
    y = -85
    x = 0

class standingkickhitbox():
    width = 300
    height = 75
    y = 20
    x = 0

class crouchingkickhitbox():
    width = 350
    height = 50
    y = 65
    x = 0    

class standingpunchknockback():
    xspeed = 10
    xdestination = 100
    yspeed = 50
    ydestination = -50

class crouchingpunchknockback():
    xspeed = 110
    xdestination = 400
    yspeed = 100
    ydestination = -200
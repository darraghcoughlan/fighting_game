import pygame

class variables():
    size = HEIGHT, WIDTH = 1080, 1920
    floor = (HEIGHT/ 10) * 7
    crouchingfloor = 96
    movementspeed = 1
    jumpheight = 10
    jumpspeed = 75

class hurtbox():
    size = HEIGHT, WIDTH = 1080, 1920
    standingwidth = WIDTH / 9
    standingheight = HEIGHT / 2.5
    crouchingwidth = WIDTH / 7
    crouchingheight = HEIGHT /4.5

class standingpuchhitbox():
    width = 250
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

class standingkickknockback():
    xspeed = 110
    xdestination = 800
    yspeed = 50
    ydestination = -50

class crouchingkickknockback():
    xspeed = 100
    xdestination = 50
    yspeed = 150
    ydestination = -450

class damage():
    standingpunch = 3
    crouchingpunch = 5
    standingkick = 4
    crouchingkick = 2

class stun():
    standingpunch = 20
    crouchingpunch = 40
    standingkick = 75
    crouchingkick = 15

class standingkickframedata():
    startup = 10
    active = 10
    endlag = 15

class crouchingkickframedata():
    startup = 7
    active = 5
    endlag = 7

class standingpunchframedata():
    startup = 3
    active = 7
    endlag = 10

class crouchingpunchframedata():
    startup = 10
    active = 5
    endlag = 15
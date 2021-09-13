import pygame

class variables():
    size = HEIGHT, WIDTH = 1080, 1920
    floor = (HEIGHT/ 10) * 6.5
    crouchingfloor = 150
    movementspeed = 1.5
    jumpheight = 10
    jumpspeed = 75

class hurtbox():
    size = HEIGHT, WIDTH = 1080, 1920
    standingwidth = WIDTH / 9.5
    standingheight = HEIGHT / 2
    crouchingwidth = WIDTH / 7.5
    crouchingheight = HEIGHT /4.5

class standingpuchhitbox():
    width = 300
    height = 500
    y = - 275
    x = 0

class crouchingpunchhitbox():
    width = 100
    height = 50
    y = -85
    x = 100

class standingkickhitbox():
    width = 350
    height = 20
    y = 10
    x = 200

class crouchingkickhitbox():
    width = 300
    height = 20
    y = 65
    x = 25

class standingpunchknockback():
    xspeed = 10
    xdestination = 100
    yspeed = 40
    ydestination = -400

class crouchingpunchknockback():
    xspeed = 10
    xdestination = 50
    yspeed = 10
    ydestination = -50

class standingkickknockback():
    xspeed = 20
    xdestination = 200
    yspeed = 50
    ydestination = -50

class crouchingkickknockback():
    xspeed = 40
    xdestination = 100
    yspeed = 50
    ydestination = -50

class damage():
    standingpunch = 3
    crouchingpunch = 1
    standingkick = 10
    crouchingkick = 2

class stun():
    standingpunch = 30
    crouchingpunch = 20
    standingkick = 100
    crouchingkick = 15

class standingkickframedata():
    startup = 30
    active = 3
    endlag = 15

class crouchingkickframedata():
    startup = 7
    active = 3
    endlag = 10

class standingpunchframedata():
    startup = 10
    active = 7
    endlag = 3

class crouchingpunchframedata():
    startup = 2
    active = 3
    endlag = 5
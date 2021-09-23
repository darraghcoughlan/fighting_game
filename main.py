
from pygame.constants import FULLSCREEN, KEYDOWN, KEYUP, KSCAN_ESCAPE, K_ESCAPE

import time, pygame, time, sys
import player1
import player2
import timer
import shotocharacter, swordchar
import camera

camera.setup()
p1char = "sword"
p2char = "shoto"

if p2char == "shoto":
    #hurtbox
    p2standingwidth = shotocharacter.hurtbox.standingwidth
    p2standingheight = shotocharacter.hurtbox.standingheight
    p2crouchingwidth = shotocharacter.hurtbox.crouchingwidth
    p2crouchingheight = shotocharacter.hurtbox.crouchingheight

    p2floor = shotocharacter.variables.floor
    p2crouchingfloor = shotocharacter.variables.crouchingfloor
    p2movementspeed = shotocharacter.variables.movementspeed
    p2jumpspeed = shotocharacter.variables.jumpspeed
    p2jumpheight = shotocharacter.variables.jumpheight

    #standing punch hitbox
    p2standingpunchwidth = shotocharacter.standingpuchhitbox.width
    p2standingpunchheight = shotocharacter.standingpuchhitbox.height
    p2standingpunchy = shotocharacter.standingpuchhitbox.y
    p2standingpunchx = shotocharacter.standingpuchhitbox.x
    p2standingpunchmovex = shotocharacter.standingpuchhitbox.movex
    p2standingpunchmovey = shotocharacter.standingpuchhitbox.movey

    #crouching punch hitbox
    p2crouchingpunchwidth = shotocharacter.crouchingpunchhitbox.width
    p2crouchingpunchheight = shotocharacter.crouchingpunchhitbox.height
    p2crouchingpunchy = shotocharacter.crouchingpunchhitbox.y
    p2crouchingpunchx = shotocharacter.crouchingpunchhitbox.x
    p2crouchingpunchmovex = shotocharacter.crouchingpunchhitbox.movex
    p2crouchingpunchmovey = shotocharacter.crouchingpunchhitbox.movey

    #standing kick hitbox
    p2standingkickwidth = shotocharacter.standingkickhitbox.width
    p2standingkickheight = shotocharacter.standingkickhitbox.height
    p2standingkicky = shotocharacter.standingkickhitbox.y
    p2standingkickx = shotocharacter.standingkickhitbox.x
    p2standingkickmovex = shotocharacter.standingkickhitbox.movex
    p2standingkickmovey = shotocharacter.standingkickhitbox.movey

    #crouch kick hitbox
    p2crouchingkickwidth = shotocharacter.crouchingkickhitbox.width
    p2crouchingkickheight = shotocharacter.crouchingkickhitbox.height
    p2crouchingkicky = shotocharacter.crouchingkickhitbox.y
    p2crouchingkickx = shotocharacter.crouchingkickhitbox.x
    p2crouchingkickmovex = shotocharacter.crouchingkickhitbox.movex
    p2crouchingkickmovey = shotocharacter.crouchingkickhitbox.movey

    #standingpunch knockback
    p2standingpunchknockbackxspeed = shotocharacter.standingpunchknockback.xspeed
    p2standingpunchknockbackxdestination = shotocharacter.standingpunchknockback.xdestination
    p2standingpunchknockbackyspeed = shotocharacter.standingpunchknockback.yspeed
    p2standingpunchknockbackydestination = shotocharacter.standingpunchknockback.ydestination

    #crouchingpunch knockback
    p2crouchingpunchknockbackxspeed = shotocharacter.crouchingpunchknockback.xspeed
    p2crouchingpunchknockbackxdestination = shotocharacter.crouchingpunchknockback.xdestination
    p2crouchingpunchknockbackyspeed = shotocharacter.crouchingpunchknockback.yspeed
    p2crouchingpunchknkockbackydestination = shotocharacter.crouchingpunchknockback.ydestination

    #standingkick knockback
    p2standingkickknockbackxspeed = shotocharacter.standingkickknockback.xspeed
    p2standingkickknockbackxdestination = shotocharacter.standingkickknockback.xdestination
    p2standingkickknockbackyspeed = shotocharacter.standingkickknockback.yspeed
    p2standingkickknockbackydestination = shotocharacter.standingkickknockback.ydestination

    #crouchingkick knockback
    p2crouchingkickknockbackxspeed = shotocharacter.crouchingkickknockback.xspeed
    p2crouchingkickknockbackxdestination = shotocharacter.crouchingkickknockback.xdestination
    p2crouchingkickknockbackyspeed = shotocharacter.crouchingkickknockback.yspeed
    p2crouchingkickknockbackydestination = shotocharacter.crouchingkickknockback.ydestination

    #standingpunch framedata
    p2standingpunchstartup = shotocharacter.standingpunchframedata.startup
    p2standingpunchactive = shotocharacter.standingpunchframedata.active
    p2standingpunchendlag = shotocharacter.standingpunchframedata.endlag

    #crouchingpunch framedata
    p2crouchingpunchstartup = shotocharacter.crouchingpunchframedata.startup
    p2crouchingpunchactive = shotocharacter.crouchingpunchframedata.active
    p2crouchingpunchendlag = shotocharacter.crouchingpunchframedata.endlag

    #standingkick framedata
    p2standingkickstartup = shotocharacter.standingkickframedata.startup
    p2standingkickactive = shotocharacter.standingkickframedata.active
    p2standingkickendlag = shotocharacter.standingkickframedata.endlag

    #crouchingkick framedata
    p2crouchingkickstartup = shotocharacter.crouchingkickframedata.startup
    p2crouchingkickactive = shotocharacter.crouchingkickframedata.active
    p2crouchingkickendlag = shotocharacter.crouchingkickframedata.endlag

    #stun frames
    p2standingpunchstun = shotocharacter.stun.standingpunch
    p2crouchingpunchstun = shotocharacter.stun.crouchingpunch
    p2standingkickstun = shotocharacter.stun.standingkick
    p2crouchingkickstun = shotocharacter.stun.crouchingkick

    #damage
    p2standingpunchdamage = shotocharacter.damage.standingpunch
    p2crouchingpunchdamage = shotocharacter.damage.crouchingpunch
    p2standingkickdamage = shotocharacter.damage.standingkick
    p2crouchingkickdamage = shotocharacter.damage.crouchingkick

if p1char == "shoto":
    #hurtbox
    p1standingwidth = shotocharacter.hurtbox.standingwidth
    p1standingheight = shotocharacter.hurtbox.standingheight
    p1crouchingwidth = shotocharacter.hurtbox.crouchingwidth
    p1crouchingheight = shotocharacter.hurtbox.crouchingheight

    p1floor = shotocharacter.variables.floor
    p1crouchingfloor = shotocharacter.variables.crouchingfloor
    p1movementspeed = shotocharacter.variables.movementspeed
    p1jumpspeed = shotocharacter.variables.jumpspeed
    p1jumpheight = shotocharacter.variables.jumpheight

    #standing punch hitbox
    p1standingpunchwidth = shotocharacter.standingpuchhitbox.width
    p1standingpunchheight = shotocharacter.standingpuchhitbox.height
    p1standingpunchy = shotocharacter.standingpuchhitbox.y
    p1standingpunchx = shotocharacter.standingpuchhitbox.x
    p1standingpunchmovex = shotocharacter.standingpuchhitbox.movex
    p1standingpunchmovey = shotocharacter.standingpuchhitbox.movey

    #crouching punch hitbox
    p1crouchingpunchwidth = shotocharacter.crouchingpunchhitbox.width
    p1crouchingpunchheight = shotocharacter.crouchingpunchhitbox.height
    p1crouchingpunchy = shotocharacter.crouchingpunchhitbox.y
    p1crouchingpunchx = shotocharacter.crouchingpunchhitbox.x
    p1crouchingpunchmovex = shotocharacter.crouchingpunchhitbox.movex
    p1crouchingpunchmovey = shotocharacter.crouchingpunchhitbox.movey

    #standing kick hitbox
    p1standingkickwidth = shotocharacter.standingkickhitbox.width
    p1standingkickheight = shotocharacter.standingkickhitbox.height
    p1standingkicky = shotocharacter.standingkickhitbox.y
    p1standingkickx = shotocharacter.standingkickhitbox.x
    p1standingkickmovex = shotocharacter.standingkickhitbox.movex
    p1standingkickmovey = shotocharacter.standingkickhitbox.movey

    #crouch kick hitbox
    p1crouchingkickwidth = shotocharacter.crouchingkickhitbox.width
    p1crouchingkickheight = shotocharacter.crouchingkickhitbox.height
    p1crouchingkicky = shotocharacter.crouchingkickhitbox.y
    p1crouchingkickx = shotocharacter.crouchingkickhitbox.x
    p1crouchingkickmovex = shotocharacter.crouchingkickhitbox.movex
    p1crouchingkickmovey = shotocharacter.crouchingkickhitbox.movey

    #standingpunch knockback
    p1standingpunchknockbackxspeed = shotocharacter.standingpunchknockback.xspeed
    p1standingpunchknockbackxdestination = shotocharacter.standingpunchknockback.xdestination
    p1standingpunchknockbackyspeed = shotocharacter.standingpunchknockback.yspeed
    p1standingpunchknockbackydestination = shotocharacter.standingpunchknockback.ydestination

    #crouchingpunch knockback
    p1crouchingpunchknockbackxspeed = shotocharacter.crouchingpunchknockback.xspeed
    p1crouchingpunchknockbackxdestination = shotocharacter.crouchingpunchknockback.xdestination
    p1crouchingpunchknockbackyspeed = shotocharacter.crouchingpunchknockback.yspeed
    p1crouchingpunchknkockbackydestination = shotocharacter.crouchingpunchknockback.ydestination

    #standingkick knockback
    p1standingkickknockbackxspeed = shotocharacter.standingkickknockback.xspeed
    p1standingkickknockbackxdestination = shotocharacter.standingkickknockback.xdestination
    p1standingkickknockbackyspeed = shotocharacter.standingkickknockback.yspeed
    p1standingkickknockbackydestination = shotocharacter.standingkickknockback.ydestination

    #crouchingkick knockback
    p1crouchingkickknockbackxspeed = shotocharacter.crouchingkickknockback.xspeed
    p1crouchingkickknockbackxdestination = shotocharacter.crouchingkickknockback.xdestination
    p1crouchingkickknockbackyspeed = shotocharacter.crouchingkickknockback.yspeed
    p1crouchingkickknockbackydestination = shotocharacter.crouchingkickknockback.ydestination

    #standingpunch framedata
    p1standingpunchstartup = shotocharacter.standingpunchframedata.startup
    p1standingpunchactive = shotocharacter.standingpunchframedata.active
    p1standingpunchendlag = shotocharacter.standingpunchframedata.endlag

    #crouchingpunch framedata
    p1crouchingpunchstartup = shotocharacter.crouchingpunchframedata.startup
    p1crouchingpunchactive = shotocharacter.crouchingpunchframedata.active
    p1crouchingpunchendlag = shotocharacter.crouchingpunchframedata.endlag

    #standingkick framedata
    p1standingkickstartup = shotocharacter.standingkickframedata.startup
    p1standingkickactive = shotocharacter.standingkickframedata.active
    p1standingkickendlag = shotocharacter.standingkickframedata.endlag

    #crouchingkick framedata
    p1crouchingkickstartup = shotocharacter.crouchingkickframedata.startup
    p1crouchingkickactive = shotocharacter.crouchingkickframedata.active
    p1crouchingkickendlag = shotocharacter.crouchingkickframedata.endlag

    #stun frames
    p1standingpunchstun = shotocharacter.stun.standingpunch
    p1crouchingpunchstun = shotocharacter.stun.crouchingpunch
    p1standingkickstun = shotocharacter.stun.standingkick
    p1crouchingkickstun = shotocharacter.stun.crouchingkick

    #damage
    p1standingpunchdamage = shotocharacter.damage.standingpunch
    p1crouchingpunchdamage = shotocharacter.damage.crouchingpunch
    p1standingkickdamage = shotocharacter.damage.standingkick
    p1crouchingkickdamage = shotocharacter.damage.crouchingkick

if p1char == "sword":
    #hurtbox
    p1standingwidth = swordchar.hurtbox.standingwidth
    p1standingheight = swordchar.hurtbox.standingheight
    p1crouchingwidth = swordchar.hurtbox.crouchingwidth
    p1crouchingheight = swordchar.hurtbox.crouchingheight

    p1floor = swordchar.variables.floor
    p1crouchingfloor = swordchar.variables.crouchingfloor
    p1movementspeed = swordchar.variables.movementspeed
    p1jumpspeed = swordchar.variables.jumpspeed
    p1jumpheight = swordchar.variables.jumpheight

    #standing punch hitbox
    p1standingpunchwidth = swordchar.standingpuchhitbox.width
    p1standingpunchheight = swordchar.standingpuchhitbox.height
    p1standingpunchy = swordchar.standingpuchhitbox.y
    p1standingpunchx = swordchar.standingpuchhitbox.x
    p1standingpunchmovex = swordchar.standingpuchhitbox.movex
    p1standingpunchmovey = swordchar.standingpuchhitbox.movey

    #crouching punch hitbox
    p1crouchingpunchwidth = swordchar.crouchingpunchhitbox.width
    p1crouchingpunchheight = swordchar.crouchingpunchhitbox.height
    p1crouchingpunchy = swordchar.crouchingpunchhitbox.y
    p1crouchingpunchx = swordchar.crouchingpunchhitbox.x
    p1crouchingpunchmovex = swordchar.crouchingpunchhitbox.movex
    p1crouchingpunchmovey = swordchar.crouchingpunchhitbox.movey

    #standing kick hitbox
    p1standingkickwidth = swordchar.standingkickhitbox.width
    p1standingkickheight = swordchar.standingkickhitbox.height
    p1standingkicky = swordchar.standingkickhitbox.y
    p1standingkickx = swordchar.standingkickhitbox.x
    p1standingkickmovex = swordchar.standingkickhitbox.movex
    p1standingkickmovey = swordchar.standingkickhitbox.movey

    #crouch kick hitbox
    p1crouchingkickwidth = swordchar.crouchingkickhitbox.width
    p1crouchingkickheight = swordchar.crouchingkickhitbox.height
    p1crouchingkicky = swordchar.crouchingkickhitbox.y
    p1crouchingkickx = swordchar.crouchingkickhitbox.x
    p1crouchingkickmovex = swordchar.crouchingkickhitbox.movex
    p1crouchingkickmovey = swordchar.crouchingkickhitbox.movey

    #standingpunch knockback
    p1standingpunchknockbackxspeed = swordchar.standingpunchknockback.xspeed
    p1standingpunchknockbackxdestination = swordchar.standingpunchknockback.xdestination
    p1standingpunchknockbackyspeed = swordchar.standingpunchknockback.yspeed
    p1standingpunchknockbackydestination = swordchar.standingpunchknockback.ydestination

    #crouchingpunch knockback
    p1crouchingpunchknockbackxspeed = swordchar.crouchingpunchknockback.xspeed
    p1crouchingpunchknockbackxdestination = swordchar.crouchingpunchknockback.xdestination
    p1crouchingpunchknockbackyspeed = swordchar.crouchingpunchknockback.yspeed
    p1crouchingpunchknkockbackydestination = swordchar.crouchingpunchknockback.ydestination

    #standingkick knockback
    p1standingkickknockbackxspeed = swordchar.standingkickknockback.xspeed
    p1standingkickknockbackxdestination = swordchar.standingkickknockback.xdestination
    p1standingkickknockbackyspeed = swordchar.standingkickknockback.yspeed
    p1standingkickknockbackydestination = swordchar.standingkickknockback.ydestination

    #crouchingkick knockback
    p1crouchingkickknockbackxspeed = swordchar.crouchingkickknockback.xspeed
    p1crouchingkickknockbackxdestination = swordchar.crouchingkickknockback.xdestination
    p1crouchingkickknockbackyspeed = swordchar.crouchingkickknockback.yspeed
    p1crouchingkickknockbackydestination = swordchar.crouchingkickknockback.ydestination

    #standingpunch framedata
    p1standingpunchstartup = swordchar.standingpunchframedata.startup
    p1standingpunchactive = swordchar.standingpunchframedata.active
    p1standingpunchendlag = swordchar.standingpunchframedata.endlag

    #crouchingpunch framedata
    p1crouchingpunchstartup = swordchar.crouchingpunchframedata.startup
    p1crouchingpunchactive = swordchar.crouchingpunchframedata.active
    p1crouchingpunchendlag = swordchar.crouchingpunchframedata.endlag

    #standingkick framedata
    p1standingkickstartup = swordchar.standingkickframedata.startup
    p1standingkickactive = swordchar.standingkickframedata.active
    p1standingkickendlag = swordchar.standingkickframedata.endlag

    #crouchingkick framedata
    p1crouchingkickstartup = swordchar.crouchingkickframedata.startup
    p1crouchingkickactive = swordchar.crouchingkickframedata.active
    p1crouchingkickendlag = swordchar.crouchingkickframedata.endlag

    #stun frames
    p1standingpunchstun = swordchar.stun.standingpunch
    p1crouchingpunchstun = swordchar.stun.crouchingpunch
    p1standingkickstun = swordchar.stun.standingkick
    p1crouchingkickstun = swordchar.stun.crouchingkick

    #damage
    p1standingpunchdamage = swordchar.damage.standingpunch
    p1crouchingpunchdamage = swordchar.damage.crouchingpunch
    p1standingkickdamage = swordchar.damage.standingkick
    p1crouchingkickdamage = swordchar.damage.crouchingkick
#pygame setup
numofp1wins = 0
numofp2wins = 0


size = WIDTH, HEIGHT = 1920, 1080    
p1framecount = 0
p2framecount = 0

black = (0, 0, 0)
yellow = (255, 255, 0)
dimmedyellow = (100, 100, 0)
green = (0, 128, 0)
red = (255, 0, 0)
white = (255, 255, 255)
gray = (150, 150, 150)
blue = (0, 0, 255)
dimmedblue = (0, 0, 100)


p1healthbackgroundshadow = pygame.Rect((HEIGHT/ 54), 75, (100*8), 40)
p1healthbackground = pygame.Rect((HEIGHT/ 54)-5, 70, (100 * 8) + 20, 60)
p2healthbackground = pygame.Rect(((HEIGHT/ 54) * 55) - 15 , 70, (100 * 8) + 20, 60)
p2healthbackgroundshadow = pygame.Rect((HEIGHT/ 54) * 55, 75, 100 * 8, 40)

clock = pygame.time.Clock()
p1gothit = False
p2gothit = False
screen = pygame.display.set_mode(size)

fps = 60
newtimer = True

def resetvars():
    global p1counteredtextX, p2counteredtextX, p1gotcountered, p2gotcountered, p1parry, p2parry, tie, roundover, p1facing, p2facing, p1instun, p1standingpunchinstun, p1standingkickinstun, p1crouchingkickinstun, p1crouchingpunchinstun, player1death,roundstart, player2death, player1wins, player2wins, player1died, player2died, player2fallover, player1fallover, p1deathframecount, p2deathframecount
    player1died = False
    player2died = False

    player2fallover = False
    player1fallover = False

    p1deathframecount = 0
    p2deathframecount = 0

    player1death = False
    player2death = False

    player2wins = False
    player1wins = False
    tie = False

    roundstart = True
    roundover = False

    p1parry = False
    p2parry = False

    #1 for right 0 for left
    p1facing = 1
    p2facing = 0
    
    p1standingpunchinstun = False
    p1crouchingpunchinstun = False
    p1standingkickinstun = False
    p1crouchingkickinstun = False
    player1.instun = False
    player2.instun = False

    p1gotcountered = False
    p2gotcountered = False

    p2counteredtextX = 0
    p1counteredtextX = WIDTH

    camera.yoffset = 0 
    
    timer.timer.setupcountdown(3)
resetvars()
#timer setup
timer.timer.setup()




#character setup
player1.p1.setup(p1standingwidth, p1standingheight, p1crouchingwidth, p1crouchingheight)
player2.p2.setup(p2standingwidth, p2standingheight, p2crouchingwidth, p2crouchingheight)
p2health = 100
p1moveright = False
p1moveleft = False
p1crouch = False
p2crouch = False
p2moveright = False
p2moveleft = False
p1atedge = False
p2atedge = False
p1jump = False
p2jump = False
epunch = False
upunch = False
p1inmove = False
p2inmove = False
epunchinendlag = False
upunchinendlag = False
qkickinendlag = False
okickinendlag = False
qkick = False
okick = False

epunchknockback = False
qkickknockback = False
upunchknockback = False
okickknockback = False

#mouse
mouse = pygame.Rect(50, 50, 50, 50)

#buttons
playagainbutton = pygame.Rect(WIDTH/2, 500, 1000, 250)
playagainbutton.center = WIDTH/2, 500
pressedplayagain = 0

#facing eachother (1 for right 0 for left)
def facing():
    global p1facing, p2facing
    if player1.p1x > player2.p2x:
        p1facing = 0
        p2facing = 1
    if player2.p2x > player1.p1x:
        p1facing = 1
        p2facing = 0


#endlag

def epunchendlag(endlagframes):
    global p1framecount, p1inmove, epunch, epunchinendlag
    p1framecount = p1framecount + 1
    if p1framecount >= endlagframes:
        epunch = False
        p1inmove = False
        epunchinendlag = False
        p1framecount = 0

def qkickendlag(endlagframes):
    global p1framecount, p1inmove, qkick, qkickinendlag
    p1framecount = p1framecount + 1
    if p1framecount >= endlagframes:
        qkick = False
        p1inmove = False
        qkickinendlag = False
        p1framecount = 0

def upunchendlag(endlagframes):
    global p2framecount, p2inmove, upunch, upunchinendlag
    p2framecount = p2framecount + 1
    if p2framecount >= endlagframes:
        upunch = False
        p2inmove = False
        upunchinendlag = False
        p2framecount = 0

def okickendlag(endlagframes):
    global p2framecount, p2inmove, okick, okickinendlag
    p2framecount = p2framecount + 1
    if p2framecount >= endlagframes:
        okick = False
        p2inmove = False
        okickinendlag = False
        p2framecount = 0

#frame data active frames

def epunchactive(activeframes):
    global p1framecount, p1gothit, epunchinendlag
    p1framecount = p1framecount + 1
    if p1framecount >= activeframes:
        player1.epunchout = False
        p1framecount = 0
        p1gothit = False
        epunchinendlag = True

def qkickactive(activeframes):
    global p1framecount, p1gothit, qkickinendlag, p1facing
    p1framecount = p1framecount + 1
    if player1.crouch == False:
        if p1facing == 1:
            player1.p1.move(5, p1movementspeed, p1floor, p1crouchingfloor)
        if p1facing == 0: 
            player1.p1.move(-5, p1movementspeed, p1floor, p1crouchingfloor)
    if p1framecount >= activeframes:
        player1.qkickout = False
        p1framecount = 0 
        p1gothit = False
        qkickinendlag = True

def upunchactive(activeframes):
    global p2framecount, p2gothit, upunchinendlag
    p2framecount = p2framecount + 1
    if p2framecount >= activeframes:
        player2.upunchout = False
        p2framecount = 0
        p2gothit = False
        upunchinendlag = True

def okickactive(activeframes):
    global p2framecount, p2gothit, okickinendlag, p2facing
    p2framecount = p2framecount + 1
    if player2.crouch == False:
        if p2facing == 1:
            player2.p2.move(5, p2movementspeed, p2floor, p2crouchingfloor)
        if p2facing == 0:
            player2.p2.move(-5, p2movementspeed, p2floor, p2crouchingfloor)
    if p2framecount >= activeframes:
        player2.okickout = False
        p2framecount = 0
        p2gothit = False
        okickinendlag = True

#startup

def epunchstartup(startupframes):
    global p1framecount, epunch, p1inmove, p1facing
    p1framecount = p1framecount + 1
    if p1framecount >= startupframes:
        player1.p1.epunch(p1facing, p1standingpunchwidth, p1standingpunchheight, p1standingpunchx, p1standingpunchy, p1crouchingpunchwidth, p1crouchingpunchheight, p1crouchingpunchx, p1crouchingpunchy, p1standingpunchmovex, p1standingpunchmovey, p1crouchingpunchmovex, p1crouchingpunchmovex)
        p1framecount = 0
        epunch = False

def qkickstartup(startupframes):
    global p1framecount, qkick, p1inmove, p1facing
    p1framecount = p1framecount + 1
    if p1framecount >= startupframes:
        player1.p1.qkick(p1facing, p1standingkickwidth, p1standingkickheight, p1standingkickx, p1standingkicky, p1crouchingkickwidth, p1crouchingkickheight, p1crouchingkickx, p1crouchingkicky)
        p1framecount = 0
        qkick = False

def upunchstartup(startupframes):
    global p2framecount, upunch, p2inmove, p2facing
    p2framecount = p2framecount + 1
    if p2framecount >= startupframes:
        player2.p2.upunch(p2facing, p2standingpunchwidth, p2standingpunchheight, p2standingpunchy, p2standingpunchx, p2crouchingpunchwidth, p2crouchingpunchheight, p2crouchingpunchx, p2crouchingpunchy)
        p2framecount = 0
        upunch = False

def okickstartup(startupframes):
    global p2framecount, okick, p2inmove, p2facing
    p2framecount = p2framecount + 1
    if p2framecount >= startupframes:
        player2.p2.okick(p2facing, p2standingkickwidth, p2standingkickheight, p2standingkicky, p2standingkickx, p2crouchingkickwidth, p2crouchingkickheight, p2crouchingkickx, p2crouchingkicky)
        p2framecount = 0
        okick = False


#pushing and bounding arena
def p1stayin():
    global p1atedge
    p1stayinleftx = player1.p1x - p1standingwidth / 2
    p1stayinrightx = player1.p1x + p1standingwidth / 2
    if p1stayinleftx <= 10:
        player1.p1.stayin((10 - p1stayinleftx) + 10)
        p1atedge = True
    if p1stayinrightx >= WIDTH - 10:
        player1.p1.stayin((WIDTH-p1stayinrightx)- 10)
        p1atedge = True
    elif p1stayinleftx >= 30 and p1stayinrightx <= WIDTH - 30:
        p1atedge = False


def p2stayin():
    global p2atedge
    p2stayinleftx = player2.p2x - p2standingwidth / 2
    p2stayinrightx = player2.p2x + p2standingwidth / 2
    if p2stayinleftx <= 10:
        player2.p2.stayin((10 - p2stayinleftx) + 10)
        p2atedge = True
    if p2stayinrightx >= WIDTH - 10:
        player2.p2.stayin((WIDTH - p2stayinrightx) - 10)
        p2atedge = True
    elif p2stayinleftx >= 30 and p2stayinrightx <= WIDTH - 30:
        p2atedge = False



def p1pushing():
    global p1moveright, p1moveleft, p2atedge, p2moveright, p2moveleft, p1facing
    if p1facing == 1:
        if player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p2atedge == True:
            player1.p1.move(-10, p1movementspeed, p1floor, p1crouchingfloor)
        elif player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p1moveright == True:
            player2.p2.move(10, p1movementspeed, p2floor, p2crouchingfloor)
    if p1facing == 0:
        if player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p2atedge == True:
            player1.p1.move(10, p1movementspeed, p1floor, p1crouchingfloor)
        elif player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p1moveleft == True:
            player2.p2.move(-10, p1movementspeed, p2floor, p2crouchingfloor)
        
    

def p2pushing():
    global p2moveleft, p2moveright, p1moveleft, p1moveright, p1atedge, p2facing
    if p2facing == 1:
        if player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p1atedge == True:
            player2.p2.move(-10, p2movementspeed, p2floor, p2crouchingfloor)
        elif player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p2moveright == True:
            player1.p1.move(10, p2movementspeed, p1floor, p1crouchingfloor)
    if p2facing == 0:
        if player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p1atedge == True:
            player2.p2.move(10,p2movementspeed, p2floor, p2crouchingfloor)
        elif player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p2moveleft == True:
            player1.p1.move(-10, p2movementspeed, p1floor, p1crouchingfloor)


#knockback
def p1knockbackleft(xspeed, xdestination, yspeed, ydestination):
    player1.p1.yvelocity(yspeed, ydestination)
    player1.p1.xvelocityleft(xspeed, xdestination)

def p1knockbackright(xspeed, xdestination, yspeed, ydestination):
    player1.p1.yvelocity(yspeed, ydestination)
    player1.p1.xvelocityright(xspeed, xdestination)

def p2knockbackleft(xspeed, xdestination, yspeed, ydestination):
    player2.p2.yvelocity(yspeed, ydestination)
    player2.p2.xvelocityleft(xspeed, xdestination)

def p2knockbackright(xspeed, xdestination, yspeed, ydestination):
    player2.p2.yvelocity(yspeed, ydestination)
    player2.p2.xvelocityright(xspeed, xdestination)

#stun
def p1stun(stunframes):
    global p1framecount, p1inmove
    p1framecount = p1framecount + 1
    if p1framecount >= stunframes:
        p1inmove = False
        p1framecount = 0
        player1.instun = False

def p2stun(stunframes):
    global p2framecount, p2inmove
    p2framecount = p2framecount + 1 
    if p2framecount >= stunframes:
        p2inmove = False
        p2framecount = 0
        player2.instun = False

#attack interupted
def p1interupted():
    global p1inmove, p1gotcountered
    player1.epunchout = False
    player1.qkickout = False
    p1gotcountered = True
    #p2inmove = False
    

def p2interupted():
    global p2inmove, p2gotcountered
    player2.upunchout == False
    player2.okickout == False
    p2gotcountered = True
    #p2inmove = False

#hitboxes and hitdetection
#p1 got hit means player 2 got hit
#p2 got hit means player 1 got hit

def epunchhitbox():
    global p1gothit, epunchknockback, p2standingpunchinstun, p2crouchingpunchinstun, p2framecount
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            if p2inmove == True:
                p2interupted()
            if player2.noknockback == False:
                player2.instun = True
            p2framecount = 0
            if player2.noknockback == False:
                epunchknockback = True
            if player1.crouch == False:
                player2.p2.takedamage(p1standingpunchdamage)
                if player2.noknockback == False:
                    p2standingpunchinstun = True
            if player1.crouch == True:
                player2.p2.takedamage(p1crouchingpunchdamage)
                if player2.noknockback == False:
                    p2crouchingpunchinstun = True
            p1gothit = True

def qkickhitbox():
    global p1gothit, qkickknockback, p2framecount, p2standingkickinstun, p2crouchingkickinstun
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            if p2inmove == True:
                p2interupted()
            if player2.noknockback == False:
                player2.instun = True
            p2framecount = 0
            if player2.noknockback == False:
                qkickknockback = True
            if player1.crouch == False:
                player2.p2.takedamage(p1standingkickdamage)
                if player2.noknockback == False:
                    p2standingkickinstun = True
            if player1.crouch == True:
                player2.p2.takedamage(p1crouchingkickdamage)
                if player2.noknockback == False:
                    p2crouchingkickinstun = True
            p1gothit = True

def upunchhitbox():
    global p2gothit, upunchknockback, p1standingpunchinstun, p1crouchingpunchinstun, p1framecount
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            if p1inmove == True:
                p1interupted()
            if player1.noknockback == False:
                player1.instun = True
            p1framecount = 0
            if player1.noknockback == False:
                upunchknockback = True
            if player2.crouch == False:
                player1.p1.takedamage(p2standingpunchdamage)
                if player1.noknockback == False:
                    p1standingpunchinstun = True
            if player2.crouch == True:
                player1.p1.takedamage(p2crouchingpunchdamage)
                if player1.noknockback == False:
                    p1crouchingpunchinstun = True
            p2gothit = True

def okickhitbox():
    global p2gothit, okickknockback, p1standingkickinstun, p1crouchingkickinstun, p1framecount
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            if p1inmove == True:
                p1interupted()
            if player1.noknockback == False:
                player1.instun = True
            p1framecount = 0
            if player1.noknockback == False:
                okickknockback = True
            if player2.crouch == False:
                player1.p1.takedamage(p2standingkickdamage)
                if player1.noknockback == False:
                    p1standingkickinstun = True
            if player2.crouch == True:
                player1.p1.takedamage(p2crouchingkickdamage)
                if player1.noknockback == False:
                    p1crouchingkickinstun = True
            p2gothit = True

#camerasetup
camera.cameraypositionpassive(player1.p1y, player2.p2y, p1floor, p2floor)
#main pygame loop 
pygame.init()

def set_text(string, coordx, coordy, fontSize, color):
    font = pygame.font. Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, color)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

while True:
    screen.fill(black)
    pygame.display.set_caption("fps : " + str(fps))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == KEYDOWN:
            #close if esc is pressed
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            
            #player 1 movement and moves
            if event.key == pygame.K_d:
                p1moveright = True
                if p1facing == 0:
                    if p1inmove == False and player1.instun == False:
                        player1.p1.blocking()
            if event.key == pygame.K_a:
                p1moveleft = True
                if p1facing == 1:
                    if p1inmove == False and player1.instun == False:
                        player1.p1.blocking()
            if event.key == pygame.K_s:
                if player1.onground == True:
                    p1crouch = True
            if event.key == pygame.K_w:
                if player1.instun == False:
                    p1jump = True
            if p1inmove == False:
                if event.key == pygame.K_e:
                    epunch = True
                if event.key == pygame.K_q:
                    qkick = True

           
            #player 2 movement and moves
            if event.key == pygame.K_l:
                p2moveright = True
                if p2facing == 0:
                    if p2inmove == False and player2.instun == False:
                        player2.p2.blocking()
            if event.key == pygame.K_j:
                p2moveleft = True
                if p2facing == 1:
                    if p2inmove == False and player2.instun == False:
                        player2.p2.blocking()
            if event.key == pygame.K_k:
                if player2.onground == True:
                    p2crouch = True
            if event.key == pygame.K_i:
                if player2.instun == False:
                    p2jump = True
            if p2inmove == False:
                if event.key == pygame.K_u:
                    upunch = True
                if event.key == pygame.K_o:
                    okick = True
            
        elif event.type == KEYUP:
            if event.key == pygame.K_d:
                p1moveright = False
                if p1facing == 0:
                    player1.p1.unblocking()
            if event.key == pygame.K_a:
                p1moveleft = False
                if p1facing == 1:
                    player1.p1.unblocking()
            if event.key == pygame.K_s:
                p1crouch = False
            if event.key == pygame.K_l:
                p2moveright = False
                if p2facing == 0:
                    player2.p2.unblocking()
            if event.key == pygame.K_j:
                p2moveleft = False
                if p2facing == 1:
                    player2.p2.unblocking()
            if event.key == pygame.K_k:
                p2crouch = False
            if event.key == pygame.K_w:
                p1jump = False
                player1.onground = False
            if event.key == pygame.K_i:
                p2jump = False
                player2.onground = False
    
    #player 1 move and crouch
    if p1inmove == False:
        if p1moveleft == False:
            if p1moveright == True:
                if p1facing == 1:
                    player1.p1.move(10, p1movementspeed, p1floor, p1crouchingfloor)
                if p1facing == 0:
                    player1.p1.move(5, p1movementspeed, p1floor, p1crouchingfloor)

        if p1moveright == False:
            if p1moveleft == True:
                if p1facing == 0:
                    player1.p1.move(-10, p1movementspeed, p1floor, p1crouchingfloor)
                if p1facing == 1:
                    player1.p1.move(-5, p1movementspeed, p1floor, p1crouchingfloor)

        if p1crouch == True:
            player1.p1.crouch(p1crouchingfloor)
        if p1jump == True:
            player1.p1.jump(p1jumpspeed, p1jumpheight)
        #player 1 uncrouch
        if p1crouch == False:
            player1.p1.uncrouch()
    if player1.instun == False:
        if epunch == True:
            p1inmove = True
            if p1crouch == False:
                epunchstartup(p1standingpunchstartup)
            if p1crouch == True:
                epunchstartup(p1crouchingpunchstartup)
        if qkick == True:
            p1inmove = True
            if p1crouch == False:
                qkickstartup(p1standingkickstartup)
            if p1crouch == True:
                qkickstartup(p1crouchingkickstartup)

    if p2inmove == False:
        #player 2 move and crouch
        if p2moveleft == False:
            if p2moveright == True:
                if p2facing == 1:
                    player2.p2.move(10, p2movementspeed, p2floor, p2crouchingfloor)
                if p2facing == 0:
                    player2.p2.move(5, p2movementspeed, p2floor, p2crouchingfloor)

        if p2moveright == False:
            if p2moveleft == True:
                if p2facing == 1:
                    player2.p2.move(-5, p2movementspeed, p2floor, p2crouchingfloor)
                if p2facing == 0:
                    player2.p2.move(-10, p2movementspeed, p2floor, p2crouchingfloor)

        if p2crouch == True:
            player2.p2.crouch(p2crouchingfloor)
        if p2jump == True:
            player2.p2.jump(p2jumpspeed, p2jumpheight)
        #player 2 uncrouch
        if p2crouch == False:
            player2.p2.uncrouch()
    if player2.instun == False:
        if upunch == True:
            p2inmove = True
            if p2crouch == False:
                upunchstartup(p2standingpunchstartup)
            if p2crouch == True:
                upunchstartup(p2crouchingpunchstartup)
        if okick == True:
            p2inmove = True
            if p2crouch == False:
                okickstartup(p2standingkickstartup)
            if p2crouch == True:
                okickstartup(p2crouchingkickstartup)


    #roundstart/ countdown
    if roundstart == True:
        timer.timer.countdown(3)
        countdowntext = set_text(str(timer.countdowntime), WIDTH/2, HEIGHT/2, 100, white)
        screen.blit(countdowntext[0], countdowntext[1])
        p1inmove = True
        p2inmove = True
        if timer.counted == True:
            roundstart = False
            timer.counted = False
            p1inmove = False
            p2inmove = False
            timer.timer.setupcountdown(100)
    
    if timer.go == True and timer.time <= 1 and roundover == False:
        gotext = set_text("FIGHT!!", WIDTH/2, HEIGHT/2, 500, white)
        screen.blit(gotext[0], gotext[1])



    #pushing and bouding and gravity
    player1.p1.gravity(p1floor)
    player2.p2.gravity(p2floor)
    facing()
    p1stayin()
    p2stayin()
    p1pushing()
    p2pushing()

    #epunch
    if epunchinendlag and p1crouch == True:
        epunchendlag(p1crouchingpunchendlag)
    elif epunchinendlag == True:
        epunchendlag(p1standingpunchendlag)
    if player1.epunchout == True and p1crouch == False:
        epunchhitbox()
        epunchactive(p1standingpunchactive)
    elif player1.epunchout == True:
        epunchhitbox()
        epunchactive(p1crouchingpunchactive)

    #qkick
    if qkickinendlag and p1crouch == True:
        qkickendlag(p1crouchingkickendlag)
    elif qkickinendlag == True:
        qkickendlag(p1standingkickendlag)
    if player1.qkickout == True and p1crouch == False:
        qkickhitbox()
        qkickactive(p1standingkickactive)
    elif player1.qkickout == True:
        qkickhitbox()
        qkickactive(p1crouchingkickactive)

    #upunch
    if upunchinendlag and p2crouch == True:
        upunchendlag(p2crouchingpunchendlag)
    elif upunchinendlag == True:
        upunchendlag(p2standingpunchendlag)
    if player2.upunchout == True and p2crouch == True:
        upunchhitbox()
        upunchactive(p2crouchingpunchactive)
    elif player2.upunchout == True:
        upunchhitbox()
        upunchactive(p2standingpunchactive)

    #okick
    if okickinendlag and p2crouch == True:
        okickendlag(p2crouchingkickendlag)
    elif okickinendlag == True:
        okickendlag(p2standingkickendlag)
    if player2.okickout == True and p2crouch == True:
        okickhitbox()
        okickactive(p2crouchingkickactive)
    elif player2.okickout == True:
        okickhitbox()
        okickactive(p2standingkickactive)

        #win condidtion
    if player1.p1health <= 0:
        player2wins = True
        player1.death = True


    if player2.p2health <= 0:
        player1wins = True
        player2.death = True

    if player2fallover == True:
        player2.p2.fallover_death(p2standingwidth, p2standingheight)
        player2.instun = True

    if player1fallover == True:
        player1.p1.fallover_death(p1standingwidth, p1standingheight)
        player1.instun = True

    #knockback
    if player2.xvelocityend and player2.yvelocityend == True:
        player2.knockbacked = True
        player2.xvelocityend = False
        player2.yvelocityend = False

    if player1.xvelocityend and player1.yvelocityend == True:
        player1.knockbacked = True
        player1.xvelocityend = False
        player1.yvelocityend = False

    if player2.noknockback == False:
        if epunchknockback == True:
            if player1.crouch == False:
                if p1facing == 1:
                    p2knockbackright(p1standingpunchknockbackxspeed, p1standingpunchknockbackxdestination, p1standingpunchknockbackyspeed, p1standingpunchknockbackydestination)
                elif p1facing == 0:
                    p2knockbackleft(p1standingpunchknockbackxspeed, -(p1standingpunchknockbackxdestination), p1standingpunchknockbackyspeed, p1standingpunchknockbackydestination)
                if player2.knockbacked == True:
                    epunchknockback = False
                    player2.knockbacked = False
            if player1.crouch == True:
                if p1facing == 1:
                    p2knockbackright(p1crouchingpunchknockbackxspeed, p1crouchingpunchknockbackxdestination, p1crouchingpunchknockbackyspeed, p1crouchingpunchknkockbackydestination)
                elif p1facing == 0:
                    p2knockbackleft(p1crouchingpunchknockbackxspeed, -(p1crouchingpunchknockbackxdestination), p1crouchingpunchknockbackyspeed, p1crouchingpunchknkockbackydestination)
                if player2.knockbacked == True:
                    epunchknockback = False
                    player2.knockbacked = False

        if qkickknockback == True:
            if player1.crouch == False:
                if p1facing == 1:
                    p2knockbackright(p1standingkickknockbackxspeed, p1standingkickknockbackxdestination, p1standingkickknockbackyspeed, p1standingkickknockbackydestination)
                elif p1facing == 0:
                    p2knockbackleft(p1standingkickknockbackxspeed, -(p1standingkickknockbackxdestination), p1standingkickknockbackyspeed, p1standingkickknockbackydestination)
                if player2.knockbacked == True:
                    qkickknockback = False
                    player2.knockbacked = False
            if player1.crouch == True:
                if p1facing == 1:
                    p2knockbackright(p1crouchingkickknockbackxspeed, p1crouchingkickknockbackxdestination, p1crouchingkickknockbackyspeed, p1crouchingpunchknkockbackydestination)
                elif p1facing == 0:
                    p2knockbackleft(p1crouchingkickknockbackxspeed, -(p1crouchingkickknockbackxdestination), p1crouchingkickknockbackyspeed, p1crouchingpunchknkockbackydestination)
                if player2.knockbacked == True:
                    qkickknockback = False
                    player2.knockbacked = False


    if player1.noknockback == False:
        if upunchknockback == True:
            if player2.crouch == False:
                if p2facing == 1:
                    p1knockbackright(p2standingpunchknockbackxspeed, p2standingpunchknockbackxdestination, p2standingpunchknockbackyspeed, p2standingpunchknockbackydestination)
                elif p2facing == 0:
                    p1knockbackleft(p2standingpunchknockbackxspeed, -(p2standingpunchknockbackxdestination), p2standingpunchknockbackyspeed, p2standingpunchknockbackydestination)
                if player1.knockbacked == True:
                    upunchknockback = False
                    player1.knockbacked = False
            if player2.crouch == True:
                if p2facing == 1:
                    p1knockbackright(p2crouchingpunchknockbackxspeed, p2crouchingpunchknockbackxdestination, p2crouchingpunchknockbackyspeed, p2crouchingpunchknkockbackydestination)
                elif p2facing == 0:
                    p1knockbackleft(p2crouchingpunchknockbackxspeed, -(p2crouchingpunchknockbackxdestination), p2crouchingpunchknockbackyspeed, p2crouchingpunchknkockbackydestination)
                if player1.knockbacked == True:
                    upunchknockback = False
                    player1.knockbacked = False
    
        if okickknockback == True:
            if player2.crouch == False:
                if p2facing == 1:
                    p1knockbackright(p2standingkickknockbackxspeed, p2standingkickknockbackxdestination, p2standingkickknockbackyspeed, p2standingkickknockbackydestination)
                elif p2facing == 0:
                    p1knockbackleft(p2standingkickknockbackxspeed, -(p2standingkickknockbackxdestination), p2standingkickknockbackyspeed, p2standingkickknockbackydestination)
                if player1.knockbacked == True:
                    okickknockback = False
                    player1.knockbacked = False
            if player2.crouch == True:
                if p2facing == 1:
                    p1knockbackright(p2crouchingkickknockbackxspeed, p2crouchingkickknockbackxdestination, p2crouchingkickknockbackyspeed, p2crouchingpunchknkockbackydestination)
                if p2facing == 0:
                    p1knockbackleft(p2crouchingkickknockbackxspeed, -(p2crouchingkickknockbackxdestination), p2crouchingkickknockbackyspeed, p2crouchingpunchknkockbackydestination)
                if player1.knockbacked == True:
                    okickknockback = False
                    player1.knockbacked = False

    #stun
    if player1.instun == True:
        if p1standingpunchinstun == True and p1gotcountered == True:
            p1stun(p2standingpunchstun * 2)
        elif p1standingpunchinstun == True:
            p1stun(p2standingpunchstun)

        if p1crouchingpunchinstun == True and p1gotcountered == True:
            p1stun(p2crouchingpunchstun * 2)
        elif p1crouchingpunchinstun == True:
            p1stun(p2crouchingpunchstun)
    
        if p1standingkickinstun == True and p1gotcountered == True:
            p1stun(p2standingkickstun * 2)
        elif p1standingkickinstun == True:
            p1stun(p2standingkickstun)
    
        if p1crouchingkickinstun == True and p1gotcountered == True:
            p1stun(p2crouchingkickstun * 2)
        elif p1crouchingkickinstun == True:
            p1stun(p2crouchingkickstun)

    elif player1.instun == False:
        p1standingkickinstun = False
        p1standingpunchinstun = False
        p1crouchingpunchinstun = False
        p1crouchingkickinstun = False

    if player2.instun == True:
        if p2standingpunchinstun == True and p2gotcountered == True:
            p2stun(p1standingpunchstun * 2)
        elif p2standingpunchinstun == True:
            p2stun(p1standingpunchstun)

        if p2crouchingpunchinstun == True and p2gotcountered == True:
            p2stun(p1crouchingpunchstun * 2)
        elif p2crouchingpunchinstun == True:
            p2stun(p1crouchingpunchstun)
    
        if p2standingkickinstun == True and p2gotcountered == True:
            p2stun(p1standingkickstun * 2)
        elif p2standingkickinstun == True:
            p2stun(p1standingkickstun)
    
        if p2crouchingkickinstun == True and p2gotcountered == True:
            p2stun(p1crouchingkickstun * 2)
        elif p2crouchingkickinstun == True:
            p2stun(p1crouchingkickstun)

    elif player2.instun == False:
        p2standingkickinstun = False
        p2standingpunchinstun = False
        p2crouchingpunchinstun = False
        p2crouchingkickinstun = False

    #death
    if player2wins == True and player1died == False:
        fps = 10
        player1died = True

    if player1wins == True and player2died == False:
        fps = 10
        player2died = True

    if player1died == True:
        p1deathframecount = p1deathframecount + 1
        if p1deathframecount >= 5:
            player1fallover = True
        if p1deathframecount >= 10:
            p1deathframecount = 0
            fps = 60
            player1died = True

    if player2died == True:
        p2deathframecount = p2deathframecount + 1
        if p2deathframecount >= 5:
            player2fallover = True
        if p2deathframecount >= 10:
            p2deathframecount = 0
            fps = 60
            player2died = True

    #timer
    if roundover == False and roundstart == False:
        timer.timer.countdown(100)
        timertext = set_text(str(timer.countdowntime), WIDTH/2, 125, 100, white)
        screen.blit(timertext[0], timertext[1])
        
    #timeout / draw
    if timer.counted == True:
        tie = True
        timer.counted = False

    if tie == True:
        tietext = set_text("DRAW", 950, 250, 200, white)
        screen.blit(tietext[0], tietext[1])
        roundover = True
        
    #player wins
    if player1wins == True:
        player1winstext = set_text("PLAYER 1 WINS", 950, 250, 200, white)
        screen.blit(player1winstext[0], player1winstext[1])
        roundover = True

    if player2wins == True:
        player2winstext = set_text("PLAYER 2 WINS", 950, 250, 200, white)
        screen.blit(player2winstext[0], player2winstext[1])
        roundover = True
        
    #round over
    if roundover and newtimer == True:
        timer.time = 0
        newtimer = False

    if roundover == True:
        timer.timer.count(5)
        if timer.counted == True:
            if player1wins == True:
                numofp1wins = numofp1wins + 1
            if player2wins == True:
                numofp2wins = numofp2wins + 1
            resetvars()
            timer.timer.setup()
            player1.p1.setup(p1standingwidth, p1standingheight, p1crouchingwidth, p1crouchingheight)
            player2.p2.setup(p2standingwidth, p2standingheight, p2crouchingwidth, p2crouchingheight)
            fps = 60 
            p1inmove = False
            p2inmove = False
            newtimer = True

    #camera
    camera.cameraypositionpassive(player1.p1y, player2.p2y, p1floor, p2floor)

    #drawing
    if p1gotcountered == True:
        p1countertext = set_text("COUNTER", p1counteredtextX, HEIGHT / 4, 100, white)
        screen.blit(p1countertext[0], p1countertext[1])
        p1counteredtextX = p1counteredtextX - 20
        if p1counteredtextX <= (WIDTH/2) + 350:
            p1counteredtextX = WIDTH
            p1gotcountered = False

    if p2gotcountered == True:
        p2countertext = set_text("COUNTER", p2counteredtextX, HEIGHT / 4, 100, white)
        screen.blit(p2countertext[0], p2countertext[1])
        p2counteredtextX = p2counteredtextX + 20
        if p2counteredtextX >= (WIDTH/2) - 350:
            p2gotcountered = False
            p2counteredtextX = 0


    pygame.draw.rect(screen, white, p1healthbackground, 0)
    pygame.draw.rect(screen, gray, p1healthbackgroundshadow, 0)
    pygame.draw.rect(screen, red, pygame.Rect((HEIGHT/ 54), 75, player1.p1health * 8, 40), 0)
    pygame.draw.rect(screen, white, p2healthbackground, 0)
    pygame.draw.rect(screen, gray, p2healthbackgroundshadow, 0)
    pygame.draw.rect(screen, red, pygame.Rect(((HEIGHT/54) * 55) + ((100 * 8) - player2.p2health * 8), 75, player2.p2health * 8, 40), 0)
    pygame.draw.circle(screen, white, (75, 125), 30, 0)
    pygame.draw.circle(screen, white, (150, 125), 30, 0)
    pygame.draw.circle(screen, white, (1845, 125), 30, 0)
    pygame.draw.circle(screen, white, (1770, 125), 30, 0)

    if p1inmove == False and player1.instun == False:
        pygame.draw.rect(screen, yellow, (player1.p1hurtbox.x,player1.p1hurtbox.y + camera.yoffset, player1.p1hurtbox.width, player1.p1hurtbox.height), 2)
    elif p1inmove == True or player1.instun == True:
        pygame.draw.rect(screen, dimmedyellow, (player1.p1hurtbox.x,player1.p1hurtbox.y + camera.yoffset, player1.p1hurtbox.width, player1.p1hurtbox.height), 2)
    
    if p2inmove == False and player2.instun == False:
        pygame.draw.rect(screen, blue, (player2.p2hurtbox.x, player2.p2hurtbox.y + camera.yoffset, player2.p2hurtbox.width, player2.p2hurtbox.height), 2)
    elif p2inmove == True or player2.instun == True:
        pygame.draw.rect(screen, dimmedblue, (player2.p2hurtbox.x, player2.p2hurtbox.y + camera.yoffset, player2.p2hurtbox.width, player2.p2hurtbox.height), 2)
    
    if numofp1wins >=1:
        pygame.draw.circle(screen, yellow, (75,125), 25, 0)
    if numofp1wins >= 2:
        pygame.draw.circle(screen, yellow, (150, 125), 25, 0)

    if numofp2wins >= 1:
        pygame.draw.circle(screen, blue, (1845, 125), 25, 0)
    if numofp2wins >= 2:
        pygame.draw.circle(screen, blue, (1770, 125), 25, 0)
   
    if numofp1wins >= 2 or numofp2wins >= 2:
        screen.fill(black)
        if numofp1wins >= 2:
            screen.blit(player1winstext[0], player1winstext[1])
        if numofp2wins >= 2:
            screen.blit(player2winstext[0], player2winstext[1])
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
            mouse.center = event.pos

        pressingplayagain = mouse.colliderect(playagainbutton)

        if pressingplayagain == True and pressedplayagain < 1000:
            pressedplayagain = pressedplayagain + 10
        if pressingplayagain == False and pressedplayagain > 0:
            pressedplayagain = pressedplayagain - 10

        playagainfill = pygame.Rect((WIDTH/ 2) - 500, 500, pressedplayagain, 250)
        playagainfill.centery = 500

        pygame.draw.rect(screen, gray, playagainfill, 0)
        pygame.draw.rect(screen, white, mouse, 2)
        pygame.draw.rect(screen, white, playagainbutton, 2)
        infotext = set_text("play again", WIDTH/2, 500, 200, white)
        screen.blit(infotext[0], infotext[1])

    

        #play again
    if pressedplayagain >= 1000:
        resetvars()
        timer.timer.setup()
        player1.p1.setup(p1standingwidth, p1standingheight, p1crouchingwidth, p1crouchingheight)
        player2.p2.setup(p2standingwidth, p2standingheight, p2crouchingwidth, p2crouchingheight)
        fps = 60
        p1inmove = False
        p2inmove = False
        numofp1wins = 0
        numofp2wins = 0
        pressedplayagain = 0
        p1gothit = False
        p2gothit = False
        newtimer = True
        
    pygame.display.flip()
     

    clock.tick(fps)
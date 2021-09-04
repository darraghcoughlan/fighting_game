
from pygame.constants import FULLSCREEN, KEYDOWN, KEYUP, KSCAN_ESCAPE, K_ESCAPE

import time, pygame, time, sys
import player1
import player2
import timer
import shotocharacter

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

    #crouching punch hitbox
    p2crouchingpunchwidth = shotocharacter.crouchingpunchhitbox.width
    p2crouchingpunchheight = shotocharacter.crouchingpunchhitbox.height
    p2crouchingpunchy = shotocharacter.crouchingpunchhitbox.y
    p2crouchingpunchx = shotocharacter.crouchingpunchhitbox.x

    #standing kick hitbox
    p2standingkickwidth = shotocharacter.standingkickhitbox.width
    p2standingkickheight = shotocharacter.standingkickhitbox.height
    p2standingkicky = shotocharacter.standingkickhitbox.y
    p2standingkickx = shotocharacter.standingkickhitbox.x

    #crouch kick hitbox
    p2crouchingkickwidth = shotocharacter.crouchingkickhitbox.width
    p2crouchingkickheight = shotocharacter.crouchingkickhitbox.height
    p2crouchingkicky = shotocharacter.crouchingkickhitbox.y
    p2crouchingkickx = shotocharacter.crouchingkickhitbox.x

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


p1healthbackgroundshadow = pygame.Rect((HEIGHT/ 54), 20, (100*9), 40)
p1healthbackground = pygame.Rect((HEIGHT/ 54)-5, 15, (100 * 9) + 20, 60)
p2healthbackground = pygame.Rect(((HEIGHT/ 54) * 50) - 15 , 15, (100 * 9) + 20, 60)
p2healthbackgroundshadow = pygame.Rect((HEIGHT/ 54) * 50, 20, 100 * 9, 40)

clock = pygame.time.Clock()
p1gothit = False
p2gothit = False
screen = pygame.display.set_mode(size)

fps = 60
newtimer = True

def resetvars():
    global tie, roundover, p1facing, p2facing, p1instun, p1standingpunchinstun, p1standingkickinstun, p1crouchingkickinstun, p1crouchingpunchinstun, player1death,roundstart, player2death, player1wins, player2wins, player1died, player2died, player2fallover, player1fallover, p1deathframecount, p2deathframecount
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

    #1 for right 0 for left
    p1facing = 1
    p2facing = 0
    
    p1standingpunchinstun = False
    p1crouchingpunchinstun = False
    p1standingkickinstun = False
    p1crouchingkickinstun = False
    player1.instun = False
    
    timer.timer.setupcountdown(3)
resetvars()
#timer setup
timer.timer.setup()

#character setup
player1.p1.setup()
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
            player1.p1.move(5)
        if p1facing == 0: 
            player1.p1.move(-5)
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
            player2.p2.move(5, p2movementspeed)
        if p2facing == 0:
            player2.p2.move(-5, p2movementspeed)
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
        player1.p1.epunch(p1facing)
        p1framecount = 0
        epunch = False

def qkickstartup(startupframes):
    global p1framecount, qkick, p1inmove, p1facing
    p1framecount = p1framecount + 1
    if p1framecount >= startupframes:
        player1.p1.qkick(p1facing)
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
    p1stayinleftx = player1.p1x - (WIDTH/ 9)/2
    p1stayinrightx = player1.p1x + (WIDTH/ 9)/2
    if p1stayinleftx <= 10:
        player1.p1.move(10)
        p1atedge = True
    if p1stayinrightx >= WIDTH - 10:
        player1.p1.move(-10)
        p1atedge = True
    elif p1stayinleftx >= 30 and p1stayinrightx <= WIDTH - 30:
        p1atedge = False


def p2stayin():
    global p2atedge
    p2stayinleftx = player2.p2x - (WIDTH/9)/2
    p2stayinrightx = player2.p2x + (WIDTH/9)/2
    if p2stayinleftx <= 10:
        player2.p2.move(10, p2movementspeed)
        p2atedge = True
    if p2stayinrightx >= WIDTH - 10:
        player2.p2.move(-10, p2movementspeed)
        p2atedge = True
    elif p2stayinleftx >= 30 and p2stayinrightx <= WIDTH - 30:
        p2atedge = False



def p1pushing():
    global p1moveright, p1moveleft, p2atedge, p2moveright, p2moveleft, p1facing
    if p1facing == 1:
        if player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p2atedge == True:
            player1.p1.move(-10)
        elif player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p1moveright == True:
            player2.p2.move(10, p2movementspeed)
    if p1facing == 0:
        if player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p2atedge == True:
            player1.p1.move(10)
        elif player1.p1hurtbox.colliderect(player2.p2hurtbox) == True and p1moveleft == True:
            player2.p2.move(-10, p2movementspeed)
        
    

def p2pushing():
    global p2moveleft, p2moveright, p1moveleft, p1moveright, p1atedge, p2facing
    if p2facing == 1:
        if player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p1atedge == True:
            player2.p2.move(-10, p2movementspeed)
        elif player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p2moveright == True:
            player1.p1.move(10)
    if p2facing == 0:
        if player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p1atedge == True:
            player2.p2.move(10,p2movementspeed)
        elif player2.p2hurtbox.colliderect(player1.p1hurtbox) == True and p2moveleft == True:
            player1.p1.move(-10)


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

#attack interupted
def p1interupted():
    global p1framecount
    player1.qkickout = False
    player1.epunchout = False
    p1framecount = 0

def p2interupted():
    global p2framecount
    player2.okickout = False
    player2.upunchout = False
    p2framecount = 0

#hitboxes and hitdetection
#p1 got hit means player 2 got hit
#p2 got hit means player 1 got hit

def epunchhitbox():
    global p1gothit, epunchknockback
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            p2interupted()
            if player2.noknockback == False:
                epunchknockback = True
            if player1.crouch == False:
                player2.p2.takedamage(100)
            if player1.crouch == True:
                player2.p2.takedamage(100)
            p1gothit = True

def qkickhitbox():
    global p1gothit, qkickknockback
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            p2interupted()
            if player2.noknockback == False:
                qkickknockback = True
            if player1.crouch == False:
                player2.p2.takedamage(4)
            if player1.crouch == True:
                player2.p2.takedamage(2)
            p1gothit = True

def upunchhitbox():
    global p2gothit, upunchknockback, p1standingpunchinstun, p1crouchingpunchinstun, p1framecount   
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            p1interupted()
            player1.instun = True
            p1framecount = 0
            if player1.noknockback == False:
                upunchknockback = True
            if player2.crouch == False:
                player1.p1.takedamage(100)
                p1standingpunchinstun = True
            if player2.crouch == True:
                player1.p1.takedamage(5)
                p1crouchingpunchinstun = True
            p2gothit = True

def okickhitbox():
    global p2gothit, okickknockback, p1standingkickinstun, p1crouchingkickinstun, p1framecount
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            p1interupted()
            player1.instun = True
            p1framecount = 0
            if player1.noknockback == False:
                okickknockback = True
            if player2.crouch == False:
                player1.p1.takedamage(4)
                p1standingkickinstun = True
            if player2.crouch == True:
                player1.p1.takedamage(2)
                p1crouchingkickinstun = True
            p2gothit = True


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
                    player1.p1.blocking()
            if event.key == pygame.K_a:
                p1moveleft = True
                if p1facing == 1:
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
                    player2.p2.blocking()
            if event.key == pygame.K_j:
                p2moveleft = True
                if p2facing == 1:
                    player2.p2.blocking()
            if event.key == pygame.K_k:
                if player2.onground == True:
                    p2crouch = True
            if event.key == pygame.K_i:
                if player2.instun == True:
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
                    player1.p1.move(10)
                if p1facing == 0:
                    player1.p1.move(5)

        if p1moveright == False:
            if p1moveleft == True:
                if p1facing == 0:
                    player1.p1.move(-10)
                if p1facing == 1:
                    player1.p1.move(-5)

        if p1crouch == True:
            player1.p1.crouch()
        if p1jump == True:
            player1.p1.jump()
        #player 1 uncrouch
        if p1crouch == False:
            player1.p1.uncrouch()
    if player1.instun == False:
        if epunch == True:
            p1inmove = True
            if p1crouch == False:
                epunchstartup(3)
            if p1crouch == True:
                epunchstartup(10)
        if qkick == True:
            p1inmove = True
            if p1crouch == False:
                qkickstartup(20)
            if p1crouch == True:
                qkickstartup(7)

    if p2inmove == False:
        #player 2 move and crouch
        if p2moveleft == False:
            if p2moveright == True:
                if p2facing == 1:
                    player2.p2.move(10, p2movementspeed)
                if p2facing == 0:
                    player2.p2.move(5, p2movementspeed)

        if p2moveright == False:
            if p2moveleft == True:
                if p2facing == 1:
                    player2.p2.move(-5, p2movementspeed)
                if p2facing == 0:
                    player2.p2.move(-10, p2movementspeed)

        if p2crouch == True:
            player2.p2.crouch(p2crouchingfloor)
        if p2jump == True:
            player2.p2.jump(p2jumpspeed, p2jumpheight)
        #player 2 uncrouch
        if p2crouch == False:
            player2.p2.uncrouch()
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
    
    if timer.go == True and timer.time <= 1 and roundover == False:
        gotext = set_text("FIGHT!!", WIDTH/2, HEIGHT/2, 200, white)
        screen.blit(gotext[0], gotext[1])



    #pushing and bouding and gravity
    player1.p1.gravity()
    player2.p2.gravity(p2floor)
    facing()
    p1stayin()
    p2stayin()
    p1pushing()
    p2pushing()

    #epunch
    if epunchinendlag and p1crouch == True:
        epunchendlag(15)
    elif epunchinendlag == True:
        epunchendlag(10)
    if player1.epunchout == True and p1crouch == False:
        epunchhitbox()
        epunchactive(7)
    elif player1.epunchout == True:
        epunchhitbox()
        epunchactive(5)

    #qkick
    if qkickinendlag and p1crouch == True:
        qkickendlag(7)
    elif qkickinendlag == True:
        qkickendlag(15)
    if player1.qkickout == True and p1crouch == False:
        qkickhitbox()
        qkickactive(10)
    elif player1.qkickout == True:
        qkickhitbox()
        qkickactive(5)

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
        player2.p2.fallover_death()
        player2.instun = True

    if player1fallover == True:
        player1.p1.fallover_death()
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
                    p2knockbackright(10, 100, 50, -50)
                elif p1facing == 0:
                    p2knockbackleft(10, -100, 50, -50)
                if player2.knockbacked == True:
                    epunchknockback = False
                    player2.knockbacked = False
            if player1.crouch == True:
                if p1facing == 1:
                    p2knockbackright(110, 400, 100, -200)
                elif p1facing == 0:
                    p2knockbackleft(110, 400, 100, -200)
                if player2.knockbacked == True:
                    epunchknockback = False
                    player2.knockbacked = False

        if qkickknockback == True:
            if player1.crouch == False:
                if p1facing == 1:
                    p2knockbackright(200, 800, 50, -50)
                elif p1facing == 0:
                    p2knockbackleft(200, -800, 50, -50)
                if player2.knockbacked == True:
                    qkickknockback = False
                    player2.knockbacked = False
            if player1.crouch == True:
                if p1facing == 1:
                    p2knockbackright(100, 50, 150, -450)
                elif p1facing == 0:
                    p2knockbackleft(100, 50, 150, -450)
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
        if p1standingpunchinstun == True:
            p1stun(p2standingpunchstun)

        if p1crouchingpunchinstun == True:
            p1stun(p2crouchingpunchstun)
    
        if p1standingkickinstun == True:
            p1stun(p2standingkickstun)
            print(p1framecount)
    
        if p1crouchingkickinstun == True:
            p1stun(p2crouchingkickstun)
    elif player1.instun == False:
        p1standingkickinstun = False
        p1standingpunchinstun = False
        p1crouchingpunchinstun = False
        p1crouchingkickinstun = False

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
        timer.timer.count(60)
        timertext = set_text(str(timer.time), WIDTH/2, 125, 100, white)
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
            player1.p1.setup()
            player2.p2.setup(p2standingwidth, p2standingheight, p2crouchingwidth, p2crouchingheight)
            fps = 60 
            p1inmove = False
            p2inmove = False
            newtimer = True

    #drawing


    pygame.draw.rect(screen, white, p1healthbackground, 0)
    pygame.draw.rect(screen, gray, p1healthbackgroundshadow, 0)
    pygame.draw.rect(screen, red, pygame.Rect((HEIGHT/ 54), 20, player1.p1health * 9, 40), 0)
    pygame.draw.rect(screen, white, p2healthbackground, 0)
    pygame.draw.rect(screen, gray, p2healthbackgroundshadow, 0)
    pygame.draw.rect(screen, red, pygame.Rect(((HEIGHT/54) * 50) + ((100 * 9) - player2.p2health * 9), 20, player2.p2health * 9, 40), 0)
    pygame.draw.circle(screen, white, (75, 125), 30, 0)
    pygame.draw.circle(screen, white, (150, 125), 30, 0)
    pygame.draw.circle(screen, white, (1845, 125), 30, 0)
    pygame.draw.circle(screen, white, (1770, 125), 30, 0)

    if p1inmove == False and player1.instun == False:
        pygame.draw.rect(screen, yellow, player1.p1hurtbox, 2)
    elif p1inmove == True or player1.instun == True:
        pygame.draw.rect(screen, dimmedyellow, player1.p1hurtbox, 2)
    
    if p2inmove == False:
        pygame.draw.rect(screen, blue, player2.p2hurtbox, 2)
    elif p2inmove == True:
        pygame.draw.rect(screen, dimmedblue, player2.p2hurtbox, 2)
    
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
        player1.p1.setup()
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
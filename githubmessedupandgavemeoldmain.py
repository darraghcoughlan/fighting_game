
from pygame.constants import FULLSCREEN, KEYDOWN, KEYUP, KSCAN_ESCAPE, K_ESCAPE

import time, pygame, time, sys
import player1
import player2

#pygame setup
size = HEIGHT, WIDTH = 1080, 1920    
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



p1healthbackgroundshadow = pygame.Rect((WIDTH/ 54), 20, (100*9), 40)
p1healthbackground = pygame.Rect((WIDTH/ 54)-5, 15, (100 * 9) + 20, 60)
p2healthbackground = pygame.Rect(((WIDTH/ 54) * 50) - 15 , 15, (100 * 9) + 20, 60)
p2healthbackgroundshadow = pygame.Rect((WIDTH/ 54) * 50, 20, 100 * 9, 40)

clock = pygame.time.Clock()
p1gothit = False
p2gothit = False
screen = pygame.display.set_mode(size)

#character setup
player1.p1.setup()
player2.p2.setup()
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

fps = 60

player1death = False
player2death = False

player2wins = False
player1wins = False

#endlag

def epunchendlag(endlagframes):
    global p1framecount, p1inmove, epunch, epunchinendlag
    p1framecount = p1framecount + 1
    if p1framecount >= endlagframes:
        epunch = False
        p1inmove = False
        epunchinendlag = False

def qkickendlag(endlagframes):
    global p1framecount, p1inmove, qkick, qkickinendlag
    p1framecount = p1framecount + 1
    if p1framecount >= endlagframes:
        qkick = False
        p1inmove = False
        qkickinendlag = False

def upunchendlag(endlagframes):
    global p2framecount, p2inmove, upunch, upunchinendlag
    p2framecount = p2framecount + 1
    if p2framecount >= endlagframes:
        upunch = False
        p2inmove = False
        upunchinendlag = False

def okickendlag(endlagframes):
    global p2framecount, p2inmove, okick, okickinendlag
    p2framecount = p2framecount + 1
    if p2framecount >= endlagframes:
        okick = False
        p2inmove = False
        okickinendlag = False

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
    global p1framecount, p1gothit, qkickinendlag
    p1framecount = p1framecount + 1
    if player1.crouch == False:
        player1.p1.move(5)
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
    global p2framecount, p2gothit, okickinendlag
    p2framecount = p2framecount + 1
    if player2.crouch == False:
        player2.p2.move(-5)
    if p2framecount >= activeframes:
        player2.okickout = False
        p2framecount = 0
        p2gothit = False
        okickinendlag = True

#startup

def epunchstartup(startupframes):
    global p1framecount, epunch, p1inmove
    p1framecount = p1framecount + 1
    if p1framecount >= startupframes:
        player1.p1.epunch()
        p1framecount = 0
        epunch = False

def qkickstartup(startupframes):
    global p1framecount, qkick, p1inmove
    p1framecount = p1framecount + 1
    if p1framecount >= startupframes:
        player1.p1.qkick()
        p1framecount = 0
        qkick = False

def upunchstartup(startupframes):
    global p2framecount, upunch, p2inmove
    p2framecount = p2framecount + 1
    if p2framecount >= startupframes:
        player2.p2.upunch()
        p2framecount = 0
        upunch = False

def okickstartup(startupframes):
    global p2framecount, okick, p2inmove
    p2framecount = p2framecount + 1
    if p2framecount >= startupframes:
        player2.p2.okick()
        p2framecount = 0
        okick = False


#pushing and bounding arena
def p1stayin():
    global p1atedge
    p1stayinleftx = player1.p1x - (WIDTH/ 9)
    p1stayinrightx = player1.p1x + (WIDTH/ 9)
    if p1stayinleftx <= 0:
        player1.p1.move(10)
        p1atedge = True
    if p1stayinrightx >= 1920:
        player1.p1.move(-10) 
    if p1stayinleftx <= 0:
        p1atedge = True
    if p1stayinrightx >= 1910:
        p1atedge = True
    elif p1stayinleftx >= 10:
        p1atedge = False

def p2stayin():
    global p2atedge
    p2stayinleftx = player2.p2x - (WIDTH/ 9)
    p2stayinrightx = player2.p2x + (WIDTH/ 9)
    if p2stayinleftx <= 0:
        player2.p2.move(10)
    if p2stayinrightx >= 1920:
        player2.p2.move(-10)
    if p2stayinleftx <= 10:
        p2atedge = True
    if p2stayinrightx >= 1910:
        p2atedge = True


def p1pushing():
    global p1moveright
    if player1.p1hurtbox.colliderect(player2.p2hurtbox) and p1moveright == True and p2atedge == False:
        player2.p2.move(10)
    elif player1.p1hurtbox.colliderect(player2.p2hurtbox) and p2atedge == True:
        player1.p1.move(-10)
    elif player1.p1hurtbox.colliderect(player2.p2hurtbox):
        player1.p1.move(-10)

def p2pushing():
    global p2moveleft
    if player2.p2hurtbox.colliderect(player1.p1hurtbox) and p2moveleft == True and p1atedge == False:
        player1.p1.move(-10)
    elif player2.p2hurtbox.colliderect(player1.p1hurtbox) and p1atedge == True:
        player2.p2.move(10)
    elif player2.p2hurtbox.colliderect(player1.p1hurtbox):
        player2.p2.move(10)

#hitboxes and hitdetection
#p1 got hit means player 2 got hit
#p2 got hit means player 1 got hit

def epunchhitbox():
    global p1gothit
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            if player1.crouch == False:
                player2.p2.takedamage(3)
                player2.p2.yvelocity(50, -50)
                player2.p2.xvelocity(10, 100)
            if player1.crouch == True:
                player2.p2.takedamage(100)
                player2.p2.yvelocity(100, -200)
                player2.p2.xvelocity(110, 400)
            p1gothit = True

def qkickhitbox():
    global p1gothit
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            if player1.crouch == False:
                player2.p2.takedamage(4)
                player2.p2.yvelocity(50, -50)
                player2.p2.xvelocity(200, 800)
            if player1.crouch == True:
                player2.p2.takedamage(2)
                player2.p2.yvelocity(150, -450)
                player2.p2.xvelocity(100, 50)
            p1gothit = True

def upunchhitbox():
    global p2gothit
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            if player2.crouch == False:
                player1.p1.takedamage(3)
                player1.p1.yvelocity(50, - 50)
                player1.p1.xvelocity(10, - 100)
            if player2.crouch == True:
                player1.p1.takedamage(5)
                player1.p1.yvelocity(100, - 200)
                player1.p1.xvelocity(110, -400)
            p2gothit = True

def okickhitbox():
    global p2gothit
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            if player2.crouch == False:
                player1.p1.takedamage(4)
                player1.p1.yvelocity(50, -50)
                player1.p1.xvelocity(200, -800)
            if player2.crouch == True:
                player1.p1.takedamage(2)
                player1.p1.yvelocity(150, -450)
                player1.p1.xvelocity(100, -50)
            p2gothit = True

def player1dies():
    player1.p1.yvelocity(100, 200)
    player1.p1.xvelocity(-5, 100)
    if player1death == True:
        fps = 60


def player2dies():
    player2.p2.yvelocity(100, 200)
    player2.p2.xvelocity(5, 100)
    if player2death == True:
            fps = 60

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
            if event.key == pygame.K_a:
                p1moveleft = True
                player1.p1.blocking()
            if event.key == pygame.K_s:
                if player1.onground == True:
                    p1crouch = True
            if event.key == pygame.K_w:
                p1jump = True
            if p1inmove == False:
                if event.key == pygame.K_e:
                    epunch = True
                if event.key == pygame.K_q:
                    qkick = True

           
            #player 2 movement and moves
            if event.key == pygame.K_l:
                p2moveright = True
                player2.p2.blocking()
            if event.key == pygame.K_j:
                p2moveleft = True
            if event.key == pygame.K_k:
                if player2.onground == True:
                    p2crouch = True
            if event.key == pygame.K_i:
                p2jump = True
            if p2inmove == False:
                if event.key == pygame.K_u:
                    upunch = True
                if event.key == pygame.K_o:
                    okick = True
            
        elif event.type == KEYUP:
            if event.key == pygame.K_d:
                p1moveright = False
            if event.key == pygame.K_a:
                p1moveleft = False
                player1.p1.unblocking()
            if event.key == pygame.K_s:
                p1crouch = False
            if event.key == pygame.K_l:
                p2moveright = False
                player2.p2.unblocking()
            if event.key == pygame.K_j:
                p2moveleft = False
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
        if p1moveright == True:
            player1.p1.move(10)
        if p1moveleft == True:
            player1.p1.move(-5)
        if p1crouch == True:
            player1.p1.crouch()
        if p1jump == True:
            player1.p1.jump()
        #player 1 uncrouch
        if p1crouch == False:
            player1.p1.uncrouch()
    if epunch == True:
        p1inmove = True
        epunchstartup(5)
    if qkick == True:
        p1inmove = True
        qkickstartup(10)

    if p2inmove == False:
        #player 2 move and crouch
        if p2moveright == True:
            player2.p2.move(5)
        if p2moveleft == True:
            player2.p2.move(-10)
        if p2crouch == True:
            player2.p2.crouch()
        if p2jump == True:
            player2.p2.jump()
        #player 2 uncrouch
        if p2crouch == False:
            player2.p2.uncrouch()
    if upunch == True:
        p2inmove = True
        upunchstartup(5)
    if okick == True:
        p2inmove = True
        okickstartup(10)

    #win condidtion
    if player1.p1health <= 0:
        player2wins = True

    if player2.p2health <= 0:
        player1wins = True
    
    #pushing and bouding and gravity
    player1.p1.gravity()
    player2.p2.gravity()
    p1stayin()
    p2stayin()
    p1pushing()
    p2pushing()

    #epunch
    if epunchinendlag and p1crouch == True:
        epunchendlag(15)
    elif epunchinendlag == True:
        epunchendlag(10)
    if player1.epunchout == True:
        epunchhitbox()
        epunchactive(7)

    #qkick
    if qkickinendlag and p1crouch == True:
        qkickendlag(7)
    elif qkickinendlag == True:
        qkickendlag(15)
    if player1.qkickout == True:
        qkickhitbox()
        qkickactive(10)

    #upunch
    if upunchinendlag and p2crouch == True:
        upunchendlag(15)
    elif upunchinendlag == True:
        upunchendlag(10)
    if player2.upunchout == True:
        upunchhitbox()
        upunchactive(7)

    #okick
    if okickinendlag and p2crouch == True:
        okickendlag(7)
    elif okickinendlag == True:
        okickendlag(15)
    if player2.okickout == True:
        okickhitbox()
        okickactive(10)

    #player wins
    if player1wins == True:
        player1winstext = set_text("PLAYER 1 WINS", 950, 250, 200, white)
        screen.blit(player1winstext[0], player1winstext[1])
        p2inmove = True
        fps = 10
        player2.oldp2x = 0
        player2.p2.gravity()
        if player2death == False:
            player2dies()
            player2death = True

    if player2wins == True:
        player2winstext = set_text("PLAYER 2 WINS", 950, 250, 200, white)
        screen.blit(player2winstext[0], player2winstext[1])
        p1inmove = True
        fps = 10
        player1.oldp1x = 0 
        player2.p2.gravity()
        if player1dies == False:
            player1dies()
            player1death = True


    if p1inmove == False:
        pygame.draw.rect(screen, yellow, player1.p1hurtbox, 2)
    elif p1inmove == True:
        pygame.draw.rect(screen, dimmedyellow, player1.p1hurtbox, 2)
    
    if p2inmove == False:
        pygame.draw.rect(screen, blue, player2.p2hurtbox, 2)
    elif p2inmove == True:
        pygame.draw.rect(screen, dimmedblue, player2.p2hurtbox, 2)
    pygame.draw.rect(screen, white, p1healthbackground, 0)
    pygame.draw.rect(screen, gray, p1healthbackgroundshadow, 0)
    pygame.draw.rect(screen, red, pygame.Rect((WIDTH/ 54), 20, player1.p1health * 9, 40), 0)
    pygame.draw.rect(screen, white, p2healthbackground, 0)
    pygame.draw.rect(screen, gray, p2healthbackgroundshadow, 0)
    pygame.draw.rect(screen, red, pygame.Rect(((WIDTH/54) * 50) + ((100 * 9) - player2.p2health * 9), 20, player2.p2health * 9, 40), 0)

   
    pygame.display.flip()
    p2atedge = False
    
    clock.tick(fps)
from pygame.constants import FULLSCREEN, KEYDOWN, KEYUP, KSCAN_ESCAPE, K_ESCAPE
punch = 0
import time, pygame, time, sys
import player1
import player2

#pygame setup
size = HEIGHT, WIDTH = 1920, 1080
p1framecount = 0
p2framecount = 0
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
red = (255, 0, 0)

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
p2moveright = False
p2moveleft = False


#frame data

def epunchactive(activeframes):
    global p1framecount, p1gothit
    p1framecount = p1framecount + 1
    if p1framecount >= activeframes:
        player1.epunchout = False
        p1framecount = 0
        p1gothit = False

def upunchactive(activeframes):
    global p2framecount, p2gothit
    p2framecount = p2framecount + 1
    if p2framecount >= activeframes:
        player2.upunchout = False
        p2framecount = 0
        p2gothit = False

#pushing
def p1pushing():
    global p1moveright
    if player1.p1hurtbox.colliderect(player2.p2hurtbox) and p1moveright == True:
        player2.p2.move(10)

def p2pushing():
    global p2moveleft
    if player2.p2hurtbox.colliderect(player1.p1hurtbox) and p2moveleft == True:
        player1.p1.move(-10)

#hitboxes and hitdetection
#p1 got hit means player 2 got hit
#p2 got hit means player 1 got hit

def epunchhitbox():
    global p1gothit
    pygame.draw.rect(screen, red, player1.hitbox, 0)
    if p1gothit == False:
        if player1.hitbox.colliderect(player2.p2hurtbox):
            player2.p2.takedamage(3)
            p1gothit = True

def upunchhitbox():
    global p2gothit
    pygame.draw.rect(screen, red, player2.hitbox, 0)
    if p2gothit == False:
        if player2.hitbox.colliderect(player1.p1hurtbox):
            player1.p1.takedamage(3)
            p2gothit = True


#main pygame loop 
pygame.init()

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

            #player 1 movement
            if event.key == pygame.K_d:
                p1moveright = True
            if event.key == pygame.K_a:
                p1moveleft = True
            if event.key == pygame.K_e:
                player1.p1.epunch()
            if event.key == pygame.K_s:
                p1crouch = True

            #player 2 movement
            if event.key == pygame.K_l:
                p2moveright = True
            if event.key == pygame.K_j:
                p2moveleft = True
            if event.key == pygame.K_u:
                player2.p2.upunch()
            
        elif event.type == KEYUP:
            if event.key == pygame.K_d:
                p1moveright = False
            if event.key == pygame.K_a:
                p1moveleft = False
            if event.key == pygame.K_s:
                p1crouch = False
            if event.key == pygame.K_l:
                p2moveright = False
            if event.key == pygame.K_j:
                p2moveleft = False
    
    #player 1 move and crouch
    if p1moveright == True:
        player1.p1.move(10)
    if p1moveleft == True:
        player1.p1.move(-10)
    if p1crouch == True:
        player1.p1.crouch()
    #player 1 uncrouch
    if p1crouch == False:
        player1.p1.uncrouch()

    if p2moveright == True:
        player2.p2.move(10)
    if p2moveleft == True:
        player2.p2.move(-10)

    #win condidtion
    if player1.p1health <= 0 or player2.p2health <= 0:
        print("you win")
        pygame.quit()
        sys.exit()
    
    #pushing
    p1pushing()
    p2pushing()

    #epunch
    if player1.epunchout == True:
        epunchhitbox()
    if player1.epunchout == True:
        epunchactive(7)

    #upunch
    if player2.upunchout == True:
        upunchhitbox()
    if player2.upunchout == True:
        upunchactive(7)

    pygame.draw.rect(screen, yellow, player1.p1hurtbox, 2)
    pygame.draw.rect(screen, yellow, player2.p2hurtbox, 2)
    pygame.draw.rect(screen, red, pygame.Rect((WIDTH/ 54), 20, player1.p1health * 9, 40), 0)
    pygame.draw.rect(screen, red, pygame.Rect(((WIDTH/54) * 50) + ((100 * 9) - player2.p2health * 9), 20, player2.p2health * 9, 40), 0)
    pygame.display.flip()

    clock.tick(60)
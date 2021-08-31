import pygame
import shotocharacter

def sayhello():
    shotocharacter.sayhello()

class p2():
    def setup(standingwidth, standingheight, crouchingwidth, crouchingheight):
        global p2x, p2y, p2hurtbox, onground, crouchhurtbox, basep2hurtbox, knockbacked, death,  noknockback, yvelocityend, xvelocityend, jump, oldp2x, oldp2y, isblocking, okickout, p2health, WIDTH, HEIGHT, crouch,  upunchout, p2framecount, black, yellow, green, red
        size = HEIGHT, WIDTH = 1080, 1920
        p2x, p2y = ((WIDTH/ 10) * 9), (HEIGHT/ 10) * 7
        basep2hurtbox = pygame.Rect(p2x, p2y, standingwidth, standingheight)
        crouchhurtbox = pygame.Rect(p2x, p2y, crouchingwidth, crouchingheight)
        p2hurtbox = basep2hurtbox
        p2hurtbox.center = p2x, p2y
        p2health = 100
        p2framecount = 0
        upunchout = False
        crouch = False
        okickout = False
        isblocking = False
        onground = True
        jump = False
        oldp2x = 0
        oldp2y = 0

        death = False

        noknockback = False

        knockbacked = False
        yvelocityend = False
        xvelocityend = False

        black = (0, 0, 0)
        yellow = (255, 255, 0)
        green = (0, 128, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)

    def takedamage(damagedealt):
        global p2health, isblocking
        if isblocking == True:
            p2health = p2health - (damagedealt / 2)
        else:
            p2health = p2health - damagedealt

    def gravity():
        global p2y, HEIGHT, onground
        if p2y < (HEIGHT/ 10) * 7:
            p2y = p2y + 20
        if p2y > (HEIGHT / 10 ) * 7:
            p2y = (HEIGHT / 10) * 7
        if p2y == (HEIGHT / 10) * 7:
            onground = True

    def move(moveby):
        global p2x, p2y, crouch, HEIGHT
        p2x = p2x + moveby
        if crouch == False:
            p2hurtbox.center = p2x, p2y
        if crouch == True:
            p2y = (HEIGHT / 10) * 7
            p2hurtbox.center = p2x, p2y + 96

    def blocking():
        global isblocking, noknockback
        isblocking = True
        noknockback = True

    def unblocking():
        global isblocking, noknockback
        isblocking = False
        noknockback = False

    def crouch():
        global WIDTH, HEIGHT, p2hurtbox, crouch
        crouch = True
        p2hurtbox = crouchhurtbox
        p2hurtbox.center = p2x, p2y + 96

    def uncrouch():
        global p2hurtbox, WIDTH, HEIGHT, crouch
        p2hurtbox = basep2hurtbox
        p2hurtbox.center = p2x, p2y
        crouch = False

    def upunch(p2facing):
        global upunchout, hitbox, crouch
        if p2facing == 1:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx, p2hurtbox.centery - 85, 250, 50)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx,p2hurtbox.centery - 85, 225, 50)
        if p2facing == 0:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx - 250, p2hurtbox.centery - 85, 250, 50)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx - 225, p2hurtbox.centery - 85, 225, 50)
        upunchout = True
    
    def okick(p2facing):
        global okickout, hitbox, crouch
        if p2facing == 1:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx, p2hurtbox.centery + 20, 300, 75)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx, p2hurtbox.centery + 65, 350, 50)
        if p2facing == 0:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx - 300, p2hurtbox.centery + 20, 300, 75)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx - 350, p2hurtbox.centery + 65, 350, 50)
        okickout = True

    def yvelocity(speed, destination):
        global p2y, onground, oldp2y, yvelocityend, death
        if death == True:
            speed = speed / 2
        if oldp2y > destination:
            p2y = p2y - speed
            oldp2y = oldp2y - speed
        if oldp2y <= destination:
            oldp2y = 0
            yvelocityend = True
            
    def jumpvelocity(speed, destination):
        global p2y, onground
        if p2y > destination:
            p2y = p2y - speed
            if jump == True:
                if p2y <= destination:
                    onground = False
            else:
                onground = False

    def xvelocityright(speed, destination):
        global p2x, oldp2x, xvelocityend, death
        if death == True:
            speed = speed / 2
            destination = (destination / 5) * 7
        if oldp2x < destination:
            p2x = p2x + speed
            oldp2x = oldp2x + speed
        if oldp2x >= destination:
            oldp2x = 0
            xvelocityend = True

    def xvelocityleft(speed, destination):
        global p2x, oldp2x, xvelocityend, death
        if death == True:
            speed = speed / 2
            destination = (destination/5 ) * 7
        if oldp2x > destination:
            p2x = p2x - speed
            oldp2x = oldp2x - speed
        if oldp2x <= destination:
            oldp2x = 0
            xvelocityend = True
            
    def jump():
        global HEIGHT, onground, jump
        if onground == True:
            p2.jumpvelocity(75, (HEIGHT / 8))
            jump = True

    def fallover_death():
        global p2hurtbox, HEIGHT, WIDTH, p2x, p2y
        p2hurtbox = pygame.Rect(p2x, p2y, (HEIGHT/ 2.5), (WIDTH/ 9))
        p2hurtbox.center = p2x, p2y + 107
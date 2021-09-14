import pygame
import shotocharacter

def sayhello():
    shotocharacter.sayhello()

class p2():
    def setup(standingwidth, standingheight, crouchingwidth, crouchingheight):
        global p2x, p2y, p2hurtbox, instun, onground, crouchhurtbox, basep2hurtbox, knockbacked, death,  noknockback, yvelocityend, xvelocityend, jump, oldp2x, oldp2y, isblocking, okickout, p2health, WIDTH, HEIGHT, crouch,  upunchout, p2framecount, black, yellow, green, red
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

        instun = False

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

    def gravity(floor):
        global p2y, HEIGHT, onground
        if p2y < floor:
            p2y = p2y + 20
        if p2y > floor:
            p2y = floor
        if p2y == floor:
            onground = True

    def move(moveby, movementspeed, floor, crouchingfloor):
        global p2x, p2y, crouch, HEIGHT
        if instun == True:
            moveby = moveby / 10
        moveby = moveby * movementspeed
        p2x = p2x + moveby
        if crouch == False:
            p2hurtbox.center = p2x, p2y
        if crouch == True:
            p2y = floor
            p2hurtbox.center = p2x, p2y + crouchingfloor
        
    def stayin(moveby):
        global crouch, p2x, p2y
        p2x = p2x + moveby

    def blocking():
        global isblocking, noknockback
        isblocking = True
        noknockback = True

    def unblocking():
        global isblocking, noknockback
        isblocking = False
        noknockback = False

    def crouch(crouchfloor):
        global WIDTH, HEIGHT, p2hurtbox, crouch
        crouch = True
        p2hurtbox = crouchhurtbox
        p2hurtbox.center = p2x, p2y + crouchfloor

    def uncrouch():
        global p2hurtbox, WIDTH, HEIGHT, crouch
        p2hurtbox = basep2hurtbox
        p2hurtbox.center = p2x, p2y
        crouch = False

    def upunch(p2facing, standingwidth, standingheight, standingy, standingx, crouchingwidth, crouchingheight, crouchingx, crouchingy):
        global upunchout, hitbox, crouch
        if p2facing == 1:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx + standingx, p2hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx + crouchingx ,p2hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        if p2facing == 0:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx - standingwidth - standingx, p2hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx - crouchingwidth - crouchingx, p2hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        upunchout = True
    
    def okick(p2facing, standingwidth, standingheight, standingy, standingx, crouchingwidth, crouchingheight, crouchingx, crouchingy):
        global okickout, hitbox, crouch
        if p2facing == 1:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx + standingx, p2hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx + crouchingx, p2hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        if p2facing == 0:
            if crouch == False:
                hitbox = pygame.Rect(p2hurtbox.centerx - standingwidth - standingx, p2hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p2hurtbox.centerx - crouchingwidth - crouchingx, p2hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
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
        global p2y, onground, oldp2y
        if p2y >= destination:
            p2y = p2y - speed
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
            
    def jump(jumpspeed, jumpheight):
        global HEIGHT, onground, jump
        if onground == True:
            p2.jumpvelocity(jumpspeed, jumpheight)
            jump = True

    def fallover_death(standingwidth, standingheight):
        global p2hurtbox, HEIGHT, WIDTH, p2x, p2y
        p2hurtbox = pygame.Rect(p2x, p2y, standingheight, standingwidth)
        p2hurtbox.center = p2x, p2y + 107
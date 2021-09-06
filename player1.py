import pygame

def sayhello():
    print("hello world")

class p1():
    def setup(standingwidth, standingheight, crouchingwidth, crouchingheight):
        global p1x, p1y, p1hurtbox,crouch, basep1hurtbox, crouchhurtbox, noknockback, death, instun, oldp1x, oldp1y, knockbacked, xvelocityend, yvelocityend, onground, jump, isblocking, qkickout, p1health, WIDTH, HEIGHT, p1gothit,  hitbox, p1framecount, black, yellow, green, red, epunchout
        size = HEIGHT, WIDTH = 1080, 1920
        p1x, p1y = (WIDTH / 10), (HEIGHT/ 10) * 7
        basep1hurtbox = pygame.Rect(p1x, p1y, standingwidth, standingheight)
        crouchhurtbox = pygame.Rect(p1x, p1y, crouchingwidth, crouchingheight)
        p1hurtbox = basep1hurtbox
        p1hurtbox.center = p1x, p1y
        p1health = 100
        epunchout = False
        p1framecount = 0
        crouch = False
        qkickout = False
        isblocking = False
        onground = True
        jump = False
        oldp1x = 0
        oldp1y = 0

        p1floor = 0

        death = False

        noknockback = False

        knockbacked = False
        xvelocityend = False
        yvelocityend = False

        instun = False

        black = (0, 0, 0)
        yellow = (255, 255, 0)
        green = (0, 128, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)
    
    def takedamage(damagedealt):
        global p1health, isblocking
        if isblocking == True:
            p1health = p1health - (damagedealt/ 2)
        else:
            p1health = p1health - damagedealt

    def gravity(floor):
        global p1y, HEIGHT, onground, p1floor
        p1floor = floor
        if p1y < floor:
            p1y = p1y + 20
        if p1y > floor:
            p1y = floor
        if p1y == floor:
            onground = True

    def move(moveby, movementspeed, floor, crouchingfloor):
        global p1x, p1y, crouch, HEIGHT
        if instun == True:
            moveby = moveby / 10
        moveby = moveby * movementspeed
        p1x = p1x + moveby
        if crouch == False:
            p1hurtbox.center = p1x, p1y
        if crouch == True:
            p1y = floor
            p1hurtbox.center = p1x, p1y + crouchingfloor

    def blocking():
        global isblocking, noknockback
        isblocking = True
        noknockback = True
    
    def unblocking():
        global isblocking, noknockback
        isblocking = False
        noknockback = False

    def crouch(crouchfloor):
        global WIDTH, HEIGHT, p1hurtbox, crouch
        crouch = True
        p1hurtbox = crouchhurtbox
        p1hurtbox.center = p1x, p1y + crouchfloor
    
    def uncrouch():
        global p1hurtbox, WIDTH, HEIGHT, crouch
        p1hurtbox = basep1hurtbox
        p1hurtbox.center = p1x, p1y
        crouch = False

    def epunch(p1facing, standingwidth, standingheight, standingx, standingy, crouchingwidth, crouchingheight, crouchingx, crouchingy):
        global epunchout, hitbox, crouch
        if p1facing == 1:
            if crouch == False:
                hitbox = pygame.Rect(p1hurtbox.centerx + standingx, p1hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p1hurtbox.centerx + crouchingx ,p1hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        if p1facing == 0:
            if crouch == False:
                hitbox = pygame.Rect(p1hurtbox.centerx - standingwidth - standingx, p1hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p1hurtbox.centerx - crouchingwidth - crouchingx, p1hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        epunchout = True
    
    def qkick(p1facing, standingwidth, standingheight, standingx, standingy, crouchingwidth, crouchingheight, crouchingx, crouchingy):
        global qkickout, hitbox, crouch
        if p1facing == 1:
            if crouch == False:
                hitbox = pygame.Rect(p1hurtbox.centerx + standingx, p1hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p1hurtbox.centerx + crouchingx, p1hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        if p1facing == 0:
            if crouch == False:
                hitbox = pygame.Rect(p1hurtbox.centerx - standingwidth - standingx, p1hurtbox.centery + standingy, standingwidth, standingheight)
            if crouch == True:
                hitbox = pygame.Rect(p1hurtbox.centerx - crouchingwidth - crouchingx, p1hurtbox.centery + crouchingy, crouchingwidth, crouchingheight)
        qkickout = True

    def yvelocity(speed, destination):
        global p1y, oldp1y, yvelocityend
        if death == True:
            speed = speed / 2
        if oldp1y > destination:
            p1y = p1y - speed
            oldp1y = oldp1y - speed
        if oldp1y <= destination:
            oldp1y = 0
            yvelocityend = True

    def jumpvelocity(speed, destination):
        global p1y, onground
        if p1y > destination:
            p1y = p1y - speed
            if jump == True:
                if p1y <= destination:
                    onground = False
            else:
                onground = False

    def xvelocityright(speed, destination):
        global p1x, oldp1x, xvelocityend, death
        if death == True:
            speed = speed / 2
            destination = (destination/5) *7
        if oldp1x < destination:
            p1x = p1x + speed
            oldp1x = oldp1x + speed
        if oldp1x >= destination:
            oldp1x = 0
            xvelocityend = True
    
    def xvelocityleft(speed, destination):
        global p1x, oldp1x, xvelocityend, death
        if death == True:
            speed = speed / 2
            destination = (destination/ 5) *7
        if oldp1x > destination:
            p1x = p1x - speed
            oldp1x = oldp1x - speed
        if oldp1x <= destination:
            oldp1x = 0
            xvelocityend = True
            
    def jump(jumpspeed, jumpheight):
        global HEIGHT, onground, jump
        if onground == True:
            p1.jumpvelocity(jumpspeed, jumpheight)
            jump = True

    def fallover_death(standingwidth, standingheight):
        global p1hurtbox, HEIGHT, WIDTH, p1x, p1y
        p1hurtbox = pygame.Rect(p1x, p1y, standingheight, standingwidth)
        p1hurtbox.center = p1x, p1y + 107
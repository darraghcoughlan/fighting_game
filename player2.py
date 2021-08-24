import pygame

def sayhello():
    print("hello world")

class p2():
    def setup():
        global p2x, p2y, p2hurtbox, onground, jump, oldp2x, isblocking, okickout, p2health, WIDTH, HEIGHT, crouch,  upunchout, p2framecount, black, yellow, green, red, hit
        size = HEIGHT, WIDTH = 1080, 1920
        p2x, p2y = ((WIDTH/ 10) * 9), (HEIGHT/ 10) * 7
        p2hurtbox = pygame.Rect(540, 240, (WIDTH / 9), (HEIGHT/ 2.5))
        p2hurtbox.center = p2x, p2y
        p2health = 100
        hit = False
        p2framecount = 0
        upunchout = False
        crouch = False
        okickout = False
        isblocking = False
        onground = True
        jump = False
        oldp2x = 0

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
        global isblocking 
        isblocking = True

    def unblocking():
        global isblocking
        isblocking = False

    def crouch():
        global WIDTH, HEIGHT, p2hurtbox, crouch
        crouch = True
        p2hurtbox = pygame.Rect(p2x, 240, (WIDTH/ 7), (HEIGHT/ 4.5))
        p2hurtbox.center = p2x, p2y + 96

    def uncrouch():
        global p2hurtbox, WIDTH, HEIGHT, crouch
        p2hurtbox = pygame.Rect(p2x, p2y, (WIDTH / 9), (HEIGHT / 2.5))
        p2hurtbox.center = p2x, p2y
        crouch = False

    def upunch():
        global upunchout, hitbox
        if crouch == False:
            hitbox = pygame.Rect(p2hurtbox.centerx - 250, p2hurtbox.centery - 85, 250, 50)
        if crouch == True:
            hitbox = pygame.Rect(p2hurtbox.centerx - 225, p2hurtbox.centery - 85, 225, 50)
        upunchout = True
    
    def okick():
        global okickout, hitbox
        if crouch == False:
            hitbox = pygame.Rect(p2hurtbox.centerx - 300, p2hurtbox.centery + 20, 300, 75)
        if crouch == True:
            hitbox = pygame.Rect(p2hurtbox.centerx - 350, p2hurtbox.centery + 65, 350, 50)
        okickout = True

    def yvelocity(speed, destination):
        global p2y, onground
        if p2y > destination:
            p2y = p2y - speed
            if jump == True:
                if p2y <= destination:
                    onground = False
            else:
                onground = False

    def xvelocity(speed, destination):
        global p2x, oldp2x
        while oldp2x < destination:
            p2x = p2x + speed
            oldp2x = oldp2x + speed
        if oldp2x >= destination:
            oldp2x = 0
            

    def jump():
        global HEIGHT, onground, jump
        if onground == True:
            p2.yvelocity(100, (HEIGHT / 2.5) - 125)
            jump = True
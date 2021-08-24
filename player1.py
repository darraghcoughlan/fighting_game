import pygame
import time

def sayhello():
    print("hello world")

class p1():
    def setup():
        global p1x, p1y, p1hurtbox,crouch, oldp1x, oldp1y, onground, jump, isblocking, qkickout, p1health, WIDTH, HEIGHT, p1gothit,  hitbox, p1framecount, black, yellow, green, red, epunchout
        size = HEIGHT, WIDTH = 1080, 1920
        p1x, p1y = (WIDTH / 10), (HEIGHT/ 10) * 7
        p1hurtbox = pygame.Rect(540, 240, (WIDTH / 9), (HEIGHT/ 2.5))
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

    def gravity():
        global p1y, HEIGHT, onground
        if p1y < (HEIGHT / 10 ) *7:
            p1y = p1y + 20
        if p1y > (HEIGHT / 10) *7:
            p1y = (HEIGHT / 10 * 7)
        if p1y == (HEIGHT/ 10) *7:
            onground = True

    def move(moveby):
        global p1x, p1y, crouch, HEIGHT
        p1x = p1x + moveby
        if crouch == False:
            p1hurtbox.center = p1x, p1y
        if crouch == True:
            p1y =  (HEIGHT / 10) * 7
            p1hurtbox.center = p1x, p1y + 96

    def blocking():
        global isblocking
        isblocking = True
    
    def unblocking():
        global isblocking 
        isblocking = False

    def crouch():
        global WIDTH, HEIGHT, p1hurtbox, crouch
        crouch = True
        p1hurtbox = pygame.Rect(p1x, 240, (WIDTH/7), (HEIGHT/ 4.5))
        p1hurtbox.center = p1x, p1y + 96
    
    def uncrouch():
        global p1hurtbox, WIDTH, HEIGHT, crouch
        p1hurtbox = pygame.Rect(p1x, p1y, (WIDTH / 9), (HEIGHT / 2.5))
        p1hurtbox.center = p1x, p1y
        crouch = False

    def epunch():
        global epunchout, hitbox, crouch
        if crouch == False:
            hitbox = pygame.Rect(p1hurtbox.centerx, p1hurtbox.centery - 85, 250, 50)
        if crouch == True:
            hitbox = pygame.Rect(p1hurtbox.centerx,p1hurtbox.centery - 85, 225, 50)
        epunchout = True
    
    def qkick():
        global qkickout, hitbox, crouch
        if crouch == False:
            hitbox = pygame.Rect(p1hurtbox.centerx, p1hurtbox.centery + 20, 300, 75)
        if crouch == True:
            hitbox = pygame.Rect(p1hurtbox.centerx, p1hurtbox.centery + 65, 350, 50)
        qkickout = True

    def yvelocity(speed, destination):
        global p1y, onground
        if p1y > destination:
            p1y = p1y - speed
            if jump == True:
                if p1y <= destination:
                    onground = False
            else:
                onground = False
    
    def xvelocity(speed, destination):
        global p1x, oldp1x
        if oldp1x > destination:
            p1x = p1x - speed
            oldp1x = oldp1x - speed
        if oldp1x <= destination:
            oldp1x = 0
            

    def jump():
        global HEIGHT, onground, jump
        if onground == True:
            p1.yvelocity(100, (HEIGHT / 2.5) - 125)
            jump = True
            
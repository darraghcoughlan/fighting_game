import pygame
import time

def sayhello():
    print("hello world")

class p1():
    def setup():
        global p1x, p1y, p1hurtbox,crouch, p1health, WIDTH, HEIGHT, p1gothit,  hitbox, p1framecount, black, yellow, green, red, epunchout
        size = HEIGHT, WIDTH = 1080, 1920
        p1x, p1y = (WIDTH / 10), (HEIGHT/ 10) * 7
        p1hurtbox = pygame.Rect(540, 240, (WIDTH / 9), (HEIGHT/ 2.5))
        p1hurtbox.center = p1x, p1y
        p1health = 100
        epunchout = False
        p1framecount = 0
        crouch = False

        black = (0, 0, 0)
        yellow = (255, 255, 0)
        green = (0, 128, 0)
        red = (255, 0, 0)
    
    def takedamage(damagedealt):
        global p1health
        p1health = p1health - damagedealt

    def move(moveby):
        global p1x, p1y, crouch, HEIGHT
        p1x = p1x + moveby
        if crouch == False:
            p1hurtbox.center = p1x, p1y
        if crouch == True:
            p1y =  (HEIGHT / 10) * 7
            p1hurtbox.center = p1x, p1y + 96


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
    
    def epunchactive(activeframes):
        global p1framecount
        p1framecount = p1framecount + 1
        if p1framecount >= activeframes:
            epunchout = False
            p1framecount = 0
            p1gothit = False

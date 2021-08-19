import pygame

def sayhello():
    print("hello world")

class p2():
    def setup():
        size = HEIGHT, WIDTH = 1080, 1920
        global p2x, p2y, p2hurtbox, p2health, upunchout, p2framecount, black, yellow, green, red, hit
        p2x, p2y = ((WIDTH/ 10) * 9), (HEIGHT/ 10) * 7
        p2hurtbox = pygame.Rect(540, 240, (WIDTH / 9), (HEIGHT/ 2.5))
        p2hurtbox.center = p2x, p2y
        p2health = 100
        hit = False
        p2framecount = 0
        upunchout = False
        
        
        black = (0, 0, 0)
        yellow = (255, 255, 0)
        green = (0, 128, 0)
        red = (255, 0, 0)

    def takedamage(damagedealt):
        global p2health
        p2health = p2health - damagedealt

    def move(moveby):
        global p2x, p2y
        p2x = p2x + moveby
        p2hurtbox.center = p2x, p2y

    def upunch():
        global upunchout, hitbox
        hitbox = pygame.Rect(p2hurtbox.centerx - 250, p2hurtbox.centery - 85, 250, 50)
        upunchout = True
    
    def upunchactive(activeframes):
        global p2framecount
        p2framecount = p2framecount + 1
        if p2framecount >= activeframes:
            epunchout = False
            p2framecount = 0
            p2gothit = False
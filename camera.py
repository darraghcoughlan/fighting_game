
def setup():
    global HEIGHT, yoffset, oldp1y
    HEIGHT = 1080
    yoffset = 0
    oldp1y = 0


def cameraypositionpassive(p1y, p2y, p1floor, p2floor):
    global yoffset, oldp1y
    print("new" + str(p1y))
    print("old" + str(oldp1y))
    if oldp1y < p1y:
        if yoffset > 0:
            yoffset = yoffset - 20
    elif p1y < p1floor - 300:
        #if p1 is in the air
        if yoffset > (p1floor - p1y) - 400:
            yoffset = yoffset + 49
    elif p1y == p1floor:
        yoffset = 0
    oldp1y = p1y
    #elif p1y > p2y:
    #    #if p2is in the air
    #    yoffset =  HEIGHT / 3
    #elif p1y == p2y:
    #    yoffset = 0
    #elif yoffset > 0:
    #    yoffset = yoffset - 10
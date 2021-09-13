
def setup():
    global HEIGHT, yoffset, oldp1y, oldp2y
    HEIGHT = 1080
    yoffset = 0
    oldp1y = 0
    oldp2y = 0


def cameraypositionpassive(p1y, p2y, p1floor, p2floor):
    global yoffset, oldp1y, oldp2y
#   if oldp1y < p1y:
#       if yoffset > 0:
#           yoffset = yoffset - 20
#   elif p1y < p1floor - 300:
#       #if p1 is in the air
#       if yoffset > (p1floor - p1y) - 400:
#           yoffset = yoffset + 49
#   else:
#       yoffset = 0
#  
#
#   if oldp2y < p2y:
#       if yoffset > 0:
#           yoffset = yoffset - 20
#   elif p2y < p2floor - 300:
#       #if p2 is in the air
#       if yoffset > (p1floor - p1y) - 400:
#           yoffset = yoffset + 49
#   else:
#       yoffset = 0
#   oldp1y = p1y
#   oldp2y = p2y
#
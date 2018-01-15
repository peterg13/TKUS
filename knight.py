import battlecode as bc
import random

directions = list(bc.Direction)
unit = 0
gc = 0

#note: (0,0) is the bottom left square

def knightLogic(unitParam, gcParam):
    global unit
    global gc
    unit = unitParam
    gc = gcParam

    d = getMoveDirection()

#current idea for knight movement:
#figure out how many of our units are in each quadrant.  Have the knights move to the quadrant with the least friendly units.
#once in that quadrant they can move randomly
def getMoveDirection():
    quad1 = 0 #top right
    quad2 = 0 #top left
    quad3 = 0 #bottom left
    quad4 = 0 #bottom right

    mapHeight = 0
    mapWidth = 0

    location = unit.location

    if location.is_on_planet(bc.Planet.Earth):
        mapHeight = gc.starting_map(bc.Planet.Earth).height
        mapWidth = gc.starting_map(bc.Planet.Earth).width
    else:
        mapHeight = gc.starting_map(bc.Planet.Mars).height
        mapWidth = gc.starting_map(bc.Planet.Mars).width


    print(mapHeight)
    print(mapWidth)

    #the direction that will be returned
    returnDirection = 0



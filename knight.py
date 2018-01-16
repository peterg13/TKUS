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

    #movement logic will be skipped if knight is in space or in garrison
    # if not unit.location.is_in_garrison() and not unit.location.is_in_space():
    #     d = getMoveDirection()

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

    #save the height and width of the map depending on which planet the unit is on
    if location.is_on_planet(bc.Planet.Earth):
        mapHeight = gc.starting_map(bc.Planet.Earth).height
        mapWidth = gc.starting_map(bc.Planet.Earth).width
    else:
        mapHeight = gc.starting_map(bc.Planet.Mars).height
        mapWidth = gc.starting_map(bc.Planet.Mars).width


    for myUnit in gc.my_units():
        x = myUnit.location.map_location().x
        y = myUnit.location.map_location().y
        if x < mapWidth/2:
            if y < mapHeight/2:
                quad3 += 1
            else:
                quad2 += 1
        else:
            if y < mapHeight/2:
                quad4 += 1
            else:
                quad1 += 1

    if gc.round() % 100 == 0:
        print("Quad1: %s, Quad2: %s, Quad3: %s, Quad4 %s" % (quad1, quad2, quad3, quad4))



    #the direction that will be returned
    returnDirection = 0



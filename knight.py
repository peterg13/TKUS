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
    if not unit.location.is_in_garrison() and not unit.location.is_in_space():
        d = getMoveDirection()

        #if the knight can move towards the center it will, otherwise it will choose a random direction
        if gc.is_move_ready(unit.id) and gc.can_move(unit.id, d):
            gc.move_robot(unit.id, d)
        else:
            # pick a random direction:
            d = random.choice(directions)
            if gc.is_move_ready(unit.id) and gc.can_move(unit.id, d):
                gc.move_robot(unit.id, d)
    

#current idea for knight movement:
#figure out how many of our non-knight units are in each quadrant.  Have the knights move to the quadrant with the least friendly units.
#once in that quadrant they can move randomly
def getMoveDirection():
    quads = [0, 0, 0, 0] #quads[0] = quadrant 1, quads[1] = quadrant 2, etc

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

    #loops through and counts how many units are in each quadrant
    for myUnit in gc.my_units():
        #if a unit is in space, in the garrison, or is a knight it will skip them
        if not myUnit.location.is_in_garrison() and not myUnit.location.is_in_space() and myUnit.unit_type != bc.UnitType.Knight:
            x = myUnit.location.map_location().x
            y = myUnit.location.map_location().y
            if x < mapWidth/2:
                if y < mapHeight/2:
                    quads[2] += 1
                else:
                    quads[1] += 1
            else:
                if y < mapHeight/2:
                    quads[3] += 1
                else:
                    quads[0] += 1

    #gets the population of the smallest populated quadrant.  Then sees if there are other quadrants with the same number and puts it into a list.
    #if so it chooses a random quadrant from the list
    leastPopQuadNum = min(quads)
    smallestQuads = []
    for i in range (0, len(quads)):
        if leastPopQuadNum == quads[i]:
            smallestQuads.append(i)
    
    moveToQuad = smallestQuads[random.randint(0, len(smallestQuads) - 1)]

    #creates a newmapLocation which will be the center of the quadrant we need to go to
    quadCenter = bc.MapLocation(unit.location.map_location().planet, 0, 0)

    #sets the center of the quadrants coords
    if moveToQuad == 0:
        quadCenter.x = int(mapWidth - mapWidth/4)
        quadCenter.y = int(mapHeight - mapHeight/4)
    elif moveToQuad == 1:
        quadCenter.x = int(mapWidth/4)
        quadCenter.y = int(mapHeight - mapHeight/4)
    elif moveToQuad == 2:
        quadCenter.x = int(mapWidth)
        quadCenter.y = int(mapHeight/4)
    else:
        quadCenter.x = int(mapWidth - mapWidth/4)
        quadCenter.y = int(mapHeight/4)

    returnDirection = unit.location.map_location().direction_to(quadCenter)
    
    return returnDirection



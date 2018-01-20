import battlecode as bc
# This will handle everything that rockets need to do



def handleRocket(unit, gc, persistentMap):
    # print('trying to launch a rocket to marks', bc.MapLocation(bc.Planet.Mars, 0, 0))

    # if the rocket is on earth
    rocketLoc = unit.location.map_location()
    newLocation = 'no location found'

    if rocketLoc.planet == bc.Planet.Earth:
    	for y in range(len(persistentMap.marsMap)):
            for x in range(len(persistentMap.marsMap[0])):
                if persistentMap.marsMap[x][y].passable:
                    newLocation = bc.MapLocation(bc.Planet.Mars, x, y)

    if gc.can_launch_rocket(unit.id, newLocation):
        gc.launch_rocket(unit.id, newLocation)
        print('Rocket Launched!')
    
    return
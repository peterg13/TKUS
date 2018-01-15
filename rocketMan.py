
# This will handle everything that rockets need to do



def handleRocket(unit, gc, bc):
    # print('trying to launch a rocket to marks', bc.MapLocation(bc.Planet.Mars, 0, 0))
    if gc.can_launch_rocket(unit.id, bc.MapLocation(bc.Planet.Mars, 0, 0)):
        gc.launch_rocket(unit.id, bc.MapLocation(bc.Planet.Mars, 0, 0))
        print('Rocket Launched!')
    
    return
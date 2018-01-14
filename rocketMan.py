
# This will handle everything that rockets need to do

# 1. Find a location to launch the rocket to
# 2. Something about garrisoning units?
# 3. Launch ze rocket !!!!!!!!!
# 4. Try to land the rocket 
# gc = bc.GameController()

def handleRocket(unit, gc, bc):
    # print('trying to launch a rocket to marks', bc.MapLocation(bc.Planet.Mars, 0, 0))
    if gc.can_launch_rocket(unit.id, bc.MapLocation(bc.Planet.Mars, 0, 0)):
        gc.launch_rocket(unit.id, bc.MapLocation(bc.Planet.Mars, 0, 0))
        print('Rocket Launched!')
    
    return
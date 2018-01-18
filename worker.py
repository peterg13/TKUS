import battlecode as bc
import random

#Rocket Rules
#1. Rockets are the number one priority if you can build a rocket do it
#2. Do not build a rocket while there is a rocket that is still being garrisoned //if we have a shit ton of units this might need to be changed
#3. Rockets can hold up to 8 units
#4. Once a rocket has been launched you can build another rocket. 

#Factory Rules
#1. Factories are always the first thing to build
#2. Each team gets 10 Karbonite per round and a factory takes 5 rounds to build a robot. Unless we're mining deposits we should never have more than 3 factories
maxRockets = 1
maxFactories = 3
maxRangers = 5
maxKnights = 10

currentRockets = 0
currentFactories = 0
harvestTotal = 0
targetFcound = False
targetLoc = 0

directions = list(bc.Direction)

def workerLogic(unit, gc, unitCounter, persistentMap):
    global currentRockets
    global currentFactories
    global distance
    global harvestTotal
    global targetFcound
    global targetLoc


    d = random.choice(directions)

    #creates a rocket
    if len(unitCounter.currentRockets) < maxRockets:
        #checks if you have enough karbonite and can built in the given location
        if gc.karbonite() > bc.UnitType.Rocket.blueprint_cost() and gc.can_blueprint(unit.id, bc.UnitType.Rocket, d):
            gc.blueprint(unit.id, bc.UnitType.Rocket, d)
            currentRockets += 1
    

    #create a factory
    if len(unitCounter.currentFactories) < maxFactories:
        #checks if you have enough karbonite and can built in the given location
        if gc.karbonite() > bc.UnitType.Factory.blueprint_cost() and gc.can_blueprint(unit.id, bc.UnitType.Factory, d):
            gc.blueprint(unit.id, bc.UnitType.Factory, d)
            currentFactories += 1

    # replicate a worker only if there are more factories than workers
    if len(unitCounter.currentWorkers) < len(unitCounter.currentFactories):
        if gc.can_replicate(unit.id, d):
            gc.replicate(unit.id, d)

            print(unit.id, "replicated")

    #build nearby factories
    workerLoc = unit.location
    workerMapLoc = workerLoc.map_location()
    if workerLoc.is_on_map():
        #gets all nearby factories at the given location
        nearbyUnits = gc.sense_nearby_units_by_type(workerLoc.map_location(), 2, bc.UnitType.Factory)
        for nearbyFactory in nearbyUnits:
            if gc.can_build(unit.id, nearbyFactory.id):
                gc.build(unit.id, nearbyFactory.id)
                continue

    # check if there is any karbonite around to harvest
    for i in directions:
        direction = directions[i]
        if gc.can_harvest(unit.id, direction):
            gc.harvest(unit.id, direction)
            harvestMapLoc = workerMapLoc.add(direction)
            persistentMap.updateKarbonite(harvestMapLoc, unit.worker_harvest_amount())
            harvestTotal += unit.worker_harvest_amount()
            # print(harvestTotal, " harvested!")
            break

    # if you don't have anything better to do. Move.
    if gc.is_move_ready(unit.id):
        # if a factory needs to be built move towards it
        if not targetFcound:
            for i in range(len(unitCounter.currentFactories)):
                thisFactory = unitCounter.currentFactories[i]
                if(thisFactory.health<thisFactory.max_health):
                    print("targeting Factory")
                    targetLoc = thisFactory.location.map_location()
                    targetFcound = True
                    
        # locate closest karbonite deposit that still has karbonite in it
        
            
            if workerMapLoc.planet == bc.Planet.Earth and not targetFcound:
                print("looking for karbonite")
                distance = 100000
                for y in range(len(persistentMap.earthMap)):
                    for x in range(len(persistentMap.earthMap[0])):
                        #check if there is karbonite at that location
                        if persistentMap.earthMap[x][y].karbonite > 0 and persistentMap.earthMap[x][y].passable:
                            #get distance to that location
                            currentLoc = bc.MapLocation(bc.Planet.Earth, x, y)
                            newDistance = workerMapLoc.distance_squared_to(currentLoc)
                            # print(newDistance, distance)
                            if newDistance < distance:
                                distance = newDistance
                                targetLoc = currentLoc
                                targetFcound = True
                                print("targeting karbonite at", targetLoc)

        elif targetFcound:
            direction = workerMapLoc.direction_to(targetLoc)
            if persistentMap.earthMap[targetLoc.x][targetLoc.y].karbonite or not persistentMap.earthMap[targetLoc.x][targetLoc.y].passable< 0:
                targetFcound = False
        
            
            if gc.can_move(unit.id, direction):
                print("moving towards", direction)
                gc.move_robot(unit.id, direction) 

            elif gc.can_move(unit.id, d):
                print("moving randomly")
                gc.move_robot(unit.id, d)
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

directions = list(bc.Direction)

def workerLogic(unit, gc, unitCounter):
    global currentRockets
    global currentFactories


    #print(currentRockets)
    d = random.choice(directions)

    #creates a rocket
    if unitCounter.currentRockets < maxRockets:
        #checks if you have enough karbonite and can built in the given location
        if gc.karbonite() > bc.UnitType.Rocket.blueprint_cost() and gc.can_blueprint(unit.id, bc.UnitType.Rocket, d):
            gc.blueprint(unit.id, bc.UnitType.Rocket, d)
            currentRockets += 1
    

    #create a factory
    if unitCounter.currentFactories < maxFactories:
        #checks if you have enough karbonite and can built in the given location
        if gc.karbonite() > bc.UnitType.Factory.blueprint_cost() and gc.can_blueprint(unit.id, bc.UnitType.Factory, d):
            gc.blueprint(unit.id, bc.UnitType.Factory, d)
            currentFactories += 1

    # replicate a worker only if there are more factories than workers
    if unitCounter.currentWorkers < unitCounter.currentFactories:
        if gc.can_replicate(unit.id, d):
            gc.replicate(unit.id, d)

            print(unit.id, "replicated")

    #build nearby factories
    workerLoc = unit.location
    if workerLoc.is_on_map():
        #gets all nearby factories at the given location
        nearbyUnits = gc.sense_nearby_units_by_type(workerLoc.map_location(), 2, bc.UnitType.Factory)
        for nearbyFactory in nearbyUnits:
            if gc.can_build(unit.id, nearbyFactory.id):
                gc.build(unit.id, nearbyFactory.id)
                # print('built a factory!')
                # move onto the next nearby unit
                continue

    # check if there is any karbonite around to harvest
    for d in directions:
        direction = directions[d]
        if gc.can_harvest(unit.id, direction):
            gc.harvest(unit.id, direction)
            # print("karbonite harvested!")
            break

    # if you don't have anything better to do. Move.
    if gc.is_move_ready(unit.id) and gc.can_move(unit.id, d):
        gc.move_robot(unit.id, d)
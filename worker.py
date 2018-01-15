import battlecode as bc
import random

directions = list(bc.Direction)

def workerLogic(unit, gc):
    #create a factory
    d = random.choice(directions)
    if gc.karbonite() > bc.UnitType.Factory.blueprint_cost() and gc.can_blueprint(unit.id, bc.UnitType.Factory, d):
        gc.blueprint(unit.id, bc.UnitType.Factory, d)

    #build nearby factories
    workerLoc = unit.location
    if workerLoc.is_on_map():
        nearbyUnits = gc.sense_nearby_units(workerLoc.map_location(), 2)
        for otherUnits in nearbyUnits:
            if gc.can_build(unit.id, otherUnits.id):
                gc.build(unit.id, otherUnits.id)
                print('built a factory!')
                # move onto the next nearby unit
                continue
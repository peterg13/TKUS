import battlecode as bc
import random

directions = list(bc.Direction)



def factoryLogic(unit, gc, unitCounter, persistentMap):
    currentResearch = gc.research_info()
    garrison = unit.structure_garrison()
    if len(garrison) > 0:
        d = random.choice(directions)
        if gc.can_unload(unit.id, d):
            print('unloaded a', unit.unit_type)
            gc.unload(unit.id, d)
    # build rangers
    elif currentResearch.get_level(bc.UnitType.Ranger) > 1 and gc.can_produce_robot(unit.id, bc.UnitType.Ranger) and len(unitCounter.currentRangers) < 5:
        try:
            gc.produce_robot(unit.id, bc.UnitType.Ranger)
            print("produced a ranger")
        except:
            print('Error producing a ranger :/')
    # build knights
    # elif gc.can_produce_robot(unit.id, bc.UnitType.Knight):
    #     try:
    #         gc.produce_robot(unit.id, bc.UnitType.Knight)
    #         print('produced a knight!')
    #     except:
    #         print('Error producing a knight')
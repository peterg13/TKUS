import battlecode as bc
import random

directions = list(bc.Direction)



def factoryLogic(unit, gc, unitCounter):
    currentResearch = gc.research_info()
    #print("factory turn")
    garrison = unit.structure_garrison()
    if len(garrison) > 0:
        d = random.choice(directions)
        if gc.can_unload(unit.id, d):
            print('unloaded a knight!')
            gc.unload(unit.id, d)
    # build rangers
    elif currentResearch.get_level(bc.UnitType.Ranger) > 1 and gc.can_produce_robot(unit.id, bc.UnitType.Ranger) and unitCounter.currentRangers < 5:
        try:
            gc.produce_robot(unit.id, bc.UnitType.Ranger)
            print("produced a ranger")
        except:
            print('Error producing a ranger :/')
    # build knights
    elif gc.can_produce_robot(unit.id, bc.UnitType.Knight):
        try:
            gc.produce_robot(unit.id, bc.UnitType.Knight)
            print('produced a knight!')
        except:
            print('Error producing a knight')
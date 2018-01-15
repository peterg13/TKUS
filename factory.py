import battlecode as bc
import random

directions = list(bc.Direction)

def factoryLogic(unit, gc):
    garrison = unit.structure_garrison()
    if len(garrison) > 0:
        d = random.choice(directions)
        if gc.can_unload(unit.id, d):
            print('unloaded a knight!')
            gc.unload(unit.id, d)
        elif gc.can_produce_robot(unit.id, bc.UnitType.Knight):
            try:
                gc.produce_robot(unit.id, bc.UnitType.Knight)
                print('produced a knight!')
            except:
                print('Error producing a knight')
import battlecode as bc 
import random

targetLocationX = 19
targetLocationY = 19

def rangerLogic(unit, gc):
	if targetLocationX and targetLocationY:
		target = bc.MapLocation(bc.Planet.Earth, targetLocationX, targetLocationY)
		# print('is snipe ready?: ', gc.is_begin_snipe_ready(unit.id))
		# print('can begin snipe?: ', gc.can_begin_snipe(unit.id, target))
		# print('ranger research level: ', gc.research_info().get_level(bc.UnitType.Ranger))
		if gc.is_begin_snipe_ready(unit.id) and gc.can_begin_snipe(unit.id, target):
			gc.begin_snipe(unit.id, target)
			# print(unit.id, "is sniping")
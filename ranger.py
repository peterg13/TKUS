import battlecode as bc 
import random

targetLocationX = 5
targetLocationY = 19

def rangerLogic(unit, gc):
	global targetLocationX
	global targetLocationY

	if targetLocationX and targetLocationY:
		target = bc.MapLocation(bc.Planet.Earth, targetLocationX, targetLocationY)
		# print('is snipe ready?: ', gc.is_begin_snipe_ready(unit.id))
		# print('can begin snipe?: ', gc.can_begin_snipe(unit.id, target))
		# print('ranger research level: ', gc.research_info().get_level(bc.UnitType.Ranger))
		# print(unit.ranger_is_sniping())
		if unit.ranger_is_sniping():
			print(unit.id, "snipe countdown: ", unit.ranger_countdown())

		if gc.is_begin_snipe_ready(unit.id) and gc.can_begin_snipe(unit.id, target):
			if unit.ability_heat() < 10 and unit.ability_cooldown()>199:
				if unit.ranger_is_sniping():
					print(unit.id, "snipe countdown: ", unit.ranger_countdown())
				else:
					gc.begin_snipe(unit.id, target)
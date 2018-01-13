import battlecode as bc
import random
import sys
import traceback
import rocketMan
import mapArray

print("pystarting")

# A GameController is the main type that you talk to the game with.
# Its constructor will connect to a running game.
gc = bc.GameController()
directions = list(bc.Direction)

print("pystarted")

# It's a good idea to try to keep your bots deterministic, to make debugging easier.
# determinism isn't required, but it means that the same things will happen in every thing you run,
# aside from turns taking slightly different amounts of time due to noise.
random.seed(6137)

# let's start off with some research!
# we can queue as much as we want.
gc.queue_research(bc.UnitType.Rocket)
gc.queue_research(bc.UnitType.Worker)
gc.queue_research(bc.UnitType.Knight)

my_team = gc.team()



# earth = gc.starting_map(bc.Planet.Earth)
# mars = gc.starting_map(bc.Planet.Mars)

mapArray.initializeMapArrays(gc,bc)

# earthMap = [[0 for x in range(20)] for y in range(20)]





while True:
    # We only support Python 3, which means brackets around print()
    print('pyround:', gc.round())
    print('karboynite total:',gc.karbonite())
    
    # frequent try/catches are a good idea
    try:

        # walk through our units:
        for unit in gc.my_units():

            if gc.is_move_ready(unit.id):
                # print(unit.unit_type, "is move ready!")
                # print(unit.location)
                #  check which directions are moveable
                for x in range (0, len(directions)):
                    if gc.can_move(unit.id, directions[x]):
                        b = 3 + 2
                    else:
                        y = x
                # let's try to crawl around the edge of the map
                # let's first move to the bottom left corner




    except Exception as e:
        print('Error:', e)
        # use this to show where the error was
        traceback.print_exc()

    # send the actions we've performed, and wait for our next turn.
    gc.next_turn()

    # these lines are not strictly necessary, but it helps make the logs make more sense.
    # it forces everything we've written this turn to be written to the manager.
    sys.stdout.flush()
    sys.stderr.flush()
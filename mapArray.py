




class locData(object):
	pass

def initializeMapArrays(gc, bc):

	earth = gc.starting_map(bc.Planet.Earth)
	mars = gc.starting_map(bc.Planet.Mars)

	earthMap = [[0 for x in range(earth.width)] for y in range(earth.height)]
	marsMap = [[0 for x in range(mars.width)] for y in range(mars.height)]
	# Earth
	for j in range(earth.width):
	    for i in range(earth.height):
	        thisLocation = bc.MapLocation(bc.Planet.Earth, i, j)
	        newData = locData()
	        newData.x = i
	        newData.y = j
	        newData.unit = 'unknown'
	        newData.team = 'neutral'

	        if earth.is_passable_terrain_at(thisLocation):
	            newData.passable = True
	        else:
	            newData.passable = False 

	       	earthMap[i][j] = newData
	        print(earthMap[i][j])


	# Mars
	for d in range(mars.width):
	    for c in range(mars.height):
	        thisLocation = bc.MapLocation(bc.Planet.Mars, c, d)
	        newData = locData
	        newData.x = c
	        newData.y = d
	        newData.unit = 'unknown'
	        newData.team = 'neutral'

	        try:

	        	if earth.is_passable_terrain_at(thisLocation):
	        		newData.passable = True
	        	else:
	        		newData.passable = False 

	        except Exception:
	        	newData.passable = False

	       	marsMap[c][d] = newData
	        print(marsMap[c][d])
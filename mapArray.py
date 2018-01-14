




class Data(object):
	pass


class smartMap:
	earthMap = 0
	marsMap = 0
	
	def __init__(self,gc,bc):
		self.gc = gc
		self.bc = bc	

	def initializeMapArrays():

		earth = self.gc.starting_map(self.bc.Planet.Earth)
		mars = self.gc.starting_map(self.bc.Planet.Mars)

		self.earthMap = [[0 for x in range(earth.width)] for y in range(earth.height)]
		self.marsMap = [[0 for x in range(mars.width)] for y in range(mars.height)]

	def addToMap(data):
		if(data.planet == 'earth'):
			self.earthMap[data.x][data.y] = data 
		if(data.planet == 'mars'):
			self.marsMap[data.x][data.y] = data

	def removeFromMap(data):
		if(data.planet == 'earth'):
			self.earthMap[data.x][data.y] = 0
		if(data.planet == 'mars'):
			self.marsMap[data.x][data.y] = 0

	def getMapData(mapLocation):
		if mapLocation.planet == bc.Planet.Earth:
			return self.earthMap[mapLocation.x][mapLocation.y]

		if mapLocation.planet == bc.Planet.Earth:
			return self.marsMap[mapLocation.x][mapLocation.y]
	# Earth
	# for j in range(earth.width):
	#     for i in range(earth.height):
	#         thisLocation = bc.MapLocation(bc.Planet.Earth, i, j)
	#         newData = locData()
	#         newData.x = i
	#         newData.y = j
	#         newData.unit = 'unknown'
	#         newData.team = 'neutral'

	#         if earth.is_passable_terrain_at(thisLocation):
	#             newData.passable = True
	#         else:
	#             newData.passable = False 

	#        	earthMap[i][j] = newData
	#         print(earthMap[i][j])


	# # Mars
	# for d in range(mars.width):
	#     for c in range(mars.height):
	#         thisLocation = bc.MapLocation(bc.Planet.Mars, c, d)
	#         newData = locData
	#         newData.x = c
	#         newData.y = d
	#         newData.unit = 'unknown'
	#         newData.team = 'neutral'

	#         try:

	#         	if earth.is_passable_terrain_at(thisLocation):
	#         		newData.passable = True
	#         	else:
	#         		newData.passable = False 

	#         except Exception:
	#         	newData.passable = False

	#        	marsMap[c][d] = newData
	#         print(marsMap[c][d])
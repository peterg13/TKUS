class Data(object):
	pass


class smartMap:
	earthMap = 0
	marsMap = 0
	
	def __init__(self,gc,bc):
		self.gc = gc
		self.bc = bc

		#downloading earth information
	def initializeMapArrays(self):

		earth = self.gc.starting_map(self.bc.Planet.Earth)
		mars = self.gc.starting_map(self.bc.Planet.Mars)

		self.earthMap = [[0 for x in range(earth.width)] for y in range(earth.height)]
		self.marsMap = [[0 for x in range(mars.width)] for y in range(mars.height)]

		# download karbonite and passable terrain locations for Earth

		for j in range(earth.width):
		    for i in range(earth.height):
		        thisLocation = self.bc.MapLocation(self.bc.Planet.Earth, i, j)
		        newData = Data()
		        newData.x = i
		        newData.y = j
		        newData.unit = 'unknown'
		        newData.team = 'neutral'
		        newData.passable = True
		        newData.karbonite = 0

		        if earth.is_passable_terrain_at(thisLocation):
		            newData.passable = True
		            if earth.initial_karbonite_at(thisLocation):
		            	newData.karbonite = earth.initial_karbonite_at(thisLocation)
		            	# print(earth.initial_karbonite_at(thisLocation), " Karbonite found!")
		            else:
		            	newData.karbonite = 0
		        else:
		            newData.passable = False 
		            newData.karbonite = 0

		       	self.earthMap[i][j] = newData

		# download karbonite and passable terrain locations for Mars
		for d in range(mars.width):
		    for c in range(mars.height):
		        thisLocation = self.bc.MapLocation(self.bc.Planet.Mars, c, d)
		        newData = Data()
		        newData.x = c
		        newData.y = d
		        newData.unit = 'unknown'
		        newData.team = 'neutral'

	        	if mars.is_passable_terrain_at(thisLocation):
	        		newData.passable = True
	        		if mars.initial_karbonite_at(thisLocation):
			        	newData.karbonite = mars.initial_karbonite_at(thisLocation)
			        	# print(mars.initial_karbonite_at(thisLocation), " Karbonite found!")
			        else:
			        	newData.karbonite = 0
	        	else:
	        		newData.passable = False
	        		newData.karbonite = 0

		       	self.marsMap[c][d] = newData

	def addToMap(self, data):
		if(data.planet == 'earth'):
			self.earthMap[data.x][data.y] = data 
		if(data.planet == 'mars'):
			self.marsMap[data.x][data.y] = data

	def removeFromMap(self, data):
		if(data.planet == 'earth'):
			self.earthMap[data.x][data.y] = 0
		if(data.planet == 'mars'):
			self.marsMap[data.x][data.y] = 0

	def getMapData(self, mapLocation):
		if mapLocation.planet == bc.Planet.Earth:
			return self.earthMap[mapLocation.x][mapLocation.y]

		if mapLocation.planet == bc.Planet.Mars:
			return self.marsMap[mapLocation.x][mapLocation.y]
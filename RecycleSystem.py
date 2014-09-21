""" $Id: RecycleSystem.py 2363 2010-08-10 04:37:07Z opus $
RecycleSystems
"""

import ItemSupply

class RecycleSystem( ItemSupply.ItemSupply ) :
	""" Intermediate system for recycling """
	secondsPerUpdate = 1
	unitsPerUpdate = 1
	energyPerUnit = None
	def __init__( self ) :
		super( RecycleSystem, self ).__init__()
		self.supply = 0
		self.setUpdateInterval( self.secondsPerUpdate )
		self.setUpdateCallback( self.processWaste )
	def setMaxSupply( self, maxSupply ) :
		self.maxSupply = maxSupply
	def addWaste( self, amount ) :
		return self.addSupply( amount )
	def processWaste( self ) :
		raise NotImplementedError
	
class FoodRecycleSystem( RecycleSystem ) :
	""" FoodRecycleSystem recycles used to new, also only one of these """
	__single = None
	foodSupply = None
	energyPerUnit = 1					# value TBD.
	def __new__( classtype, *args, **kwargs ) :
		if classtype != type( classtype.__single ) :
			classtype.__single = object.__new__( classtype, *args, **kwargs )
		return classtype.__single
	def __init__( self ) :
		super( FoodRecycleSystem, self ).__init__()
		self.setMaxSupply( 100000 ) # this is in kg
	def setFoodSupply( self, foodSupply ) :
		self.foodSupply = foodSupply
	def processWaste( self ) :
		""" Process Waste, 1 unit, get the energy, move from this supply to the food supply
		TODO: deescribe how to handle functional and operational status values here
			  maybe do a random number to lower the odds of processing
		"""
		if self.supply > 0 :
			status = self.foodSupply.getStatus()
			if status[0] < status[1] :	
				self.energySupply.getEnergy( self.energyPerUnit * self.unitsPerUpdate )
				self.supply -= self.unitsPerUpdate
				self.foodSupply.addFood(self.unitsPerUpdate)		
class OxygenRecycleSystem( RecycleSystem ) :
	""" OxygenRecycleSystem recycles used to new. """
	__single = None
	unitsPerUpdate = 11000				# 11574 does the entire supply in 24 hours
	energyPerUnit = 1					
	oxygenSupply = None
	def __init__( self ) :
		super( OxygenRecycleSystem, self ).__init__()
		self.setMaxSupply( 1000000000 )	# this is in m^3
	def setOxygenSupply( self, oxygenSupply ) :
		self.oxygenSupply = oxygenSupply
	def processWaste( self ) :
		""" Process Waste, and move from this supply to the oxygen supply
		TODO:  stuff
		"""
		if self.supply > 0 :
			status = self.oxygenSupply.getStatus()
			unitDiff = status[1] - status[0]
			if unitDiff > 0 :
				units = min( unitDiff, self.unitsPerUpdate, self.supply )
				self.energySupply.getEnergy( self.energyPerUnit * units )
				self.supply -= units
				self.oxygenSupply.addOxygen( units )
class WaterRecycleSystem( RecycleSystem ) :
	""" WaterRecycleSystem recycles used to new. """
	unitsPerUpdate = 2					# 2 liters per second
	energyPerUnit = 10					# TBD value
	waterSupply = None
	def __init__( self ) :
		super( WaterRecycleSystem, self ).__init__()
		self.setMaxSupply( 1000000000 ) # this is in liters
	def setWaterSupply ( self, waterSupply ) :
		self.waterSupply = waterSupply
	def processWaste( self ) :
		""" Process Waste, and move from this supply to the water supply
		TODO: describe how to handle the functional and operational status values here
		"""
		if self.supply > 0 :
			status = self.waterSupply.getStatus()
			unitDiff = status[1] - status[0]
			if unitDiff > 0 :
				units = min( unitDiff, self.unitsPerUpdate, self.supply )
				self.energySupply.getEnergy( self.energyPerUnit * units )
				self.supply -= units
				self.waterSupply.addWater( units )



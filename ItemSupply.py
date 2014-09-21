""" $Id: ItemSupply.py 2364 2010-08-10 04:37:40Z opus $

	ItemSupply module provides the base class for providing a supply system
	
"""

import StarShipSystem

class ItemSupply( StarShipSystem.StarShipSystem ) :
	maxSupply = None
	supply = None
	distributionEnergy = None
	distrubutionPerUnit = None
	storageEnergy = None
	storagePerUnit = None
	getAccum = 0

	def __init__( self, maxSupply=None, supply=None ) :
		super( ItemSupply, self ).__init__()
		if ( maxSupply and supply ) :
			if supply > maxSupply :
				supply = maxSupply
			self.maxSupply = maxSupply
			self.supply = supply
	def getStatus( self ) :
		""" get the status of this supply """
		return ( self.supply, self.maxSupply )
	def getSupply( self, amount ) :
		""" return an amount of the supply, and decrement the supply value """
		if (self.supply is not None) :
			valOut = min( self.supply, amount )
			self.supply -= valOut
			self.getAccum += valOut
			return valOut
		return None
	def addSupply( self, amount ) :
		if (self.supply is not None) and (self.maxSupply is not None) :
			emptyVal = self.maxSupply - self.supply
			valOut = min( emptyVal, amount )
			self.supply += valOut
			return valOut
		return None
#	def tick( self ) :
#		super.tick()

class FoodSupply( ItemSupply ) :
	""" FoodSupply is the supply for the entire ship.  Units are kg.
	This is a singleton holding this data """
	__single = None
	nutrition = None			# 0 - 100%
	pollution = None			# 0 - 100%
	def __new__( classtype, *args, **kwargs ) :
		if classtype != type( classtype.__single ) :
			classtype.__single = object.__new__( classtype, *args, **kwargs )
		return classtype.__single
	def __init__( self, maxSupply=100000, supply=50000 ) :
		super( FoodSupply, self ).__init__( maxSupply, supply )
		self.nutrition = 100
		self.pollution = 100
		self.distributionEnergy = 2
		self.distributionPerUnit = 1000
		self.storageEnergy = 1
		self.storagePerUnit = 10000
	def getFood( self, amount ) :
		""" return an amount of food from the supply, and decrement the supply """
		return self.getSupply( amount )
	def addFood( self, amount ) :
		return self.addSupply( amount )
class OxygenSupply( ItemSupply ) :
	""" OxygenSupply is the supply for the entire ship. Units are m^3.
	This is a singleton holding this data """
	__single = None
	pollution = None
	def __new__( classtype, *args, **kwargs ) :
		if classtype != type( classtype.__single ) :
			classtype.__single = object.__new__( classtype, *args, **kwargs )
		return classtype.__single
	def __init__( self, maxSupply=1000000000, supply=500000000 ) :
		super( OxygenSupply, self ).__init__( maxSupply, supply )
		self.pollution = 100
	def getOxygen( self, amount ) :
		""" return an amount of oxygen from the supply, and decrement the supply """
		return self.getSupply( amount )
	def addOxygen( self, amount ) :
		return self.addSupply( amount )
class WaterSupply( ItemSupply ) :
	""" WaterSupply is the supply for the entire ship. Units are liters.
	This is a singleton holding this data """
	__single = None
	pollution = None			# 0 - 100%
	def __new__( classtype, *args, **kwargs ) :
		if classtype != type( classtype.__single ) :
			classtype.__single = object.__new__( classtype, *args, **kwargs )
		return classtype.__single
	def __init__( self, maxSupply=1000000000, supply=500000000 ) :
		super( WaterSupply, self ).__init__( maxSupply, supply )
		self.pollution = 100
	def getWater( self, amount ) :
		""" return an amount of water from the supply, and decrement the supply """
		return self.getSupply( amount )
	def addWater( self, amount ) :
		return self.addSupply( amount )

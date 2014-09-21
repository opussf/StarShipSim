""" $Id: LifeSupport.py 2378 2010-08-10 04:49:26Z opus $

	LifeSupport module.  This module provides life support.
	
"""

import StarShipSystem
import ItemSupply
import RecycleSystem

class OxygenDistributionSystem( StarShipSystem.StarShipSystem ) :
	pass

class WaterDistributionSystem( StarShipSystem.StarShipSystem ) :
	pass

class LifeSupport( object ) :
	""" Life support systems """
	food,oxygen,water = 0,1,2			# list indexes
	itemSupplys = None					# The supplys of items (Water, Oxygen, Food)
	itemRecycles = None					# THe recycle of items
	itemObjects = None					# all the items to call ticks for
	
	def __init__(self):
		super( LifeSupport,self ).__init__()
		self.itemSupplys = []
		self.itemSupplys.append( ItemSupply.FoodSupply() )
		self.itemSupplys.append( ItemSupply.OxygenSupply() )
		self.itemSupplys.append( ItemSupply.WaterSupply() )
		self.itemRecycles = []
		self.itemRecycles.append( RecycleSystem.FoodRecycleSystem() )
		self.itemRecycles.append( RecycleSystem.OxygenRecycleSystem() )
		self.itemRecycles.append( RecycleSystem.WaterRecycleSystem() )
		self.itemObjects = []
		self.itemObjects.extend( self.itemSupplys )
		self.itemObjects.extend( self.itemRecycles )
	def getFoodSupply( self ) :
		""" return the foodSupply system """
		return self.itemSupplys[ self.food ]
	def getOxygenSupply( self ) :
		""" return the oxygenSupply system """
		return self.itemSupplys[ self.oxygen ]
	def getWaterSupply( self ) :
		""" return the waterSupply system """
		return self.itemSupplys[ self.water ]
	def getFoodRecycle( self ) :
		""" return the foodRecycle system """
		return self.itemRecycles[ self.food ]
	def getOxygenRecycle( self ) :
		""" return the oxygenRecycle """
		return self.itemRecycles[ self.oxygen ]
	def getWaterRecycle( self ) :
		""" return the waterRecycle """
		return self.itemRecycles[ self.water ]
	def tick( self ) :
		""" Ticks for all the objects here - might get removed? """
		for item in self.itemObjects:
			item.tick()

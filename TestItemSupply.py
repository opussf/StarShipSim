#!/usr/bin/env python
""" $Id: TestItemSupply.py 2367 2010-08-10 04:40:27Z opus $
"""
from ItemSupply import *

import unittest
class testItemSupply( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ) :
		self.s = ItemSupply( )
	def test_Supply_getStatus( self ) :
		self.assertEqual( self.s.getStatus(), (None, None) )
		self.s.maxSupply = 4000
		self.s.supply = 0
		self.assertEqual( self.s.getStatus(), (0, 4000) )
	def test_Supply_addSupply( self ) :
		self.assertEqual( self.s.addSupply(100), None )
		self.s.maxSupply = 4000
		self.s.supply = 0
		self.assertEqual( self.s.addSupply(100), 100 )
		self.assertEqual( self.s.addSupply(4000), 3900 )
		self.assertEqual( self.s.getStatus(), (4000, 4000) )
	def test_Supply_getSupply( self ) :
		self.assertEqual( self.s.getSupply(100), None )
		self.s.maxSupply = 4000
		self.s.supply = 100
		self.assertEqual( self.s.getSupply(100), 100 )
		self.assertEqual( self.s.getSupply(100), 0 )
		self.assertEqual( self.s.getStatus(), (0, 4000) )
		self.assertEqual( self.s.getAccum, 100 )
	def test_Supply_setEnergySupply( self ) :
		self.s.setEnergySupply( self.supplyTest() )
		self.failUnless( self.s.energySupply )
	def test_Supply_tick( self ) :
		self.s.tick()
	
	
class testFoodSupply( unittest.TestCase ) :
	def setUp( self ) :
		self.fs = FoodSupply()
	def test_FoodSupply_getFood( self ) :
		""" Test that food can be obtained from the supply """
		self.fs.supply = 200
		self.assertEqual( self.fs.getFood(10), 10 )
		self.assertEqual( self.fs.getFood(90), 90 )
		self.assertEqual( self.fs.getFood(200), 100 )
	def test_FoodSupply_addFood( self ) :
		""" Test that food can be added to the supply """
		self.assertEqual( self.fs.getStatus(), (50000, 100000) )
		self.assertEqual( self.fs.addFood( 1000 ), 1000 ) 
		self.assertEqual( self.fs.getStatus(), (51000, 100000) )
		self.assertEqual( self.fs.addFood( 48000 ), 48000 )
		self.assertEqual( self.fs.addFood( 2000 ), 1000 )
		self.assertEqual( self.fs.getStatus(), (100000, 100000) )
		self.assertEqual( self.fs.addFood( 1000 ), 0, "Should not be able to add more food than can hold" ) 
		self.assertEqual( self.fs.getStatus(), (100000, 100000) )
	def test_FoodSupply_2InstancesAreSame( self ) :
		""" Test that 2 instances pull from the same resource """
		fs2 = FoodSupply()
		self.assertEqual( self.fs.getStatus(), (50000, 100000) )
		self.assertEqual( fs2.getStatus(), (50000, 100000) )
		self.assertEqual( fs2.getFood( 1000 ), 1000 )
		self.assertEqual( self.fs.getStatus(), (49000, 100000) )

class testOxygenSupply( unittest.TestCase ) :
	def setUp( self ) :
		self.os = OxygenSupply()
	def test_OxygenSupply_getFood( self ) :
		""" Test that oxygen can be obtained from the supply """
		self.os.supply = 200
		self.assertEqual( self.os.getOxygen(10), 10 )
		self.assertEqual( self.os.getOxygen(90), 90 )
		self.assertEqual( self.os.getOxygen(200), 100 )
	def test_OxygenSupply_addFood( self ) :
		""" Test that oxygen can be added to the supply """
		self.assertEqual( self.os.getStatus(), (500000000, 1000000000) )
		self.assertEqual( self.os.addOxygen( 1000 ), 1000 ) 
		self.assertEqual( self.os.getStatus(), (500001000, 1000000000) )
		self.assertEqual( self.os.addOxygen(   499998000 ), 499998000 )
		self.assertEqual( self.os.addOxygen( 2000 ), 1000 )
		self.assertEqual( self.os.getStatus(), (1000000000, 1000000000) )
		self.assertEqual( self.os.addOxygen( 1000 ), 0, "Should not be able to add more food than can hold" ) 
		self.assertEqual( self.os.getStatus(), (1000000000, 1000000000) )
	def test_OxygenSupply_2InstancesAreSame( self ) :
		""" Test that 2 instances pull from the same resource """
		os2 = OxygenSupply()
		self.assertEqual( self.os.getStatus(), (500000000, 1000000000) )
		self.assertEqual( os2.getStatus(), (500000000, 1000000000) )
		self.assertEqual( os2.getOxygen( 1000 ), 1000 )
		self.assertEqual( self.os.getStatus(), (499999000, 1000000000) )


class testWaterSupply( unittest.TestCase ) :
	def setUp( self ) :
		self.ws = WaterSupply()
		self.maxWater = 1000000000
	def test_WaterSupply_getFood( self ) :
		""" Test that food can be obtained from the supply """
		self.ws.supply = 200
		self.assertEqual( self.ws.getWater(10), 10 )
		self.assertEqual( self.ws.getWater(90), 90 )
		self.assertEqual( self.ws.getWater(200), 100 )
	def test_WaterSupply_addFood( self ) :
		""" Test that food can be added to the supply """
		self.assertEqual( self.ws.getStatus(), (500000000, self.maxWater) )
		self.assertEqual( self.ws.addWater( 1000 ), 1000 ) 
		self.assertEqual( self.ws.getStatus(), (500001000, self.maxWater) )
		self.assertEqual( self.ws.addWater( 499998000 ), 499998000 )
		self.assertEqual( self.ws.addWater( 2000 ), 1000 )
		self.assertEqual( self.ws.getStatus(), (self.maxWater, self.maxWater) )
		self.assertEqual( self.ws.addWater( 1000 ), 0, "Should not be able to add more food than can hold" ) 
		self.assertEqual( self.ws.getStatus(), (self.maxWater, self.maxWater) )
	def test_WaterSupply_2InstancesAreSame( self ) :
		""" Test that 2 instances pull from the same resource """
		ws2 = WaterSupply()
		self.assertEqual( self.ws.getStatus(), (500000000, self.maxWater) )
		self.assertEqual( ws2.getStatus(), (500000000, self.maxWater) )
		self.assertEqual( ws2.getWater( 1000 ), 1000 )
		self.assertEqual( self.ws.getStatus(), (499999000, self.maxWater) )
		
if __name__ == "__main__" :	
	unittest.main()
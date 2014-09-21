#!/usr/bin/env python
""" $Id: TestRecycleSystem.py 2362 2010-08-10 04:36:20Z opus $
"""
from RecycleSystem import *

import unittest
class testRecycleSystem( unittest.TestCase ) :
	class supplyTest( object ) :
		""" Test stub for Energy Supply """
		def getEnergy( self, amount ) :
			return amount
	def setUp( self ) :
		self.rs = RecycleSystem()
		self.rs.setFunctionalStatus( 100 )
		self.rs.setOperationalStatus( 100 )
		self.rs.setReliabilityFactor( 100 )
		self.rs.setEnergySupply( self.supplyTest() )
	def test_recycleSystem_getStatus( self ) :
		""" test that the getStatus works as expected """
		self.assertEqual( self.rs.getStatus(), (0, None) )
	def test_RecycleSystem_setMaxSupply( self ) :
		""" test that setMaxSupply exists, and sets the value """
		self.rs.setMaxSupply( 2000 )
		self.assertEqual( self.rs.getStatus(), (0, 2000) )
	def test_RecycleSystem_addWaste( self ) :
		""" test that addWaste exists, and sets the value """
		self.rs.setMaxSupply( 2000 )
		self.assertEqual( self.rs.addWaste( 1000 ), 1000 )
		self.assertEqual( self.rs.addWaste( 1500 ), 1000 )
		self.assertEqual( self.rs.getStatus(), (2000, 2000) )
	def test_RecycleSystem_processWaste( self ) :
		""" test that this raises an exception """
		try :
			self.rs.processWaste()
		except NotImplementedError :
			pass
		except :
			self.fail("Unknown error happened")
class testFoodRecycleSystem( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ) :
		self.frs = FoodRecycleSystem()
		self.frs.setFunctionalStatus( 100 )
		self.frs.setOperationalStatus( 100 )
		self.frs.setReliabilityFactor( 100 )
		self.frs.setEnergySupply( self.supplyTest() )
		self.frs.setFoodSupply( ItemSupply.FoodSupply() )
	def test_FoodRecycleSystem_setFoodSuppy( self ) :
		self.failUnless( self.frs.foodSupply, "This should be set" )
		self.assertEqual( self.frs.foodSupply.getStatus(), (50000, 100000) )
	def test_FoodRecycleSystem_tick( self ) :
		self.assertEqual( self.frs.foodSupply.getStatus(), (50000, 100000) )
		self.frs.addWaste( 1 )
		self.assertEqual( self.frs.getStatus(), (1, 100000) )
		while( self.frs.getStatus()[0] > 0 ) :
			self.frs.tick()
		self.assertEqual( self.frs.foodSupply.getStatus(), (50001, 100000) )
	def test_FoodRecycleSystem_tick2( self ) :
		self.frs.foodSupply.addFood(50000)
		self.assertEqual( self.frs.foodSupply.getStatus(), (100000, 100000) )
		self.frs.addWaste( 1 )
		while( self.frs.getStatus()[0] > 0 ) :
			self.frs.tick()
			if self.frs.elapsed.seconds > 3 :
				break
		self.failIf( self.frs.elapsed.seconds < 3, "It should not have processed anything" )


class testOxygenRecycleSystem( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ) :
		self.ors = OxygenRecycleSystem()
		self.ors.setFunctionalStatus( 100 )
		self.ors.setOperationalStatus( 100 )
		self.ors.setReliabilityFactor( 100 )
		self.ors.setEnergySupply( self.supplyTest() )
		self.ors.setOxygenSupply( ItemSupply.OxygenSupply() )
	def test_OxygenRecycleSystem_getStatus( self ) :
		""" get the status of the recycleSystem """
		self.assertEqual( self.ors.getStatus(), (0, 1000000000) )
	def test_OxygenRecycleSystem_addWaste( self ) :
		""" add waste to the system """
		self.assertEqual( self.ors.getStatus(), (0, 1000000000) )
		self.assertEqual( self.ors.addWaste( 900000000 ), 900000000 )
		self.assertEqual( self.ors.getStatus(), (900000000, 1000000000) )
		self.assertEqual( self.ors.addWaste( 200000000 ), 100000000 )
		self.assertEqual( self.ors.getStatus(), (1000000000, 1000000000) )
	def test_OxygenRecycleSystem_setFoodSuppy( self ) :
		self.failUnless( self.ors.oxygenSupply, "This should be set" )
		self.assertEqual( self.ors.oxygenSupply.getStatus(), (500000000, 1000000000) )
	def test_OxygenRecycleSystem_tick( self ) :
		self.assertEqual( self.ors.oxygenSupply.getStatus(), (500000000, 1000000000) )
		self.ors.addWaste( 1 )
		self.assertEqual( self.ors.getStatus(), (1, 1000000000) )
		while( self.ors.getStatus()[0] > 0 ) :
			self.ors.tick()
		self.assertEqual( self.ors.oxygenSupply.getStatus(), (500000001, 1000000000) )
	def test_OxygenRecycleSystem_tick2( self ) :
		self.ors.oxygenSupply.addOxygen( 500000000 )
		self.assertEqual( self.ors.oxygenSupply.getStatus(), (1000000000, 1000000000) )
		self.ors.addWaste( 1 )
		while( self.ors.getStatus()[0] > 0 ) :
			self.ors.tick()
			if self.ors.elapsed.seconds > 3 :
				break
		self.failIf( self.ors.elapsed.seconds < 3, "It should not have processed anything %s" % (self.ors.getStatus(),) )

class testWaterRecycleSystem( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ) :
		self.wrs = WaterRecycleSystem()
		self.wrs.setFunctionalStatus( 100 )
		self.wrs.setOperationalStatus( 100 )
		self.wrs.setReliabilityFactor( 100 )
		self.wrs.setEnergySupply( self.supplyTest() )
		self.wrs.setWaterSupply( ItemSupply.WaterSupply() )
	def test_WaterRecycleSystem_getStatus( self ) :
		""" get the status of the recycleSystem """
		self.assertEqual( self.wrs.getStatus(), (0, 1000000000) )
	def test_WaterRecycleSystem_addWaste( self ) :
		""" add waste to the system """
		self.assertEqual( self.wrs.getStatus(), (0, 1000000000) )
		self.assertEqual( self.wrs.addWaste( 900000000 ), 900000000 )
		self.assertEqual( self.wrs.getStatus(), (900000000, 1000000000) )
		self.assertEqual( self.wrs.addWaste( 200000000 ), 100000000 )
		self.assertEqual( self.wrs.getStatus(), (1000000000, 1000000000) )
	def test_WaterRecycleSystem_setFoodSuppy( self ) :
		self.failUnless( self.wrs.waterSupply, "This should be set" )
		self.assertEqual( self.wrs.waterSupply.getStatus(), (500000000, 1000000000) )
	def test_WaterRecycleSystem_tick( self ) :
		self.assertEqual( self.wrs.waterSupply.getStatus(), (500000000, 1000000000) )
		self.wrs.addWaste( 1 )
		self.assertEqual( self.wrs.getStatus(), (1, 1000000000) )
		while( self.wrs.getStatus()[0] > 0 ) :
			self.wrs.tick()
		self.assertEqual( self.wrs.waterSupply.getStatus(), (500000001, 1000000000) )
	def test_WaterRecycleSystem_tick2( self ) :
		self.wrs.waterSupply.addWater( 500000000 )
		self.assertEqual( self.wrs.waterSupply.getStatus(), (1000000000, 1000000000) )
		self.wrs.addWaste( 1 )
		while( self.wrs.getStatus()[0] > 0 ) :
			self.wrs.tick()
			if self.wrs.elapsed.seconds > 3 :
				break
		self.failIf( self.wrs.elapsed.seconds < 3, "It should not have processed anything %s" % (self.wrs.getStatus(),) )


if __name__ == "__main__" :
	unittest.main()
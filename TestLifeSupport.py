#!/usr/bin/env python
""" $Id: TestLifeSupport.py 2369 2010-08-10 04:42:29Z opus $
"""
from LifeSupport import *

import unittest
class testLifeSupport( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp(self):
		self.ls = LifeSupport()
		st = self.supplyTest()
		for iS in self.ls.itemObjects :
			iS.setFunctionalStatus( 100 )
			iS.setOperationalStatus( 100 )
			iS.setReliabilityFactor( 100 )
			iS.setEnergySupply( st )	
#		def test_LifeSupport_InitialVals(self):
#			self.ls = LifeSupport()
#			self.assertEqual(self.ls.getFunctionalStatus(),0,"FunctionalStatus should start as 0")
#			self.assertEqual(self.ls.getReliabilityFactor(),0,"ReliabilityFactor should start as 0")
#			self.assertEqual(self.ls.getOperationalStatus(),0,"OperationalStatus should start as 0")
#		def test_LifeSupport_hasEnergySupply( self ) :
#			""" test that the energySupply is registered to this """
#			self.failUnless( self.ls.energySupply )
	def test_LifeSupport_hasWaterSupply( self ) :
		""" test that a waterSupply is hooked up """
		self.failUnless( self.ls.getWaterSupply() )
	def test_LifeSupport_hasFoodSupply( self ) :
		""" test that a foodSupply is hooked up """
		self.failUnless( self.ls.getFoodSupply() )
	def test_LifeSupport_hasOxygenSupply( self ) :
		""" test that an oxygenSupply is hooked up """
		self.failUnless( self.ls.getOxygenSupply() )
	def test_LifeSupport_hasWaterRecycle( self ) :
		""" test that a waterRecycle is hooked up """
		self.failUnless( self.ls.getWaterRecycle() )
	def test_LifeSupport_hasFoodRecycle( self ) :
		""" test that a foodRecycle is hooked up """
		self.failUnless( self.ls.getFoodRecycle() )
	def test_LifeSupport_hasOxygenRecycle( self ) :
		""" test that an oxygenRecycle is hooked up """
		self.failUnless( self.ls.getOxygenRecycle() )
	def test_LifeSupport_hasTick( self ) :
		self.ls.tick()


class testOxygenDistributionSystem( unittest.TestCase ) :
	def test_OxygenDistributionSystem( self ) :
		pass
class testWaterDistributionSystem( unittest.TestCase ) :
	def test_WaterDistributionSystem( self ) :
		pass
	
if __name__ == "__main__":
	unittest.main()
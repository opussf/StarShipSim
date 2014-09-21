#!/usr/bin/env python
""" $Id: TestEnergyConduit.py 2369 2010-08-10 04:42:29Z opus $ 
"""
from EnergyConduit import *

import unittest
class testEnergyConduit(unittest.TestCase):
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp(self):
		self.ec = EnergyConduit()
		self.ec.setSupply ( self.supplyTest() )
		self.ec.setFunctionalStatus( 100 )
		self.ec.setOperationalStatus( 100 )
		self.ec.setReliabilityFactor( 100 )
	def test_EnergyConduit_InitialVals(self):
		self.ec = EnergyConduit()
		self.assertEqual ( self.ec.getFunctionalStatus(), 0, "FunctionalStatus should start as 0" )
		self.assertEqual ( self.ec.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0" )
		self.assertEqual ( self.ec.getOperationalStatus(), 0, "OperationalStatus should start as 0" )
	def test_EnergyConduit_setSupply ( self ) :
		self.ec = EnergyConduit()
		self.assertEqual ( self.ec.energySupply, None, "Should not be inited" )
		es = EnergySupply.EnergySupply()
		self.ec.setSupply ( es )
		self.assertNotEqual ( self.ec.energySupply, None, "Should be set" )
	def test_EnergyConduit_getEnergy_01( self ) :
		""" Test that it raises the correct exception with no supply set """
		self.ec = EnergyConduit()
		es = EnergySupply.EnergySupply()
		try :
			self.ec.getEnergy ( 1 )
		except NoSupply :
			pass
		try :
			self.ec.setSupply( es )
			self.ec.getEnergy ( 1 )
		except NoSupply :
			fail( "Should not get exception" )
	def test_EnergyConduit_getEnergy_02( self ) :
		""" Test that it moves energy """
		self.assertEqual( self.ec.getEnergy( 10 ), 10, "Should return the requested value" )
	def test_EnergyConduit_getEnergy_03( self ) :
		""" Test that tick clears the energyAskedAccum counter """
		self.ec.tick()
		self.ec.getEnergy(100)
		while( self.ec.elapsed.seconds < 2 ) :
			self.ec.tick()
		self.assertEqual( self.ec.energyAskedAccum, 0 )
	def test_EnergyConduit_getEnergy_04( self ) :
		""" Test that damage is caused each second if asked for too much energy """
		self.ec2 = EnergyConduit()
		self.ec2.setSupply( self.supplyTest() )
		self.ec2.setFunctionalStatus( 100 )
		self.ec2.setOperationalStatus( 100 )
		self.ec2.setReliabilityFactor( 100 )
		self.ec3 = EnergyConduit()
		self.ec3.setSupply( self.supplyTest() )
		self.ec3.setFunctionalStatus( 100 )
		self.ec3.setOperationalStatus( 100 )
		self.ec3.setReliabilityFactor( 100 )
		self.ec.tick()
		self.ec2.tick()
		self.ec3.tick()
		self.ec.getEnergy( 600 )
		self.ec2.getEnergy( 1000 )
		self.ec3.getEnergy( 2000 )
		while( self.ec.elapsed.seconds < 2 ) :
			self.ec.tick()
			self.ec2.tick()
			self.ec3.tick()
		self.assertEqual( self.ec.getFunctionalStatus(), 99 )
		self.assertEqual( self.ec2.getFunctionalStatus(), 75 )
		self.assertEqual( self.ec3.getFunctionalStatus(), 0 )
	def test_EnergyConduit_getEnergy_FunctionalStatus( self ) :
		""" Test that the Functional status correctly affects the results """
		self.ec.setFunctionalStatus( 50 )
		self.assertEqual( self.ec.getEnergy( 100 ), 50, "Should return reduced value" )
		self.ec.setFunctionalStatus( 10 )
		self.assertEqual( self.ec.getEnergy( 100 ), 10, "Should return reduced value" )
		self.ec.setFunctionalStatus( 1 )
		self.assertEqual( self.ec.getEnergy( 99 ), 0, "Should return reduced value" )
	def test_EnergyConduit_getEnergy_OperationalStatus( self ) :
		""" Test that the Operational status correctly affects the results """
		self.ec.setOperationalStatus( 50 )
		self.assertEqual( self.ec.getEnergy( 100 ), 50, "Should return reduced value" )
			
if __name__ == "__main__" :		
	unittest.main()
#!/usr/bin/env python
""" $Id: TestEnergyGeneration.py 2369 2010-08-10 04:42:29Z opus $
"""
from EnergyGeneration import *

import unittest
class testEnergyGeneration( unittest.TestCase ) :
	def setUp(self):
		self.es = EnergyGeneration()
		self.es.setFunctionalStatus( 100 )
		self.es.setOperationalStatus( 100 )
		self.es.setReliabilityFactor( 100 )

	def test_EnergyGeneration_InitialVals(self):
		""" Basic initial vals are inherited and set to 0 """
		self.es = EnergyGeneration()
		self.assertEqual(self.es.getFunctionalStatus(),0,"FunctionalStatus should start as 0")
		self.assertEqual(self.es.getReliabilityFactor(),0,"ReliabilityFactor should start as 0")
		self.assertEqual(self.es.getOperationalStatus(),0,"OperationalStatus should start as 0")

	def test_EnergyGneration_setReactiveMass( self ) :
		""" Reactive Mass is set """
		self.es.setMaxReactiveMass(100)
		self.assertEqual(self.es.setReactiveMass(100), 100, "Should have returned the set value")
		self.assertEqual( self.es.getReactiveMass(), (100, 100), "Should be full")
		self.assertEqual( self.es.setReactiveMass(-5), 0, "Negative value should set it to 0")
		self.assertEqual( self.es.getReactiveMass(), (0, 0), "Should be empty")
		self.assertEqual( self.es.setReactiveMass(105), 100, "Should not be able to set above the max")
		self.assertEqual( self.es.getReactiveMass(), (100, 100), "Should be full")
	
	def test_changeReactiveMass( self ) :
		self.es.setMaxReactiveMass( 100 )
		self.es.setReactiveMass( 75 )
		self.assertEqual( self.es.changeReactiveMass (-5), -5, "Should return the amount taken")
		self.assertEqual( self.es.getReactiveMass() , (70, 70), "Should have properly changed the amount of mass available")
		self.assertEqual( self.es.changeReactiveMass (-75), -70, "Should return the amount removed")
		self.assertEqual( self.es.changeReactiveMass (110), 100, "Should ")
		
	def test_getReactiveMass( self ) :
		self.assertEqual( self.es.getReactiveMass(), (0,0), "Should return 0, no error")
		self.es.setMaxReactiveMass(100)
		self.assertEqual( self.es.getReactiveMass(), (0,0), "Should return 0, no error")
		self.es.setReactiveMass (50)
		self.assertEqual( self.es.getReactiveMass(), (50,50), "Should return (50,0.5)")
		
	def test_getEnergy( self ) :
		import time
		self.es.setOperationalStatus ( 1 )
		self.es.setMaxReactiveMass(16330)
		self.es.setReactiveMass(16330)
		self.es.tick()
		time.sleep( 1 )
		self.es.tick()
		self.assertEqual( self.es.getEnergy(-1), 0, "Should return 0")
		self.assertEqual( self.es.getEnergy(1), 1 )
		self.assertFalse( self.es.getEnergy(8) == 8, "This should fail, as this cannot be obtained")
		self.assertFalse( self.es.getEnergy(1000000000) == 1000000000, "This should fail, as this cannot be obtained")
		
	def test_getStatus( self ) :
		import time
		self.es.setOperationalStatus ( 100 )
		self.es.setMaxReactiveMass(16330)
		self.es.setReactiveMass(150)
		self.es.tick()
		for lcv in range( 2 ) :
			time.sleep(1)
			self.es.tick()
		self.assertEqual( self.es.getStatus(), (1522,45700) )
		self.es.getEnergy ( 1000 )
		self.assertEqual( self.es.getStatus(), (522,45700), "Invalid ammount of energy after getting some")
		
	def test_EG_tick( self ) :
		self.es.tick()
		
if __name__ == "__main__" :	
	unittest.main()
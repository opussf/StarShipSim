#!/usr/bin/env python
""" $Id: TestEnergySupply.py 2369 2010-08-10 04:42:29Z opus $
"""
from EnergySupply import *

import unittest
class testEnergySupply(unittest.TestCase):
	def setUp(self):
		self.eg = EnergyGeneration.EnergyGeneration()
		self.eg.setOperationalStatus( 100 )
		self.eg.setFunctionalStatus( 100 )
		self.eg.setReliabilityFactor( 100 )
		self.eg.setMaxReactiveMass( 16330 )
		self.eg.setReactiveMass( 16330 )
		self.es = EnergySupply()
		self.es.setEnergyGeneration( self.eg )
		self.es.setOperationalStatus( 100 )
		self.es.setFunctionalStatus( 100 )
		self.es.setReliabilityFactor( 100 ) 

	def test_EnergySupply_InitialVals(self):
		self.es = EnergySupply()
		self.assertEqual( self.es.getFunctionalStatus(), 0, "FunctionalStatus should start as 0" )
		self.assertEqual( self.es.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0" )
		self.assertEqual( self.es.getOperationalStatus(), 0, "OperationalStatus should start as 0" )
		
	def test_getStatus( self ) :
		self.es.quantity = 0
		self.assertEqual( self.es.getStatus(), (0, 2000000000),)
		while ( self.es.getStatus()[0] < 1 ) :	# repeat until we have some energy to work with
			self.es.tick()
			self.eg.tick()
			#print self.es.getStatus(), self.es.energyGeneration.getReactiveMass(), self.es.energyGeneration.getStatus()
		self.assertEqual( self.es.getStatus(), (761, 2000000000), )
		self.assertEqual( self.es.getStatus(), (761, 2000000000), "Small amount of energy" )
		
	def test_getEnergy( self ) :
		while ( self.es.getStatus()[0] < 1 ) :	# repeat until we have some energy to work with
			self.es.tick()
		startEnergy = self.es.getStatus()[0]
		gotEnergy = self.es.getEnergy( 100 )
		self.assertEqual( gotEnergy, 100, "Should have gotten 100 units of energy" )
		self.assertEqual( self.es.getStatus()[0], startEnergy-100, "100 units should have been removed")
			
if __name__ == "__main__":		
	unittest.main()
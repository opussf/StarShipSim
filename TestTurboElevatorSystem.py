#!/usr/bin/env python
""" $Id: TestTurboElevatorSystem.py 2369 2010-08-10 04:42:29Z opus $
"""
from TurboElevatorSystem import *

import unittest
class testTurboElevatorSystem( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ) :
		self.tes = TurboElevatorSystem()
		self.tes.setFunctionalStatus( 100 )
		self.tes.setOperationalStatus( 100 )
		self.tes.setReliabilityFactor( 100 )
	def tearDown( self ):
		self.tes = None
	def test_TurboElevatorSystem_InitialVals(self):
		self.assertEqual ( self.tes.getFunctionalStatus(), 100, "FunctionalStatus should start as 0" )
		self.assertEqual ( self.tes.getReliabilityFactor(), 100, "ReliabilityFactor should start as 0" )
		self.assertEqual ( self.tes.getOperationalStatus(), 100, "OperationalStatus should start as 0" )
	def test_TurboElevatorSystem_tick( self ):
		self.tes.tick()
	def test_TurboElevatorSystem_addItem( self ):
		import MassObject
		obj = MassObject.MassObject()
		self.tes.addObject( obj )
		self.assertEqual( len(self.tes.cargo), 1 )
	def test_TurboElevatorSystem_addPerson( self ):
		import Person
		p = Person.Person()
		self.tes.addObject( p )
		self.assertEqual( len(self.tes.cargo), 1 )	

if __name__ == "__main__" :
	unittest.main()
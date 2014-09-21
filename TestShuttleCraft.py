#!/usr/bin/env python
""" $Id: TestShuttleCraft.py 2369 2010-08-10 04:42:29Z opus $
"""
from ShuttleCraft import *

import unittest
class testShittleCraft( unittest.TestCase ):
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ):
		self.sc = ShuttleCraft()
	def test_ShuttleCraft_InitialVals(self):
		self.assertEqual( self.sc.getFunctionalStatus(), 0, "FunctionalStatus should start as 0" )
		self.assertEqual( self.sc.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0" )
		self.assertEqual( self.sc.getOperationalStatus(), 0, "OperationalStatus should start as 0" )
	def test_ShuttleCraft_addItem( self ):
		import MassObject
		obj = MassObject.MassObject()
		self.sc.addObject( obj )
		self.assertEqual( len(self.sc.cargo), 1 )
	def test_ShuttleCraft_addPerson( self ):
		import Person
		p = Person.Person()
		self.sc.addObject( p )
		self.assertEqual( len(self.sc.cargo), 1 )	
		
if __name__=="__main__" :
	unittest.main()

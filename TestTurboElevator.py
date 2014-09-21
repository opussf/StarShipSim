#!/usr/bin/env python
""" $Id: TestTurboElevator.py 2369 2010-08-10 04:42:29Z opus $
"""
from TurboElevator import *

import unittest
class testTurboElevator( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp( self ) :
		self.te = TurboElevator()
		self.te.setFunctionalStatus( 100 )
		self.te.setOperationalStatus( 100 )
		self.te.setReliabilityFactor( 100 )
	def test_TurboElevator_InitialVals(self):
		self.assertEqual ( self.te.getFunctionalStatus(), 100, "FunctionalStatus should start as 0" )
		self.assertEqual ( self.te.getReliabilityFactor(), 100, "ReliabilityFactor should start as 0" )
		self.assertEqual ( self.te.getOperationalStatus(), 100, "OperationalStatus should start as 0" )

	
if __name__ == "__main__" :
	unittest.main()
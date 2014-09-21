#!/usr/bin/env python
""" $Id: TestWarpEngine.py 2369 2010-08-10 04:42:29Z opus $
"""
from WarpEngine import *
	
import unittest
class testWarpEngine( unittest.TestCase ):
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ):
			return amount
	def setUp( self ):
		self.we = WarpEngine()
	def test_WaroEngine_InitialVals_baseclass(self):
		self.assertEqual( self.we.getFunctionalStatus(), 0, "FunctionalStatus should start as 0" )
		self.assertEqual( self.we.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0" )
		self.assertEqual( self.we.getOperationalStatus(), 0, "OperationalStatus should start as 0" )

if __name__=="__main__":	
	unittest.main()
#!/usr/bin/env python
""" $Id: TestImpulseEngine.py 2369 2010-08-10 04:42:29Z opus $
"""
from ImpulseEngine import *

import unittest
class testImpulseEngine(unittest.TestCase):
	class supplyTest ( object ):
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ):
			return amount
	def setUp( self ):
		self.ie = ImpulseEngine()
	def test_ImpulseEngine_InitialVals_baseclass(self):
		self.assertEqual( self.ie.getFunctionalStatus(), 0, "FunctionalStatus should start as 0" )
		self.assertEqual( self.ie.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0" )
		self.assertEqual( self.ie.getOperationalStatus(), 0, "OperationalStatus should start as 0" )
	
if __name__=="__main__" :
	unittest.main()
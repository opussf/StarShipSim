#!/usr/bin/env python
""" $Id: TestTransporter.py 2369 2010-08-10 04:42:29Z opus $
"""
from Transporter import *

import unittest
class testTransporter( unittest.TestCase ):
	class supplyTest ( object ):
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ):
			return amount
	def setUp( self ):
		self.T = Transporter()
		self.T.setFunctionalStatus( 100 )
		self.T.setOperationalStatus( 100 )
		self.T.setReliabilityFactor( 100 ) 
	def test_Transporter_InitialVals_baseclass(self):
		self.assertEqual( self.T.getFunctionalStatus(), 100, "FunctionalStatus should start as 0" )
		self.assertEqual( self.T.getReliabilityFactor(), 100, "ReliabilityFactor should start as 0" )
		self.assertEqual( self.T.getOperationalStatus(), 100, "OperationalStatus should start as 0" )
	def test_Transporter_SetSupply( self ) :
		self.T.setSupply( self.supplyTest() )
	def test_Transporter_getBufferStatus( self ):
		""" Get the status of the buffer """
		self.assertEqual( self.T.getBufferStatus(), 0 )
	def test_Transporter_activate( self ):
		""" test activation of Transporter """
		pass
			
if __name__ == "__main__":	
	unittest.main()
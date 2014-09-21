#!/usr/bin/env python
""" $Id: TestShield.py 2369 2010-08-10 04:42:29Z opus $
"""
from Shield import *

import unittest
class testShield ( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp ( self ) :
		self.s = Shield ()
		self.s.setFunctionalStatus( 100 )
		self.s.setOperationalStatus( 100 )
		self.s.setReliabilityFactor( 100 )
	def test_Shield_InitialVals_baseclass( self ) :
		""" Inherited attributes from the base """
		self.s = Shield()
		self.assertEqual( self.s.getFunctionalStatus(), 0, "FunctionalStatus should start as 0")
		self.assertEqual( self.s.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0")
		self.assertEqual( self.s.getOperationalStatus(), 0, "OperationalStatus should start as 0")
	def test_Shield_setSupply( self ) :
		self.s.setSupply( self.supplyTest() )
		self.failIfEqual( self.s.energySupply, None )
	def test_Shield_getStatus_FunctionalStatusEffect( self ) :
		""" Tests the effect of the functionalStatus on the getStatus() method """
		me = self.s.getMaxEnergy()
		self.assertEqual( self.s.getStatus(), (0,me) )
		self.s.setFunctionalStatus( 90 )
		self.assertEqual( self.s.getStatus(), (0,me*.9) )
		self.s.setFunctionalStatus( 50 )
		self.assertEqual( self.s.getStatus(), (0,me*.5) )
		self.s.setFunctionalStatus( 25 )
		self.assertEqual( self.s.getStatus(), (0,me*.25) )
		self.s.setFunctionalStatus( 0 )
		self.assertEqual( self.s.getStatus(), (0,0), "Should be (0, 0)")
	def test_Shield_getStatus_OperationalStatusEffect( self ) :
		""" Tests the effect of the operationalStatus on the getStatus() method """
		me = self.s.getMaxEnergy()
		self.assertEqual( self.s.getStatus(), (0,me) )
		self.s.setOperationalStatus( 90 )
	def test_Shield_getStatus_FunAndOpStatusEffect( self ) :
		""" Tests the combined effects of Functional and Operational status """
		me = self.s.getMaxEnergy()
		self.assertEqual( self.s.getStatus(), (0,me) )
		self.s.setFunctionalStatus( 90 )
		self.s.setOperationalStatus( 90 )
		self.assertEqual( self.s.getStatus(), (0,me*.9) )
		self.s.setOperationalStatus( 50 )
		self.assertEqual( self.s.getStatus(), (0,me*.9) )
	def test_Shield_takeDamage( self ) :
		""" Tests how the shield system works with taking damage """
		self.s.energy = 100
		self.assertEqual( self.s.takeDamage( 50 ), 0, "Should not let any damage by" )
		self.assertEqual( self.s.getStatus()[0], 50, "Should show this amount of damage" )
		self.assertEqual( self.s.takeDamage( 75 ), 25, "Should show that damage got past" )
		self.assertEqual( self.s.getStatus()[0], 0, "Should show this amount of damage" )
		try :
			self.s.takeDamage( -5 )
		except ValueError :
			pass	# any other exception is in error
	def test_Shield_tick ( self ) :
		status = self.s.getStatus
		self.s.setEnergySupply( self.supplyTest() )
		self.s.setReliabilityFactor( 0 )
		#pv = 0
		while status()[0] < 10 :
			self.s.tick()
			#st = self.s.getStatus()
			#if status()[0] != pv :
				#pv = status()[0]
				#print status(), "=", (status()[0] * 100)/status()[1], "%"
		self.assertEqual( status()[0], 60, "Shield energy charge should be 60, got: %i" % status()[0] )

if __name__ == "__main__" :					
	unittest.main()

#!/usr/bin/env python
""" $Id: TestMedical.py 2369 2010-08-10 04:42:29Z opus $
"""
from Medical import *
import Person

import unittest
class testMedical( unittest.TestCase ) :
	class supplyTest ( object ) :
		""" Test stub for Energy Supply """
		def __init__( self ):
			self.energyUsed = 0
		def getEnergy ( self, amount ) :
			self.energyUsed += amount
			return amount
	def setUp( self ) :
		self.m = Medical()
		self.m.setFunctionalStatus( 100 )
		self.m.setOperationalStatus( 100 )
		self.m.setReliabilityFactor( 100 )
		self.m.setSupply( self.supplyTest() )
	def test_Medical_InitialVals(self):
		m = Medical()
		self.assertEqual( m.getFunctionalStatus(), 0, "FunctionalStatus should start as 0" )
		self.assertEqual( m.getReliabilityFactor(), 0, "ReliabilityFactor should start as 0" )
		self.assertEqual( m.getOperationalStatus(), 0, "OperationalStatus should start as 0" )
	def test_Medical_SetSupply( self ):
		self.m.setSupply( self.supplyTest() )
	def test_Medical_getCapacity( self ):
		self.assertEqual( self.m.getCapacity() , 10 )
	def test_Medical_getAvailable( self ):
		self.assertEqual( self.m.getAvailable(), 10 )
	def test_Medical_addPerson_Healthy( self ):
		p = Person.Person()
		self.m.addPerson( p )
		self.assertEqual( self.m.getAvailable(), 9 )
	def test_Medical_addPerson_UnHealthy( self ):
		p = Person.Person()
		p.setHealthStatus( 50 )    # Sick
		self.m.addPerson( p )
		self.assertEqual( self.m.getAvailable(), 9 )
	def test_Medical_addPerson_UnHealthy_moreThanAvailable( self ):
		people = [ Person.Person() for p in range(10) ]
		for p in people:
			p.setHealthStatus( 50 )    # Sick
			self.m.addPerson( p )
		self.assertEqual( self.m.getAvailable(), 0, "Should have 0 available" )
		p = Person.Person()
		p.setHealthStatus( 50 )    # Sick
		self.m.addPerson( p )
		self.assertEquals( len( self.m.getStatusReport()["standbyStatus"] ), 1 )
	def test_Medical_addPerson_UnHealthy_moreThanAvailable_triageWorks( self ):
		people = [ Person.Person() for p in range(10) ]
		val = 45
		for p in people:
			p.setHealthStatus( val )    # Sick
			self.m.addPerson( p )
			val += 5
		self.assertEqual( self.m.getAvailable(), 0, "Should have 0 available" )
		p = Person.Person()
		p.setHealthStatus( 25 )    # Sick
		self.m.addPerson( p )
		self.assertEquals( len( self.m.getStatusReport()["standbyStatus"] ), 1 )
		self.assertEquals( self.m.getStatusReport()["standbyStatus"][0].getHealthStatus(), 25 )
		self.m.tick()
		self.assertEquals( self.m.getStatusReport()["standbyStatus"][0].getHealthStatus(), 90 )
	def test_Medical_addPerson_Dead( self ):
		p = Person.Person()
		p.setHealthStatus( 0 )    # Dead
		self.m.addPerson( p )
		self.m.tick()
		self.assertEquals( len( self.m.getStatusReport()["deadStatus"] ), 1 )
	def test_Medical_getStatusReport_empty( self ):
		expectedResult = {"bedsAvailable":10, "bedsStatus":[]}
		actualResult = self.m.getStatusReport()
		for k in expectedResult.keys():
			self.assertEquals( actualResult[k], expectedResult[k] )
	def test_Medical_getStatusReport_1patient( self ):
		expectedResult = {"bedsAvailable":9}
		expectedPatientStatus = [50]
		p = Person.Person()
		p.setHealthStatus( 50 )    # Sick
		self.m.addPerson( p )
		actualResult = self.m.getStatusReport()
		for k in expectedResult.keys():
			self.assertEquals( actualResult[k], expectedResult[k] )
		self.assertEquals( len( actualResult["bedsStatus"] ), 1 )
	def test_Medical_getHealed_noneInMedical( self ):
		self.assertEquals( self.m.getHealed(), None )
	def test_Medical_getHealed_oneHealedPerson( self ):
		p = Person.Person()
		self.m.addPerson( p )
		self.m.tick()
		self.assertEqual( self.m.getHealed(), p )
	def test_Medical_getHealed_oneStillSickPerson( self ):
		p = Person.Person()
		p.setHealthStatus( 98 )
		self.m.addPerson( p )
		self.m.tick()
		self.assertEqual( self.m.getHealed(), None )
	def test_Medical_tick( self ):
		self.m.setEnergySupply( self.supplyTest() )
		self.m.tick()


if __name__ == "__main__":
	unittest.main()
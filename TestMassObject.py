#!/usr/bin/env python
""" $Id: TestMassObject.py 2355 2010-08-10 04:23:09Z opus $
"""
from MassObject import *

import unittest
class testMassObject( unittest.TestCase ) :
	def setUp( self ) :
		self.mo = MassObject()
	def test_MassObject_setMass_greaterThan0( self ):
		""" test that setMass does not throw an error """
		self.mo.setMass( 113 )
	def test_MassObject_setMass_lessThan0( self ):
		""" MassObject.setMass sets mass to 0 if <0 is given """
		self.mo.setMass( -1 )
		self.assertEquals( self.mo.getMass(), 0 )
	def test_MassObject_getMass_None( self ):
		""" MassObject.getMass returns None if not set """
		self.assertEquals( self.mo.getMass(), None )
	def test_MassObject_getMass_withAMassValue( self ):
		""" MassObject.getMass returns the proper value """
		self.mo.setMass( 113 )
		self.assertEquals( self.mo.getMass(), 113 )
	def test_MassObject_setDensity_greaterThan0( self ):
		""" MassObject.setDensity sets density """
		self.mo.setDensity( 1 )
	def test_MassObject_setDensity_lessThan0( self ):
		""" MassObject.setDensity sets density to 0 is <0 is given """
		self.mo.setDensity( -1 )
		self.assertEquals( self.mo.getDensity(), 0 )
	def test_MassObject_getDensity_None( self ):
		""" MassObject.getDensity returns None if not set """
		self.assertEquals( self.mo.getDensity(), None )
	def test_MassObject_getDensity_withAValue( self ):
		""" MassObject.getDensity returns the proper value """
		self.mo.setDensity( 1 )
		self.assertEquals( self.mo.getDensity(), 1 )
	def test_MassObject_getVolume_noData( self ):
		""" MassObject.getVolume should return None if no data was set """
		self.failIf( self.mo.getVolume() )
	def test_MassObject_getVolume_NoMass( self ):
		""" MassObject.getVolume should return None if no mass was set """
		self.mo.setDensity( 1 )
		self.failIf( self.mo.getVolume() )
	def test_MassObject_getVolume_noDensity( self ):
		""" MassObject.getVolume should return None if no density was set """
		self.mo.setMass( 113 )
		self.failIf( self.mo.getVolume() )
	def test_MassObject_getVolume_H2O( self ):
		""" MassObject.getVolume returns the proper volume """
		self.mo.setMass( 113 )
		self.mo.setDensity( 1 )    # water - g/cc
		self.assertEquals( self.mo.getVolume(), 113000 )
	def test_MassObject_getVolume_HG( self ):
		""" MassObject.getVolume returns the proper volume """
		self.mo.setMass( 113 )
		self.mo.setDensity( 11.35 )    # lead - g/cc
		self.assertAlmostEqual( self.mo.getVolume(), 9955 )
	def test_MassObject_hasTick( self ):
		self.mo.tick()
	def test_MassObject_hasLocation( self ):
		self.mo.location.getLocation()
	def test_MassObject_hasTrajectory( self ):
		pass
	

if __name__ == "__main__":			
	unittest.main()
#!/usr/bin/env python
""" $Id: TestLocation.py 2369 2010-08-10 04:42:29Z opus $
"""
from Location import *
import MassObject
import Coord

import unittest
class testLocation(unittest.TestCase):
	def setUp( self ):
		self.l = Location()
		self.mo = MassObject.MassObject()
	def test_Location_setLocation_absoluteWithNoReference( self ):
		self.l.setLocation( Coord.Coord(0,0,0) )
		self.assertEqual( self.l.coords, Coord.Coord(0,0,0) )
		self.failIf( self.l.reference )
	def test_Location_setLocation_relativeWithReference( self ):
		self.mo.location.setLocation( Coord.Coord(10,10,10) )
		self.l.setLocation( Coord.Coord(20,20,20), self.mo )
		self.assertEqual( self.l.coords, Coord.Coord(20,20,20) )
		self.assertEqual( self.l.reference, self.mo )
	def test_Location_setLocation_invalidReferenceObjectRaisesException( self ):
		self.assertRaises( TypeError, self.l.setLocation, Coord.Coord(0,0,0), int() )
	def test_Location_setLocation_NoneCoordsRaisesTypeError( self ):
		self.assertRaises( TypeError, self.l.setLocation, None )
	def test_Location_setLocation_3ValueTupleIsConvertedToCoord( self ):
		self.l.setLocation( (10,100,1000) )
		self.assert_( isinstance( self.l.coords, Coord.Coord ) )
	def test_Location_getLocation_invalidReferenceObjectRaisesException( self ):
		self.assertRaises( TypeError, self.l.getLocation, int() )
	def test_Location_getLocation_TakesTupleParameter( self ):
		self.l.setLocation( (10,100,1000) )
		print self.l.getLocation( (10,100,1000) )
	def test_Location_getLocation_TakesListParameter( self ):
		self.l.setLocation( (10,100,1000) )
		print self.l.getLocation( [10,100,1000] )
	def test_Location_getLocation_TakesCoordParameter( self ):
		self.l.setLocation( (10,100,1000) )
		print self.l.getLocation( Coord.Coord(10,100,1000) )
	def test_Location_getLocation_absoluteWithNoReference( self ):
		self.l.setLocation( Coord.Coord(0, 0, 0) )
		self.assertEqual( self.l.getLocation( ), Coord.Coord(0,0,0) )
	def test_Location_getLocation_absoluteWithSelfReference( self ):
		self.l.setLocation( Coord.Coord(10,20,30) )
		self.assertEqual( self.l.getLocation( self.mo), Coord.Coord(0,0,0) )
	def test_Location_getLocation_relativeWithNoReference( self ):
		self.mo.location.setLocation( Coord.Coord(0, 0, 0) )
		self.l.setLocation( Coord.Coord(10, 10, 10), self.mo )
		self.assertEqual( self.l.getLocation(), Coord.Coord(10,10,10) )
	def test_Location_getLocation_relativeWithOriginalReference( self ):
		self.mo.location.setLocation( Coord.Coord(0, 0, 0) )
		self.l.setLocation( Coord.Coord(10, 10, 10), self.mo )
		self.assertEqual( self.l.getLocation( self.mo ), Coord.Coord(10,10,10) )
	def test_Location_getLocation_relativeWithZeroReference( self ):
		self.mo.location.setLocation( Coord.Coord(0, 0, 0) )
		self.l.setLocation( Coord.Coord(10, 10, 10), self.mo )
		self.assertEqual( self.l.getLocation( Coord.Coord(0,0,0) ), Coord.Coord(10,10,10) )
	def test_Location_getLocation_relativeWithObjectLocationReference( self ):
		self.mo.location.setLocation( Coord.Coord(0, 0, 0) )
		self.l.setLocation( Coord.Coord(10, 10, 10), self.mo )
		self.assertEqual( self.l.getLocation( Coord.Coord(10,10,10) ), Coord.Coord(0,0,0) )
	def test_Location_getLocation_relativeReferenceObjectOffCenter( self ):
		self.mo.location.setLocation( Coord.Coord(-100, -100, -100) )
		self.l.setLocation( Coord.Coord(10, 10, 10), self.mo )
		self.assertEqual( self.l.getLocation( self.mo ), Coord.Coord(-90, -90, -90) )
	def test_Location_getLocation_relativeReferenceObjectXTranslate( self ):
		self.mo.location.setLocation( Coord.Coord( 10, 10, 10 ) )
		self.mo2 = MassObject.MassObject()
		self.mo2.location.setLocation( Coord.Coord( 110, 10, 10 ) )
		self.l.setLocation( (10, 0, 0 ), self.mo2 )
		self.assertEqual( self.l.getLocation( self.mo ), Coord.Coord(130, 0, 0) )
	def test_Location_getLocation_relativeReferenceObjectHasRelativeReferenceObject( self ):
		self.mo.location.setLocation( Coord.Coord(10, 10, 10) )
		self.mo2 = MassObject.MassObject()
		self.mo2.location.setLocation( Coord.Coord(20, 20, 20), self.mo )
		self.l.setLocation( Coord.Coord(40, 40, 40), self.mo2 )
		self.assertEqual( self.l.getLocation( Coord.Coord(0,0,0) ), Coord.Coord(70, 70, 70 ) )
	

if __name__=="__main__":
	unittest.main()

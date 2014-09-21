#!/usr/bin/env python
""" $Id: TestCoord.py 2369 2010-08-10 04:42:29Z opus $
"""
from Coord import *
import unittest

class testCoord( unittest.TestCase ) :
	def setUp( self ):
		self.c = Coord( (0,0,0) )
		self.x = Coord( (100, 0, 0) )
		self.y = Coord( (0, 100, 0) )
		self.xy = Coord( (100, 100, 0) )
		self.z = Coord( 0, 0, 100 )
		self.xyz = Coord( (100, 100, 100) )
		
	def test_Coord_initNoParameters( self ):
		self.assertRaises( ValueError, Coord )
	def test_Coord_initListParameter( self ):
		self.assertRaises( ValueError, Coord, [])
	def test_Coord_initNonTupleOrListParameter( self ):
		self.assertRaises( TypeError, Coord, 5)
	def test_Coord_init4TupleParameter( self ):
		self.assertRaises( ValueError, Coord, (1,2,3,4) )
	def test_Coord_init3Parameters( self ):
		self.c = Coord( 1,2,3 )
	def test_Coord_init4Parameters( self ):
		self.assertRaises( ValueError, Coord, 1,2,3,4 )
	def test_Coord_initLightSecond( self ):
		self.c = Coord( (299792458, 0, 0) )
	def test_Coord_initLightYear( self ):
		val = int( 299792458 * (60*60*24*364.24) )
		self.c = Coord( (val, 0, 0) )
	def test_Coord_initParsec( self ):
		val = 3.08568025 * pow(10,16)
		self.c = Coord( (val, 0, 0) )
	def test_Coord_initLotsOfLightYears( self ):
		val = int( 299792458 * (60*60*24*364.24) )
		val *= pow(10, 10000)
		self.c = Coord( (val, 0, 0) )
	def test_Coord_initDecimals( self ):
		cMinor = Coord( (0.5, 0.5, 0.5) )
	def test_Coord_distance_OtherInteger( self ):
		self.assertRaises( TypeError, self.c.distance, 5 )
	def test_Coord_distance_OtherList( self ):
		self.assertRaises( TypeError, self.c.distance, [100,100,100] )
	def test_Coord_distance_OtherTuple( self ):
		self.assertRaises( TypeError, self.c.distance, (100,100,100) )
	def test_Coord_distanceX( self ):
		self.assertEqual( self.c.distance( self.x ), 100 )
	def test_Coord_distanceY( self ):
		self.assertEqual( self.c.distance( self.y ), 100 )
	def test_Coord_distanceXY( self ):
		self.assertAlmostEqual( self.c.distance( self.xy ), 141.42, 2 )
	def test_Coord_distanceZ( self ):
		self.assertEqual( self.c.distance( self.z ), 100 )
	def test_Coord_distanceXYZ( self ):
		self.assertAlmostEqual( self.c.distance( self.xyz ), 173.21, 2 )
	def test_Coord_distanceXYZ_decimalVal01( self ):
		cMinor = Coord( (0.5, 0.5, 0.5) )
		self.assertAlmostEqual( self.c.distance( cMinor ), 0.8660, 4 )
	def test_Coord_distanceXYZ_decimalVal02( self ):
		cMinor = Coord( (-0.5, -0.5, -0.5) )
		self.assertAlmostEqual( self.c.distance( cMinor ), 0.8660, 4 )
	def test_Coord_addNonCoord_Interger( self ):
		self.assertRaises( TypeError, self.c.__add__, self.c, 100 )
	def test_Coord_addNonCoord_List( self ):
		self.assertRaises( TypeError, self.c.__add__, self.c, [100,100,100] )
	def test_Coord_addNonCoord_Tuple( self ):
		self.assertRaises( TypeError, self.c.__add__, self.c, (100,100,100) )
	def test_Coord_addX( self ):
		result = Coord( 100, 0, 0 )
		self.assertEqual( self.c + self.x, result )
	def test_Coord_addY( self ):
		result = Coord( 0, 100, 0 )
		self.assertEqual( self.c + self.y, result )
	def test_Coord_addXY( self ):
		result = Coord( 100, 100, 0 )
		self.assertEqual( self.c + self.xy, result )
	def test_Coord_addZ( self ):
		result = Coord( 0, 0, 100 )
		self.assertEqual( self.c + self.z, result )
	def test_Coord_addXYZ( self ):
		result = Coord( 100, 100, 100 )
		self.assertEqual( self.c + self.xyz, result )
	def test_Coord_eq_isEqual( self ):
		self.assertTrue( self.x == Coord( 100, 0, 0 ) )
	def test_Coord_eq_notEqual( self ):
		self.assertFalse( self.x == self.y )
		
			
if __name__ == "__main__":		
	unittest.main()
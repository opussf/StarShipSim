#!/usr/bin/env python
""" $Id: TestTickable.py 2369 2010-08-10 04:42:29Z opus $
"""
from Tickable import *

import unittest
class TestTickable( unittest.TestCase ) :

	def setUp( self ):
		self.t = Tickable()

	def test_Tickable_tickAccumGetsProperValueAfter1Second( self ):
		""" That a 1 second sleep is reflected in the update time of the system """
		import time
		self.t.tick()
		self.assertEqual( self.t.tickAccum.seconds, 0, "Should be 0" )
		time.sleep(1)
		self.t.tick()
		self.assertEqual( self.t.tickAccum.seconds, 1, "Should be about 1" )
	def test_Tickable_failAccumGetsProperValueAfter1Second( self ):
		import time
		self.t.tick()
		self.assertEqual( self.t.tickAccum.seconds, 0, "Should be 0" )
		time.sleep(1)
		self.t.tick()
		self.assertEqual( self.t.failAccum.seconds, 1, "Should be about 1" )
	def test_Tickable_InitedIsSet( self ):
		self.failIfEqual( self.t.inited, None )
	def test_Tickable_NowIsSet( self ):
		self.failIfEqual( self.t.now, None )
	def test_Tickable_LastTickInitAtNone( self ):
		self.assertEqual( self.t.lastTick, None )
	def test_Tickable_LastTickUpdated( self ):
		self.t.tick()
		self.failIfEqual( self.t.lastTick, None )
	def test_Tickable_HasElapsed( self ):
		self.failIfEqual( self.t.elapsed, None )
	def test_Tickable_setFailInterval( self ):
		self.t.setFailInterval( 1 )
		self.failIfEqual( self.t.setFailInterval, None )

if __name__ == "__main__":			
	unittest.main()
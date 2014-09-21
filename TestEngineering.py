#!/usr/bin/env python
""" $Id: TestEngineering.py 2369 2010-08-10 04:42:29Z opus $
"""
from Engineering import *

import unittest
class testEngineering( unittest.TestCase ) :
	def setUp( self ) :
		self.eng = Engineering()
	def test_01( self ) :
		print self.eng.objects
	def test_tick( self ) :
		self.eng.tick()
		
			
if __name__ == "__main__":		
	unittest.main()
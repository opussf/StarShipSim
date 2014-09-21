#!/usr/bin/env python
""" $Id: TestStarShip.py 2369 2010-08-10 04:42:29Z opus $
"""
from StarShip import *

import unittest
class testStarShip( unittest.TestCase ):
	def setUp( self ):
		self.starship = StarShip()

#	def test_StarShip_01(self):
#		starship = StarShip()
			
if __name__=="__main__":
	unittest.main()
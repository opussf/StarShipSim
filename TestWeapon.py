#!/usr/bin/env python
""" $Id: TestWeapon.py 2369 2010-08-10 04:42:29Z opus $
"""
from Weapon import *

import unittest
class testWeapon(unittest.TestCase):
	def setUp(self):
		self.w = Weapon()
	def test_Weapon_InitialVals_baseclass(self):
		self.assertEqual(self.w.getFunctionalStatus(),0,"FunctionalStatus should start as 0")
		self.assertEqual(self.w.getReliabilityFactor(),0,"ReliabilityFactor should start as 0")
		self.assertEqual(self.w.getOperationalStatus(),0,"OperationalStatus should start as 0")
#	def test_Weapon(self):
#		pass
		
if __name__ == "__main__":
	unittest.main()

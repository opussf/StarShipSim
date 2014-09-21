#!/usr/bin/env python
""" $Id: Weapon.py 2372 2010-08-10 04:46:03Z opus $

	Weapon Subsystems
"""
import StarShipSystem
import Location

class Weapon( StarShipSystem.StarShipSystem ):
	
	def __init__(self):
		super(Weapon,self).__init__()
		self.target = Location.Location()
		self.location = Location.Location()

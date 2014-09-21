""" $Id: MassObject.py 2356 2010-08-10 04:24:11Z opus $
MassObject
"""

import Location
import Trajectory

class MassObject( object ):
	def __init__( self ):
		self.location = Location.Location()
		self.trajectory = Trajectory.Trajectory()
		self.mass = None    # mass in kg
		self.density = None    # density of object
		
	def setMass( self, value ):
		""" Set the mass of this object.
		an object may have a 0 mass for now, but not negative """
		if value < 0: value = 0
		self.mass = value
	def getMass( self ):
		""" Return the mass of this object """
		return self.mass
	def setDensity( self, value ):
		""" Set the density of this object.
		g/cc is the unit. no negative densities """
		if value < 0: value = 0
		self.density = value
	def getDensity( self ):
		""" Return the density of this object.
		g/cc is the unit """
		return self.density
	def getVolume( self ):
		""" Returns the volume of this object. """
		if not self.mass or not self.density:
			return None
		volume = (self.mass * 1000) / self.density
		return int(volume)
	def tick( self ):
		""" Tick """
		pass

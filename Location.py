""" $Id: Location.py 2357 2010-08-10 04:25:18Z opus $

Location:  A location is based on a frame of reference, and is instantantious.
This sets up a higherarchary of how to find something.

A person may be in a craft, that craft may be on a planet, which is in a solar system, in a universe....

something may be IN the person, or object, in the craft....

This class should then be able to return the location of any object in reference to any other.

Will need to have another class for an Item database (massObject db?) - is that the Universe object?
coords are in meters distance from origin
"""

import Universe
import MassObject
import Coord

class Location( object ):
	universe = Universe.Universe()
	def __init__( self ):
		self.coords = None
		self.reference = None
	def setLocation( self, coordsIn, refIn = None):
		""" sets the location of an object
		takes (x,y,z) tuple and an optional object for reference
		"""
		if (coordsIn is None):
			raise TypeError("coordsIn needs to be a coord type")
		if (isinstance( coordsIn, (list, tuple) ) ):
			coordsIn = Coord.Coord(coordsIn)
		if (not isinstance( coordsIn, Coord.Coord )):
			raise TypeError("coordsIn needs to be a coord type")
		if (refIn is None) or (type(refIn) == type( MassObject.MassObject() ) ):
			self.coords = coordsIn
			self.reference = refIn
			if (refIn is not None):
				self.universe.addObject( refIn )
		else:
			raise TypeError("Invalid reference object given")
	def getLocation( self, refObj = None ):
		""" gets the location of an object
		takes a tuple, a CoordObj, an object for reference, or None
		Tuple or CoordObj, returns coords based on that coord.  Good to calculate a distance from a point
		None, returns coords based on the original refernce object
		refObj, returns coords based on the reference Object.
		"""
		# use given reference object
		if refObj is None:
			return self.coords
		
		# use an object as reference
		elif type(refObj) == type( MassObject.MassObject() ):
			if (refObj == self.reference):    # return same as if given None
				return self.coords
			else:
				#find the coords of the ref object
				refCoord = refObj.location.getLocation( )
				return 0
				raise NotImplementedError
		
		# use an absolute Coord
		elif (isinstance( refObj, (list, tuple, Coord.Coord) ) ):
			# Convert tuple or list to Coord
			if isinstance( refObj, (list, tuple) ):
				refObj = Coord.Coord( refObj )
			# Will need to compute the obsolute distances..
			
			raise NotImplementedError
		else:
			raise TypeError("Invalid reference object given")
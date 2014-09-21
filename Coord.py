""" $Id: Coord.py 2360 2010-08-10 04:28:02Z opus $
"""

import math

class Coord( object ) :
	def __init__ (self, *args):
		super( Coord, self).__init__()
		self.data = None
		if len(args) == 0:
			raise ValueError
		elif len(args) == 1:
			if not isinstance(args[0], (list,tuple)):
				raise TypeError
			elif len(args[0]) != 3:
				raise ValueError
			else:
				self.data = tuple(args[0])
		elif len(args) != 3:
			raise ValueError
		else:
			self.data = tuple((args[0], args[1], args[2]))
	def __add__( self, other ):
		""" add 2 coords together.  return coord
		"""
		if not isinstance( other, Coord ):
			raise TypeError
		return Coord( (self.data[0] + other.data[0], 
				self.data[1] + other.data[1],
				self.data[2] + other.data[2]) )
	def __eq__( self, other ):
		""" eq """
		if not isinstance( other, Coord ):
			return False
		if (self.data[0] == other.data[0]) and \
			(self.data[1] == other.data[1]) and \
			(self.data[2] == other.data[2]):
				return True
		return False
	def __ne__( self, other ):
		""" ne """
		if not isinstance( other, Coord ):
			return False
		if (self.data[0] != other.data[0]) or \
			(self.data[1] != other.data[1]) or \
			(self.data[2] != other.data[2]):
				return True
		return False
	def __str__( self ):
		return "(%0.2f, %0.2f, %0.2f)" % self.data
	def distance( self, other ):
		""" returns the distance between 2 coords 
		d = sqrt[(x1-x2)2 + (y1-y2)2 + (z1-z2)2] 
		"""
		if not isinstance( other, Coord ):
			raise TypeError
		return math.sqrt( pow(self.data[0] - other.data[0], 2) +
				pow(self.data[1] - other.data[1], 2) +
				pow(self.data[2] - other.data[2], 2) )

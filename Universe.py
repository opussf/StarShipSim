""" $Id: Universe.py 2358 2010-08-10 04:25:59Z opus $
Universe

The Universe, for now, is the collection of items in the Universe.
Universe is an object container.
It ticks.

Make this a singleton that all locations have a reference too
"""
import Tickable
#import MassObject

class Universe( Tickable.Tickable ):
	__instance = None
	def __new__( self ):
		if not self.__instance:
			Tickable.Tickable.__new__( self )
			self.objects = {}
			self.__instance = super( Universe, self ).__new__( self )
		return self.__instance
	def addObject( self, obIn ):
		import MassObject
		if not isinstance( obIn, MassObject.MassObject ):
			raise TypeError, "addObject requires a MassObject instance"
		#print "U.addObject(", obIn, ").  id:", id(obIn)
		self.objects[ id(obIn) ] = obIn
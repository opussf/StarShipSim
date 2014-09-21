""" $Id: Tickable.py 2359 2010-08-10 04:26:45Z opus $
"""

import datetime

class Tickable( object ):
	""" This is a base class for anything that has a tick() method
	"""
	
	def __init__( self ):
		self.lastTick = None
		self.now = datetime.datetime.today()
		self.inited = datetime.datetime.today()
		self.elapsed = datetime.timedelta()
		self.tickAccum = datetime.timedelta(0)
		self.failAccum = datetime.timedelta(0)
	def setFailInterval( self, secIn ):
		""" this is the interval for when to fail.
		@param integer secIn number of seconds between fail attempts """
		self.failInterval = datetime.timedelta( seconds = secIn )
	def tick( self ):
		""" updates .now, .updateNow, .lastTick, .elapsed,
		.tickAccum and .failAccum
		Subclass 
		"""
		self.now = datetime.datetime.today()
		self.updateNow = False
		if self.lastTick :
			accumVal = self.now - self.lastTick
			self.tickAccum += accumVal
			self.failAccum += accumVal
		self.lastTick = self.now
		self.elapsed = self.now - self.inited

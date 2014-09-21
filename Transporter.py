""" $Id: Transporter.py 2377 2010-08-10 04:48:49Z opus $

	Transporter module.
"""
import StarShipSystem
import Location
import MassObject

class Transporter( StarShipSystem.StarShipSystem ) :
	__buffer = 0
	__bufferMax = 200000
	supply = None
	
	def __init__( self ) :
		super( Transporter, self).__init__()
		self.bufferStatus = 0
	def getBufferStatus( self ) :
		""" return the % of the buffer is full.  0 - 100 (full) """
		return self.__buffer / self.__bufferMax
	def setSupply( self, supply ) :
		""" sets the supply that this pulls energy from """
		self.supply = supply

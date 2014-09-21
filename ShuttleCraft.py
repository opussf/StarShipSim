""" $Id: ShuttleCraft.py 2371 2010-08-10 04:45:31Z opus $

	ShuttleCraft module.
"""
import StarShipSystem
import MassObject

class ShuttleCraft( StarShipSystem.StarShipSystem, MassObject.MassObject ) :
	def __init__( self ) :
		MassObject.MassObject.__init__( self )
		StarShipSystem.StarShipSystem.__init__( self )
		self.cargo = []
	def addObject( self, obj ):
		self.cargo.append( {"obj": obj, "added": self.now} )


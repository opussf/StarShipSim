""" $Id: EnergyConduit.py 2370 2010-08-10 04:43:44Z opus $

	EnergyConduit module.  This module actually moves energy to a system.
	
"""

import StarShipSystem
import EnergySupply

class NoSupply ( Exception ) :
	pass

class EnergyConduit ( StarShipSystem.StarShipSystem ) :
	""" Energy Conduit moves energy from EnergySupply to the the system that needs the energy
		Can only move so much each second.  
	"""
	maxEnergyPerSec = 500
	""" The maximum amount of energy per second before damage occurs.  This is energy asked, not deliverd """
	energyAskedAccum = 0
	""" This is energy asked for """
	energySupply = None
	
	def __init__(self):
		super(EnergyConduit,self).__init__()
		
	def setSupply( self, supply ) :
		self.energySupply = supply
		
	def getEnergy( self, amount ) :
		""" Pulls energy from the supply and moves it along.
		TODO: Backward flow of energy?	
		"""
		energy = 0
		getAmount = 0
		if not self.energySupply :
			raise NoSupply
		if self.operationalStatus :
			getAmount = amount * self.operationalStatus / 100
			self.energyAskedAccum += amount
		if self.functionalStatus :
			energy = ( self.energySupply.getEnergy( getAmount ) * self.functionalStatus ) / 100
		return energy

	def tick( self ) :
		""" EnergyConduit tick, checks for the amount of enery moved in a period of time.
		"""
		super( EnergyConduit, self).tick()
		if self.updateNow :
			if self.energyAskedAccum > self.maxEnergyPerSec :
				overAsked = self.energyAskedAccum - self.maxEnergyPerSec
				damageDone = (overAsked / 100) ** 2
				self.functionalStatus -= damageDone
				print "Energy Conduit: Damage Done:", damageDone, "New functionalStatus:", self.functionalStatus
			self.energyAskedAccum = 0


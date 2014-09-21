""" $Id: Shield.py 2371 2010-08-10 04:45:31Z opus $

	Shield Subsystems

"""
import StarShipSystem

class Shield( StarShipSystem.StarShipSystem ):
	maxEnergy = 100000			# max energy for system (adjust by functional and operational)
	energyPerSec = 60			# energy added per second
	energy = 0					# current energy lvl
	energySupply = None

	def __init__( self ):
		super( Shield, self ) . __init__()
		self.energy = 0
	def setSupply( self, supply ):
		self.energySupply = supply
	def getStatus( self ):
		""" current Energy, MaxEnergy """
		return ( self.energy, self.getMaxEnergy())
	def getMaxEnergy( self ):
		""" Return the modified maxEnergy for the system, based on functional status """
		maxE = 0
		if self.functionalStatus :
			maxE = ( self.maxEnergy * self.functionalStatus ) / 100
		return maxE
	def takeDamage( self, damageAmt ):
		""" Takes the damage directed at it, and returns the amount passed on
		"""
		if damageAmt < 0 :
			raise ValueError
		damagePassed = 0
		self.energy -= damageAmt
		if self.energy < 0 :
			damagePassed = -self.energy
			self.energy = 0
		return damagePassed
	def tick ( self ):
		super( Shield, self ).tick()
		maxE = self.getMaxEnergy()
		if self.updateNow :
			maxFill = ( maxE * self.operationalStatus ) / 100
			if self.energy < maxFill :
				energy = self.energySupply.getEnergy( self.energyPerSec )
				self.energy += ( energy * self.functionalStatus ) / 100
			self.update()
		if self.energy > maxE :
			self.energy = maxE

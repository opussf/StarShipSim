#!/usr/bin/env python
"""EnergyGeneration.py

	EnergyGeneration module.  This module actually generates energy.  Consumes 'fuel' and produces energy.
	Subclasses of this module will decide the 'fuel' and the other values of this system.
	
"""

import StarShipSystem

class EnergyGeneration( StarShipSystem.StarShipSystem ) :
	massUnit = "gram"
	reactiveMass = 0								# mass in grams	
	maxReactiveMass = 0								# mass in grams
	energyPool = 0									# Engergy in Joules
	conversionRateToEnergy = (300000**2)*1000		# E=mc^2  m=kg E=Joules c=speed of light
	conversionRateToEnergy = 45700					# 45.7 MJ/kg  in Gasoline
	#conversionRateToEnergy = 4570000				# Experimental value
	conversionRatePerSecond = conversionRateToEnergy / 60	# second being a tick (for now)
	maxEnergyPool = conversionRateToEnergy
	
	def __init__(self):
		super(EnergyGeneration,self).__init__()

	def __convertUnitOfMass( self ) :
		""" convert reactiveMass to energy.  Call this once a second
		"""
		gainEnergy = ( self.conversionRatePerSecond * self.operationalStatus ) / 100
		if ( self.energyPool + gainEnergy < self.maxEnergyPool ) and ( self.reactiveMass > 0 ) :
			self.energyPool += gainEnergy
			self.reactiveMass -= 1

	def getStatus ( self ) :
		""" returns the energyPool, ( amount, % of max )
		"""
		#return ( self.energyPool, ( self.energyPool * 100 ) / self.maxEnergyPool )
		return( self.energyPool, self.maxEnergyPool )

	def getReactiveMass( self ) :
		""" returns the reactive mass, (amount, % of total)
		"""
		if self.maxReactiveMass > 0 :
			return (self.reactiveMass, (self.reactiveMass *100) / self.maxReactiveMass)
		else:
			return ( 0, 0 )
	def getEnergy( self, amount ) :
		""" try to get a certain amount of energy
		"""
		if amount < 0 :
			amount = 0
		returnAmount = min ( amount, self.energyPool )
		if self.energyPool > returnAmount :
			self.energyPool -= returnAmount
		else :
			self.energyPool = 0
		return returnAmount
	def setMaxReactiveMass( self, MR ) :
		if MR < 0 :
			MR = 0
		self.maxReactiveMass = MR
		return MR
	def setReactiveMass( self, RM ) :
		""" This sets the value of the reactiveMass.
		Negative Values set to 0, >max set to max
		"""
		if RM < 0:
			RM = 0
		if RM > self.maxReactiveMass :
			RM = self.maxReactiveMass
		self.reactiveMass = RM 
		return RM
	def changeReactiveMass( self, CM ) :
		""" Change the amount of reactive mass from an external source.
		Something akin to refueling.  Can also empty the "tank" this way too.
		returns the amount taken.
		"""
		maxToChange = self.maxReactiveMass - self.reactiveMass
		if ( CM > maxToChange ) :
			CM = maxToChange
		if ( CM < -self.reactiveMass ) :
			CM = -self.reactiveMass
		self.reactiveMass += CM
		return CM
	def tick ( self ) :
		super( EnergyGeneration, self ).tick()
		#print "EnergyGen tick", self.updateNow
		if self.updateNow :
			self.__convertUnitOfMass()
			self.update()
#			print self.getStatus(), 
#		print "EnergyGeneration Tick"
#		print

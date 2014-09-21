#!/usr/bin/env python
"""EnergySupply.py

	EnergySupply module.  This module actually stores energy.  Making it available to systems via EnergyConduits.
	
"""

import StarShipSystem
import EnergyGeneration

class EnergySupply(StarShipSystem.StarShipSystem):
	maxQuantity = 20 * (10**9)			# max Energy ammount
	maxQuantity = 2 * (10**9)
	quantity = 0						# current Energy ammount
	energyGeneration = None				# energy generator 
	
	def __init__(self):
		super(EnergySupply,self).__init__()
		self.quantity = self.maxQuantity
		
	def setEnergyGeneration( self, eg ) :
		self.energyGeneration = eg
		
	def getEnergy ( self, amount ) :
		""" returns an amount of energy requested
		"""
		returnAmount = min ( amount, self.quantity )
		if returnAmount > 0 :
			self.quantity -= returnAmount
		return returnAmount

	def getStatus ( self ) :
		return ( self.quantity, self.maxQuantity )
	
	def tick ( self ) :
		super ( EnergySupply, self ).tick()
		if self.energyGeneration :
			#self.energyGeneration.tick()
			if self.quantity < self.maxQuantity :
				self.quantity += self.energyGeneration.getEnergy(self.maxQuantity-self.quantity)

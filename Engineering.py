#!/usr/bin/env python
"""Engineering.py

	Engineering module.
"""

import EnergySupply
import EnergyGeneration
import EnergyConduit
import ImpulseEngine
import WarpEngine
import TurboElevator
import Transporter
import Shield
import ShuttleCraft
#import wx

class Engineering( object ) :
	"""Engineering
	
	Engineering has the following modules:
		EnergySupply
		EnergyGeneration
		ImpulseEngines
		WarpEngines
		TurboElevators
		Transporters
		ShuttleCraft?
		Shields?
	"""
	objects = None						# This is a collection of all the objects here
	energyConduits = None
	
	def __init__( self ) :
		self.objects = []
		self.energySupply = EnergySupply.EnergySupply()
		self.energySupply.setOperationalStatus(100)
		self.energySupply.setFunctionalStatus(100)
		self.energySupply.setReliabilityFactor(100)
		self.objects.append( self.energySupply )
		
		self.energyGeneration = EnergyGeneration.EnergyGeneration()
		self.energyGeneration.setOperationalStatus( 100 )
		self.energyGeneration.setFunctionalStatus( 100 )
		self.energyGeneration.setReliabilityFactor(100)
		self.energyGeneration.setMaxReactiveMass( 16330 )
		self.energyGeneration.setReactiveMass( 1000 )
		self.energySupply.setEnergyGeneration( self.energyGeneration )
		
		self.objects.append( self.energyGeneration )
		self.warpEngine = WarpEngine.WarpEngine()
		self.objects.append( self.warpEngine )
		self.impulseEngine = ImpulseEngine.ImpulseEngine()
		self.objects.append( self.impulseEngine )
#		self.lifeSupport = LifeSupport.LifeSupport()
#		self.objects.append( self.lifeSupport )
		
		self.energyConduits = []
		ec = EnergyConduit.EnergyConduit()
		ec.setFunctionalStatus(100)
		ec.setReliabilityFactor(100)
		ec.setOperationalStatus(100)
		ec.setSupply( self.energySupply )
		self.energyConduits.append( ec )
		self.objects.append( ec )
		
		self.shields = []
		for lcv in range( 6 ) :  # 0-5
			sh = Shield.Shield()
			sh.setFunctionalStatus(100)
			sh.setReliabilityFactor(95)
			sh.setSupply( self.energyConduits[0] )
			self.shields.append( sh )
			self.objects.append( sh )
		
		self.shuttleCraft = []
		for lcv in range( 6 ) :
			sc = ShuttleCraft.ShuttleCraft()
			self.shuttleCraft.append( sc )
			self.objects.append( sc )
		self.running = True
	
	def getEnergyConduit( self ) :
		""" make a new energy conduit and return it """
		nec = EnergyConduit.EnergyConduit()		# nec = New Energy Conduit
		nec.setFunctionalStatus( 100 )
		nec.setReliabilityFactor( 100 )
		nec.setOperationalStatus( 100 )
		nec.setSupply( self.energySupply )
		self.energyConduits.append( nec )
		self.objects.append( nec )
		return nec
		
	def tick( self ) :
		if self.running :
			for obj in self.objects :
				obj.tick()
			
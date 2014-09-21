""" $Id: StarShip.py 2376 2010-08-10 04:48:10Z opus $

	This is the StarShip.  It contains the modules that make up a star ship.
	It also contains the parts of the ship
	
"""
import MassObject
import Tickable

class StarShip( Tickable.Tickable, MassObject.MassObject ):
	locations = {}
	systems = {}
	
	def __init__ ( self ) :
		self.locations['Bridge'] = []
		self.locations['Sciences'] = []
		self.systems['Engineering'] = []
		self.locations['Brig'] = []
		"""
		Security
		Nav
		MedicalLab
		MedicalComp
		TEComp
		TractorBeam
		FoodProcessing
		OxygenSystems
		WaterSystems
		EnergySuppy
		IntensiveCareUnit
		SensorStations
		CrewQuarters
		ShuttleBay
		TransporterStations
		TEStation
		TurboElevator
		ShuttleCraft
		PhotoTorpedoTube
		PhaserStation
		DeflectorShieldStation
		"""	



""" $Id: TurboElevatorSystem.py 2377 2010-08-10 04:48:49Z opus $

	TurboElevatorSystem
	
	Transfer time within service area = 1 min
	Transfer between service areas is the difference in area numbers * 90 seconds
	Time is modified by funtional and operational status
	Energy is based on the number of items in motion
	
	From figure 3.6 (page 30) - The Star Ship Simulation Project
	T/E station Number			Area
		1						Bridge
								Sensor Stations
								Transporter #1
								Phaser Station #1
							
		2						Sciences Lab
								Transporter #2
								Torpedo Tube #1
								Deflector Shield Station #1
								
		3						Engineering
								Transporter #3
								Phaser Station #2

		4						Navigation Computer
								Transporter #4
								Torpedo Tube #2
								Deflector Shield Station #2
		
		5						Medical Research Lab
								Medical Computer
								Intensive Care Unit
								Transporter #5
								Phaser Station #3
								
		6						Turbo Elevator Computer
								Food Processing Plant
								Oxygen Distribution and recycling center
								Water Distribution and recycling center
								Transporter #6
								Torpedo Tube #3
								Deflector Shield Station #3
								
		7						Energy Supply
								Transporter #7
								Phaser Station #4
								
		8						Energy Supply
								Transporter #8
								Torpedo Tube #4
								Deflector Shield Station #4
								
		9						Transporter #9
								Phaser Station #5
								Deflector Shield Station #5
								
		10						Transporter #10
								Shuttle Bay
								Phaser Station #6
								Deflector Shield Station #6
	
"""

import StarShipSystem
import MassObject

class TurboElevatorSystem( StarShipSystem.StarShipSystem ):
	#stations = {}
	#cargo = []
	def __init__( self ):
		StarShipSystem.StarShipSystem.__init__( self )
		self.cargo = []
	def addObject( self, obj ):
		self.cargo.append( {"obj": obj, "added": self.now} )
	def tick( self ):
		pass

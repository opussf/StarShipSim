""" $Id: StarShipSystem.py 2366 2010-08-10 04:39:49Z opus $

	Generic System Object for Systems on a StarShip
"""

import logging
import datetime
import random
import Tickable

class StarShipSystem( Tickable.Tickable ):
	__statusMax = 100
	__statusMin = 0
	functionalStatus = 0			# 0 - 100%		100 - perfectly functional, 0 - complete fail!!!!1!
	reliabilityFactor = 0			# 0 - 100%		How realiable
	operationalStatus = 0			# 0 - 100%		Set operational Status
	energyRequirement = None		# energy required to operate system
	#energyRequirementUnit = 0		# type of Energy model 0 = instant, 1= over time
	#energyType = None				# type of Energy needed to use
	energyCapacitor = 0				# energy stored in system
	energySupply = None				# the energy supply for this system
	__updateInterval = None			# How often to update?
	__updateCallback = None
	updateNow = False
	failInterval = None
	
	def __init__(self):
		super( StarShipSystem, self ).__init__()
		self.failInterval = datetime.timedelta( seconds = 60 )
		self.setUpdateInterval( 1 )
	def setFunctionalStatus(self, statusIn):
		""" sets the Functional Status of the system.  From 0 to 100 """
		if (statusIn >= self.__statusMin) and (statusIn <= self.__statusMax):
			self.functionalStatus = statusIn
		else:
			raise ValueError("Invalid Status Value")
	
	def setReliabilityFactor( self, statusIn ):
		""" sets the Reliability Factor of the system.  From 0 to 100 """
		if (statusIn >= self.__statusMin) and (statusIn <= self.__statusMax):
			self.reliabilityFactor = statusIn
		else:
			raise ValueError("Invalid Status Value")
			
	def setOperationalStatus( self, statusIn ):
		""" sets the Operational Status of the system.  From 0 to 100 """
		if (statusIn >= self.__statusMin) and (statusIn <= self.__statusMax):
			self.operationalStatus = statusIn
		else:
			raise ValueError("Invalid Status Value")
		
	def setUpdateInterval( self, seconds = 1 ) :
		""" sets the updateInterval value to the number of seconds """
		if seconds > 0 :
			self.__updateInterval = datetime.timedelta( seconds = seconds )
		else :
			raise ValueError("Invalid Update Value")
		
	def getFunctionalStatus( self ):
		""" This is the functional status, or damage level.  100 is fully functional, 100% efficicent.
		0 is totally failed.  Engineering repairs raise this value.  Damage, and failures lower this value.
		"""
		return self.functionalStatus
	
	def getReliabilityFactor( self ):
		""" This is the reliability of the system.  When will it fail?  100 is no chance of failure.
		0 is failing all the time
		"""
		return self.reliabilityFactor

	def getOperationalStatus( self ):
		""" This is if the system is working and to what degree.  Set to 0 to turn off,
		set to 100 to turn on.  Ranges between determine a percent.  IE shields at 50%.
		"""
		return self.operationalStatus
	
	def performDiagnosis( self, level=None ) :
		""" This performs a diagnosis on this system """
		pass
	
	def setEnergySupply( self, supply ) :
		""" Sets the energy supply for this system
		TODO: make sure that this supply can provide energy
		"""
		self.energySupply = supply
		
	def setUpdateCallback( self, func ) :
		self.__updateCallback = func
	
	def update( self ) :
		""" call this method when an update happens """
		self.tickAccum -= self.__updateInterval
	
	def tick( self ) :
		""" the tick at this level will set the FunctionalStatus based on the ReliabilityFactor
		updates lastTick, and adds time to tickAccum
		"""
		super( StarShipSystem, self ).tick()
		if self.functionalStatus :
			if self.failAccum > self.failInterval :
				#print "SSS FAIL TEST"
				self.failAccum -= self.failInterval
				r = random.randint(self.__statusMin+1, self.__statusMax)
				if r > self.reliabilityFactor :
					self.functionalStatus -= 1
					if r == 50 :
						self.functionalStatus -= 20
					#print ( "r:", r, ">", self.reliabilityFactor, "f:", self.functionalStatus )
			if self.tickAccum > self.__updateInterval :
				""" set the updateNow flag, if a callback is registered, call that.
					Leave the updateNow flag set if the callback is called so that the parent can also do something """
				self.updateNow = True
				if self.__updateCallback is not None :
					val = self.__updateCallback()
					self.update()
		if self.functionalStatus < 0 :	self.functionalStatus = 0
		if self.reliabilityFactor < 0 : self.reliabilityFactor = 0
		if self.operationalStatus < 0 : self.operationalStatus = 0
#		print ( "tickAccum:", self.tickAccum )



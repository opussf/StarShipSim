""" $Id: Person.py 2375 2010-08-10 04:47:36Z opus $
"""

import datetime
import Location
import MassObject
import Tickable

class Rank( object ):
	pass

class Job( object ):
	pass


class Person( Tickable.Tickable, MassObject.MassObject ):
	""" Person object.
	HealthStatus is a percent of health.  Divide this into 5ths.  
	0 is dead, 1-20 is unconcious, 21-40 is sick enough to not work, 
	41-60 is sick at dropping functional, 61-80 is sick with stable functional, 
	81-100 is healthy with raising functional.
	
	Get 4 health for each meal
	get 2 health for each 30 minutes sleeping
	lose 1 health for each 30 minutes awake
	lose 2 functional for each 30 minutes working
	
	"""
	__statusMin, __statusMax = 0, 100
	foodConsumption = 1				# kg/hr average  (0.25 sounds better)
	waterConsumption = 1			# l/hr average
	oxygenConsumption = 1			# l/hr average
	
	def __init__( self ):
		MassObject.MassObject.__init__( self )
		Tickable.Tickable.__init__( self )
		self.inited = datetime.datetime.today()
		self.setDensity( 1 )    # most people are about this density
		self.failInterval = datetime.timedelta( seconds = 1800 )
		self.functionalStatus = 100
		self.healthStatus = 100
		self.isSleeping = False
		self.isWorking = False
		self.diseases = []
		self.destination = None
		self.name = None
		self.age = None
		self.intelligence = None
		self.rank = Rank()
		self.job = Job()

	def setName( self, name ):
		self.name = name
	def getName( self ):
		return self.name
	def getHealthStatus( self ):
		""" Returns the current health of this person """
		return self.healthStatus
	def setHealthStatus( self, val ):
		""" sets the current health of this person. 0=dead, 100=full health	"""
		if (val >= self.__statusMin) and (val <= self.__statusMax):
			self.healthStatus = val
		else:
			raise ValueError("Invalid Health Value")
	def raiseHealthStatus( self, valIn = 1 ):
		""" Raise the health status of the person by valIn (defualts to 1) """
		self.healthStatus += valIn
		if self.healthStatus > self.__statusMax:
			self.healthStatus = self.__statusMax
	def lowerHealthStatus( self, valIn = 1 ):
		""" Lower the health status of the person by 1 """
		self.healthStatus -= valIn
		if self.healthStatus < self.__statusMin:
			self.healthStatus = self.__statusMin
	def setFunctionalStatus(self, statusIn):
		""" sets the Functional Status of the system.  From 0 to 100 """
		if (statusIn >= self.__statusMin) and (statusIn <= self.__statusMax):
			self.functionalStatus = statusIn
		else:
			raise ValueError("Invalid Status Value")
		
	def __str__( self ):
		strOut = "%s" % (self.name,)
		return strOut
			
	def tick( self ) :
		""" A person loses health during the day.  eating, sleeping, and medical
		can raise the health.
		FunctionalStatus is raised or lowered based on health.
		"""
		super( Person, self ).tick()
		if self.healthStatus > 0:
			""" still alive """
			if self.failAccum > self.failInterval:
				self.failAccum -= self.failInterval
				if self.isSleeping:
					self.raiseHealthStatus(2)    # raise by 2 from sleeping
				elif self.isWorking:
					self.lowerHealthStatus(2)
				else:
					self.lowerHealthStatus()
				if self.healthStatus <= 60:
					self.functionalStatus -= 1
				elif self.healthStatus > 80:
					self.functionalStatus += 1
			if self.functionalStatus < 0:
				self.functionalStatus = 0
			elif self.functionalStatus > 100:
				self.functionalStatus = 100








		"""
		self.now = datetime.datetime.today()
		self.updateNow = False
		if self.lastTick :
			accumVal = self.now - self.lastTick
			self.tickAccum += accumVal
			self.failAccum += accumVal
		self.lastTick = self.now
		self.elapsed = self.now - self.inited
		
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
		"""
		""" set the updateNow flag, if a callback is registered, call that.
			Leave the updateNow flag set if the callback is called so that the parent can also do something """
		"""
			self.updateNow = True
			if self.__updateCallback is not None :
				val = self.__updateCallback()
				self.update()
		if self.functionalStatus < 0 :	self.functionalStatus = 0
		if self.reliabilityFactor < 0 : self.reliabilityFactor = 0
		if self.operationalStatus < 0 : self.operationalStatus = 0
#		print ( "tickAccum:", self.tickAccum )
		"""
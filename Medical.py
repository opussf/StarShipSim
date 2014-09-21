""" $Id: Medical.py 2374 2010-08-10 04:47:08Z opus $

	Medical module.
"""
import StarShipSystem
import Person

class Medical( StarShipSystem.StarShipSystem ) :
	""" Medical systems.
	Takes people, and energy, and raises their health status
	How much energy is needed for healing?  What is the rate for healing?
	What is the effect of lower Functional, Operational, or Reliabity?
	"""
	supply = None    # energy supply, used to heal people.  Create medicines, etc.
	beds = None      # beds for injured, or sick people
	healed = None    # list of people who are healed, but not returned to active status
	standby = None   # list of people too sick to be healed, but not sick enough for a currently used bed
	dead = None      # list of people who are dead (died here, or brought in dead)
	capacity = 10
	energyPerHealth = 100
	
	def __init__( self ) :
		super( Medical, self).__init__()
		self.beds = []
		self.healed = []
		self.standby = []
		self.dead = []
	def getAvailable( self ):
		""" returns the number of beds available """
		return self.capacity - len(self.beds)
	def getCapacity( self ):
		""" returns the capacity of the medical lab """
		return self.capacity
	def setSupply( self, supply ) :
		""" sets the supply that this pulls energy from """
		self.supply = supply
	def addPerson( self, person ):
		""" add a person to the lab.  Put them in a bed, or if all full, the standby queue """
		if len(self.beds) < self.capacity:
			self.beds.append(person)
		else:
			self.standby.append(person)
	def getStatusReport( self ):
		statusOut = {}
		statusOut["bedsAvailable"] = self.capacity - len(self.beds)
		statusOut["bedsStatus"] = self.beds
		statusOut["healedStatus"] = self.healed
		statusOut["standbyStatus"] = self.standby
		statusOut["deadStatus"] = self.dead
		return statusOut
	def getHealed( self ):
		if len(self.healed):
			return self.healed.pop()
		return None
	def tick( self ):
		super( Medical, self ).tick()
		# cycle through beds for healed patients, and for dead
		for i in range( len( self.beds ) ):
			person = self.beds[i]
			if person.getHealthStatus() >= 99:
				self.beds.pop(i)
				self.healed.append( person )
			if person.getHealthStatus() == 0:
				self.beds.pop(i)
				self.dead.append( person )
		# move standby to open beds
		while (len( self.beds ) < self.capacity) and (len( self.standby) > 0):
			self.beds.append( self.standby.pop() )
		# triage.  If there is someone sicker than the sickest in the beds, remove best from beds
		if (len( self.beds ) == self.capacity) and (len( self.standby ) > 0):    # need to triage
			bestInBeds = ( 0, self.beds[0].getHealthStatus() )
			for i in range( len( self.beds ) ):
				person = self.beds[i]
				if person.getHealthStatus() > bestInBeds[1]:
					bestInBeds = ( i, person.getHealthStatus() )
			worseInStandby = ( 0, self.standby[0].getHealthStatus() )
			for i in range( len( self.standby ) ):
				person = self.standby[i]
				if person.getHealthStatus() < worseInStandby[1]:
					worseInStandby = ( i, person.getHealthStatus() )
			if (worseInStandby[1] < bestInBeds[1]):
				self.standby.append( self.beds.pop( bestInBeds[0] ) )
				self.beds.append( self.standby.pop( worseInStandby[0] ) )
		# heal patients in the beds
		if self.supply:
			energy = 0
			for person in self.beds:    # only heal those in beds
				while energy < self.energyPerHealth:
					energy += self.supply.getEnergy( self.energyPerHealth )
				person.raiseHealthStatus()
				energy -= self.energyPerHealth
			#print "Energy left over:", energy
		# tick all alive people
		allPeople = []
		allPeople.extend( self.beds )
		allPeople.extend( self.healed )
		allPeople.extend( self.standby )
		for p in allPeople:
			p.tick()
			


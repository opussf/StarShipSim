#!/usr/bin/env python
""" $Id: TestPerson.py 2369 2010-08-10 04:42:29Z opus $
"""
from Person import *
	
import unittest
class testPerson( unittest.TestCase ):
	def setUp( self ):
		self.p = Person()
	def test_Person_getHealthStatus( self ):
		self.assertEqual( self.p.getHealthStatus(), 100, "Health should be 100")
	def test_Person_getMass( self ):
		self.p.setMass( 113 )
		self.assertEqual( self.p.getMass(), 113 )
	
	def test_Person_setHealthStatus( self ):
		self.p.setHealthStatus( 50 )
		self.assertEqual( self.p.getHealthStatus(), 50, "Health should be about 50" )
		self.p.setHealthStatus( 0 )
		self.assertEqual( self.p.getHealthStatus(), 0, "Health should be about 0" )
		self.assertRaises( ValueError, self.p.setHealthStatus, -1 )
		self.assertRaises( ValueError, self.p.setHealthStatus, 101 )
	def test_Person_raiseHealthStatus( self ):
		self.p.setHealthStatus( 50 )
		self.p.raiseHealthStatus()
		self.assertEquals( self.p.getHealthStatus(), 51 )
	def test_Person_lowerHealthStatus( self ):
		self.p.setHealthStatus( 50 )
		self.p.lowerHealthStatus()
		self.assertEquals( self.p.getHealthStatus(), 49 )
	def test_Person_setName( self ):
		self.p.setName( "Bob" )
	def test_Person_getName( self ):
		self.p.setName( "Fred" )
		self.assertEquals( self.p.getName(), "Fred" )
	def test_Person_Display( self ):
		self.p.setName( "Dave" )
		self.assertEquals( str( self.p ), "Dave" )
	def test_Person_2People( self ):
		self.p2 = Person()
		self.p2.setHealthStatus( 50 )
		self.assertEqual( self.p2.getHealthStatus(), 50 )
		self.assertEqual( self.p.getHealthStatus(), 100 )
	def test_Person_healthStatusFalls_Accelerated( self ):
		import time
		self.p.setFailInterval( 1 )
		self.p.tick()
		time.sleep(1)
		self.p.tick()
		self.assertEqual( self.p.healthStatus, 99 )
		self.assertEqual( self.p.functionalStatus, 100 )
	def test_Person_functionalStatusFalls_Accelerated( self ):
		import time
		self.p.setFailInterval( 1 )
		self.p.setHealthStatus( 60 )
		self.p.tick()
		time.sleep(1)
		self.p.tick()
		self.assertEqual( self.p.healthStatus, 59 )
		self.assertEqual( self.p.functionalStatus, 99 )
	def test_Person_healthStatusRaisesIfSleeping_Accelerated( self ):
		import time
		self.p.setFailInterval( 1 )
		self.p.setHealthStatus( 50 )
		self.p.isSleeping = True
		self.p.tick()
		time.sleep(1)
		self.p.tick()
		self.assertEqual( self.p.healthStatus, 52 )
		self.assertEqual( self.p.functionalStatus, 99 )
	def test_Person_functionalStatusRaises_Accelerated( self ):
		import time
		self.p.setFailInterval( 1 )
		self.p.setHealthStatus( 82 )
		self.p.setFunctionalStatus( 50 )
		self.p.tick()
		time.sleep(1)
		self.p.tick()
		self.assertEqual( self.p.healthStatus, 81 )
		self.assertEqual( self.p.functionalStatus, 51 )
	def test_Person_24hCycle_Accelerated( self ):
		""" 24h cycle at 30 minutes can be simmed in 48s """
		import time
		self.p.setFailInterval( 1 )
		self.p.setHealthStatus( 96 )
		self.assertEqual( self.p.healthStatus, 96 )
		self.assertEqual( self.p.functionalStatus, 100 )
		
		self.p.tick()
		self.p.raiseHealthStatus(3)    # breakfast
		#	self.p.eatMeal()
		time.sleep( 1 )    # 30 minute breakfast
		self.p.tick()
		self.p.isWorking = True
		for lcv in range(8):	# 4 hour shift
			time.sleep( 1 )
			self.p.tick()
		self.p.isWorking = False
		self.p.raiseHealthStatus(3)    # lunch
		for lcv in range(2):    # 1 hour lunch
			time.sleep( 1 )
			self.p.tick()
		self.p.isWorking = True
		for lcv in range(8):	# 4 hour shift
			time.sleep( 1 )
			self.p.tick()
		self.p.isWorking = False
		self.p.raiseHealthStatus(5)    # dinner
		for lcv in range(2):    # 1 hour dinner
			time.sleep( 1 )
			self.p.tick()
		for lcv in range(11):    # 5.5 hour rest time
			time.sleep( 1 )
			self.p.tick()
		self.p.isSleeping = True
		for lcv in range(16):    # 8 hour sleep
			time.sleep( 1 )
			self.p.tick()
		self.p.isSleeping = False
		
		#	self.p.eatMeal()
		self.assertEqual( self.p.healthStatus, 91 )
		self.assertEqual( self.p.functionalStatus, 100 )
		
		
	def test_Person_tick( self ):
		self.p.tick()

if __name__ == "__main__":			
	unittest.main()
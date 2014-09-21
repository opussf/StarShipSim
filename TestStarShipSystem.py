#!/usr/bin/env python
""" $Id: TestStarShipSystem.py 2369 2010-08-10 04:42:29Z opus $ 
"""
from StarShipSystem import *

import unittest
class testStarShipSystem( unittest.TestCase ):
	class SupplyTest ( object ) :
		""" Test stub for Energy Supply """
		def getEnergy ( self, amount ) :
			return amount
	def setUp(self):
		self.sss = StarShipSystem()
	def test_StarShipSystem_InitialVals(self):
		self.assertEqual(self.sss.getFunctionalStatus(),0,"FunctionalStatus should start as 0")
		self.assertEqual(self.sss.getReliabilityFactor(),0,"ReliabilityFactor should start as 0")
		self.assertEqual(self.sss.getOperationalStatus(),0,"OperationalStatus should start as 0")
	def test_StarShipSystem_setFun_01(self):
		self.sss.setFunctionalStatus(100)
		self.assertEqual(self.sss.getFunctionalStatus(), 100, "FunctionalStatus should be 100")
	def test_StarShipSystem_setFun_02(self):
		try:
			self.sss.setFunctionalStatus(101)
			self.fail("Should throw an exception")
		except ValueError:
			self.assertEqual(self.sss.getFunctionalStatus(), 0, "FunctionalStatus should be 0")
		except:
			self.fail("Wrong Exception thrown")
	def test_StarShipSystem_setFun_03(self):
		try:
			self.sss.setFunctionalStatus(-1)
			self.fail("Should throw an exception")
		except ValueError:
			self.assertEqual(self.sss.getFunctionalStatus(), 0, "FunctionalStatus should be 0")
		except:
			self.fail("Wrong Exception thrown")
	def test_StarShipSystem_setRel_01(self):
		self.sss.setReliabilityFactor(100)
		self.assertEqual(self.sss.getReliabilityFactor(), 100, "ReliabilityFactor should be 100")
	def test_StarShipSystem_setRel_02(self):
		try:
			self.sss.setReliabilityFactor(101)
			self.fail("Should throw an exception")
		except ValueError:
			self.assertEqual(self.sss.getReliabilityFactor(), 0, "ReliabilityFactor should be 0")
		except:
			self.fail("Wrong Exception thrown")
	def test_StarShipSystem_setRel_03(self):
		try:
			self.sss.setReliabilityFactor(-1)
			self.fail("Should throw an exception")
		except ValueError:
			self.assertEqual(self.sss.getReliabilityFactor(), 0, "ReliabilityFactor should be 0")
		except:
			self.fail("Wrong Exception thrown")
	def test_StarShipSystem_setOp_01(self):
		self.sss.setOperationalStatus(100)
		self.assertEqual(self.sss.getOperationalStatus(), 100, "OperationalStatus should be 100")
	def test_StarShipSystem_setOp_02(self):
		try:
			self.sss.setOperationalStatus(101)
			self.fail("Should throw an exception")
		except ValueError:
			self.assertEqual(self.sss.getOperationalStatus(), 0, "OperationalStatus should be 0")
		except:
			self.fail("Wrong Exception thrown")
	def test_StarShipSystem_setOp_03(self):
		try:
			self.sss.setOperationalStatus(-1)
			self.fail("Should throw an exception")
		except ValueError:
			self.assertEqual(self.sss.getOperationalStatus(), 0, "OperationalStatus should be 0")
		except:
			self.fail("Wrong Exception thrown")
	def test_StarShipSystem_tick_01( self ) :
		""" That a 1 second sleep is reflected in the update time of the system """
		import time
		self.sss.tick()
		self.assertEqual( self.sss.tickAccum.seconds, 0, "Should be 0" )
		time.sleep(1)
		self.sss.tick()
		self.assertEqual( self.sss.tickAccum.seconds, 1, "Should be about 1" )
		self.assertEqual( self.sss.failAccum.seconds, 1, "Should be about 1" )
	def test_StarShipSystem_tick_02( self ) :
		""" Test the ticks till 1 second is accumulated
		Fails if it never completes """
		c = 0
		while ( self.sss.tickAccum.seconds < 1 ) :
			c += 1
			self.sss.tick()
		print ( "1 second took %i ticks." % (c,))
	def test_StarShipSystem_tick_03( self ) :
		""" Test that the accum can be modified externally """
		import datetime
		start = datetime.datetime.today()
		update = datetime.timedelta(seconds=1)
		c = 2
		rt = 4
		while ( self.sss.tickAccum.seconds < 2 ) :
			if (self.sss.tickAccum > update) and c>0 :
				self.sss.tickAccum -= update
				c -= 1
			self.sss.tick()
		end = datetime.datetime.today()
		runtime = end - start
	
		self.assertEqual ( self.sss.tickAccum.seconds, 2, "Should show 2 seconds" )
		self.assertEqual ( runtime.seconds, rt, "The runtime should be about 4 seconds")
	def test_StarShipSystem_tick_failAccums( self ) :
		""" Test that the failAccum accums over time """
		import datetime
		pass
	def notest_StarShipSystem_tick_functionalStatus( self ) :
		""" Test that the functionalStatus updates """
		self.sss.setFunctionalStatus( 100 )
		self.sss.setOperationalStatus( 100 )
		self.sss.setReliabilityFactor( 0 )
		self.sss.failInterval = datetime.timedelta( seconds=1 )
		count = 0
		while( count< 10000000 ) :
			self.sss.tick()
			count += 1
			if self.sss.functionalStatus == 0 :
				print "Failed at", count, "ticks"
				break
		print self.sss.functionalStatus, self.sss.operationalStatus, self.sss.reliabilityFactor
	def test_StarShipSystem_setSupply( self ) :
		""" Test that the system can have an energy supply set """
		testSupply = self.SupplyTest()
		self.sss.setEnergySupply( testSupply )
	def test_StarShipSystem_setUpdateCallback( self ) :
		""" Test that a function can be set as a call back when an update happens """
		def callMe() :
			print "Called Me"
		self.sss.setUpdateCallback( None )
		self.sss.setUpdateCallback( callMe )
	def test_StarShipSystem_seperateObjects( self ):
		self.sss2 = StarShipSystem()
		self.sss.setFunctionalStatus(100)
		self.assertEqual( self.sss.getFunctionalStatus(), 100 )
		self.assertEqual( self.sss2.getFunctionalStatus(), 0 )		
	def test_StarShipSystem_setUpdateCallback_tick(self):
		""" Test that the callback is called when it should by tick() """
		class simple( object ) :
			count = 0
			def callMe( self ) :
				self.count +=1
				return self.count
		s = simple()
		self.sss.setFunctionalStatus( 100 )
		self.sss.setUpdateCallback( s.callMe )
		c = 0
		while ( s.count < 2 ) :
			c += 1
			self.sss.tick()
		called = s.count
		print ( "2 seconds took %i ticks." % (c,))
		self.assertEqual( called, 2 )

if __name__=="__main__": 		
	unittest.main()

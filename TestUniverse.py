#!/usr/bin/env python
""" $Id: TestUniverse.py 2368 2010-08-10 04:41:33Z opus $

"""
import Universe

import unittest
class testUniverse( unittest.TestCase ):
	uid = None
	def setUp( self ):
		self.u = Universe.Universe()
		if self.uid is None:
			self.uid = id( self.u )
	def tearDown( self ):
		#print "UniverseID:", id(self.u)
		self.assertEqual( id( self.u ), self.uid )
		self.u = None
	def test_Universe_initIsDateTimeObject( self ):
		import datetime
		self.assertEqual( type( self.u.inited ), type( datetime.datetime.now() ) )
	def test_Universe_addObject_generic( self ):
		import MassObject
		mo = MassObject.MassObject()
		self.u.addObject( mo )
		self.failUnless( id(mo) in self.u.objects.keys() )
	def test_Universe_addObject_person( self ):
		import Person
		p = Person.Person()
		self.u.addObject( p )
		self.failUnless( id(p) in self.u.objects.keys() )
	def test_Universe_addObject_nonMassObject( self ):
		i = int( 1 )
		self.failUnlessRaises( TypeError, self.u.addObject, i )
	def test_Universe_tick01( self ):
		self.u.tick()
	def test_Universe_tick02( self ):
		import Person
		p = Person.Person()
		self.u.addObject( p )
		self.u.tick()
	

if __name__=="__main__": 
	unittest.main()

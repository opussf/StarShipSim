#!/usr/bin/env python
""" $Id: StarShipTestsuite.py 2379 2010-08-10 04:53:06Z opus $
"""

import unittest
import xmlrunner
#import Shield
#import EnergyConduit

modules = ['TestMassObject','TestRecycleSystem','TestItemSupply',
		   'TestUniverse','TestStarShipSystem','TestEnergyGeneration',
		   'TestEnergySupply','TestEnergyConduit','TestShield','TestWeapon',
		   'TestWarpEngine','TestImpulseEngine', # TestLocation
		   'TestShuttleCraft','TestMedical','TestPerson','TestStarShip',
		   'TestTurboElevatorSystem','TestTransporter','TestLifeSupport',
		   'TestEngineering','TestTickable','TestCoord','TestTrajectory']

ts = unittest.TestLoader().loadTestsFromNames(modules)
StarShipTestsuite = unittest.TestSuite()
StarShipTestsuite.addTests(ts)

#StarShipTestsuite = unittest.TestLoader().loadTestsFromNames(modules)
#unittest.TextTestRunner(verbosity=2).run(StarShipTestsuite)
if __name__=="__main__":
	xmlrunner.XMLTestRunner( verbose=True ).run( StarShipTestsuite )

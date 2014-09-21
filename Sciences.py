#!/usr/bin/env python
""" Sciences.py

	Sciences module
"""

import Engineering
import LifeSupport

class Sciences( object ) :
	""" Sciences
	
	Sciences has the following modules:
		LifeSupport
		Others (TBD)
	"""
	objects = None
	def __init__( self, eng ) :
		""" takes eng so that it can get powerSupplies
		"""
		print "Init of sciences"
		self.eng = eng
		
		
		

if __name__ == "__main__" :
	eng = Engineering.Engineering()
	sci = Sciences( eng )
	
	
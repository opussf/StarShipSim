#!/usr/bin/env python
"""StarShipSim.py

	This is the simulation controller.
"""

import StarShip
import logging

# start logging
StarShipSimLog = logging.getLogger(name="StarShipSim")

# Create a starship
Enterprise = StarShip.StarShip(log = StarShipSimLog)

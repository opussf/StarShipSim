#!/usr/bin/env python

import wx
from wx import xrc
import Engineering

class EngineeringApp( wx.App ) :
	def OnInit( self ) :
		self.res = xrc.XmlResource( "EngineeringDisplay.xrc" )
		self.init_frame()
		self.startTimer()
		return True
	def init_frame( self ) :
		self.frame = self.res.LoadFrame( None, "EngineeringFrame" )
		self.panel = xrc.XRCCTRL( self.frame, "EngineeringPanel" )
		self.supplyText = xrc.XRCCTRL( self.panel, "EngergySupplyAmount")
		self.supplyGauge = xrc.XRCCTRL( self.panel, "EnergySupplyGauge")
		self.shield = [[],[],[],[],[],[]]
		self.shield[0] = [xrc.XRCCTRL( self.panel, "fore_power"), xrc.XRCCTRL( self.panel, "fore_func") ]
		self.shield[1] = [xrc.XRCCTRL( self.panel, "sb_power"), xrc.XRCCTRL( self.panel, "sb_func") ]
		self.shield[2] = [xrc.XRCCTRL( self.panel, "port_power"), xrc.XRCCTRL( self.panel, "port_func") ]
		self.shield[3] = [xrc.XRCCTRL( self.panel, "aft_power"), xrc.XRCCTRL( self.panel, "aft_func") ]
		self.shield[4] = [xrc.XRCCTRL( self.panel, "vent_power"), xrc.XRCCTRL( self.panel, "vent_func") ]
		self.shield[5] = [xrc.XRCCTRL( self.panel, "dorsal_power"), xrc.XRCCTRL( self.panel, "dorsal_func") ]
		for g in self.shield :
			g[1].SetRange(100)
		
		self.frame.Bind( wx.EVT_SCROLL, self.OnForeShieldSlider, id=xrc.XRCID('fore_op') )
		self.frame.Bind( wx.EVT_SCROLL, self.OnSBShieldSlider, id=xrc.XRCID('sb_op') )
		self.frame.Bind( wx.EVT_SCROLL, self.OnPortShieldSlider, id=xrc.XRCID('port_op') )
		self.frame.Bind( wx.EVT_SCROLL, self.OnAftShieldSlider, id=xrc.XRCID('aft_op') )
		self.frame.Bind( wx.EVT_SCROLL, self.OnVentShieldSlider, id=xrc.XRCID('vent_op') )
		self.frame.Bind( wx.EVT_SCROLL, self.OnDorsalShieldSlider, id=xrc.XRCID('dorsal_op') )
		self.eng = Engineering.Engineering()
		self.supplyGauge.SetRange( self.eng.energySupply.maxQuantity )
		print self.eng.energySupply.getStatus(), self.eng.energySupply.maxQuantity
		self.frame.Show()
	def startTimer( self ) :
		self.t1 = wx.Timer( self, id=1 )
		self.t1.Start(100)
		self.Bind( wx.EVT_TIMER, self.OnTimer)
	def OnForeShieldSlider( self, evt ) :
		#print "Fore",evt.GetPosition()
		self.eng.shields[0].setOperationalStatus( evt.GetPosition() )
	def OnSBShieldSlider( self, evt ) :
		#print "Starboard",evt.GetPosition()
		self.eng.shields[1].setOperationalStatus( evt.GetPosition() )
	def OnPortShieldSlider( self, evt ) :
		#print "Port",evt.GetPosition()
		self.eng.shields[2].setOperationalStatus( evt.GetPosition() )
	def OnAftShieldSlider( self, evt ) :
		#print "Aft",evt.GetPosition()
		self.eng.shields[3].setOperationalStatus( evt.GetPosition() )
	def OnVentShieldSlider( self, evt ) :
		#print "Ventral",evt.GetPosition()
		self.eng.shields[4].setOperationalStatus( evt.GetPosition() )
	def OnDorsalShieldSlider( self, evt ) :
		#print "Dorsal",evt.GetPosition()
		self.eng.shields[5].setOperationalStatus( evt.GetPosition() )
		
	def OnTimer( self, evt ) :
		print "OnTimer",
		self.updateFromEng()
	def updateFromEng( self ) :
		self.eng.tick()
		#print self.eng.energySupply.getStatus()
		self.supplyGauge.SetValue( self.eng.energySupply.getStatus()[0] )
		str = "%s (%s)" % ( self.eng.energySupply.getStatus()[0], self.eng.energyGeneration.getReactiveMass()[0] )
		self.supplyText.SetValue( str )
		for s in range(6) :
			print self.eng.shields[s].getStatus(),
			self.shield[s][0].SetRange( self.eng.shields[s].getMaxEnergy() )
			self.shield[s][0].SetValue( self.eng.shields[s].getStatus()[0] )
			self.shield[s][1].SetValue( self.eng.shields[s].getFunctionalStatus() )
		print
		
		
if __name__ == "__main__" :
	app = EngineeringApp(False)
	app.MainLoop()
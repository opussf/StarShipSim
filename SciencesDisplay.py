#!/usr/bin/env python

import wx
from wx import xrc
import Sciences
import Engineering

class SciencesApp( wx.App ) :
	def OnInit( self ) :
		self.res = xrc.XmlResource( "SciencesDisplay.xrc" )
		self.init_frame()
		self.startTimer()
		return True
	def init_frame( self ) :
		self.frame = self.res.LoadFrame( None, "SciencesFrame" )
		self.panel = xrc.XRCCTRL( self.frame, "SciencesPanel" )
		self.supplyText = xrc.XRCCTRL( self.panel, "EngergySupplyAmount")
		self.supplyGauge = xrc.XRCCTRL( self.panel, "EnergySupplyGauge")
		self.eng = Engineering.Engineering()
		self.sci = Sciences.Sciences()
		self.supplyGauge.SetRange( self.eng.energySupply.maxQuantity )
		self.frame.Show()
	def startTimer( self ) :
		self.t1 = wx.Timer( self, id=1 )
		self.t1.Start(100)
		self.Bind( wx.EVT_TIMER, self.OnTimer)
	def OnTimer( self, evt ) :
		self.updateFromEng()
		self.updateFromSci()
	def updateFromEng( self ) :
		self.eng.tick()
		#print self.eng.energySupply.getStatus()
		self.supplyGauge.SetValue( self.eng.energySupply.getStatus()[0] )
		str = "%s (%s)" % ( self.eng.energySupply.getStatus()[0], self.eng.energyGeneration.getReactiveMass()[0] )
		self.supplyText.SetValue( str )
	def updateFromSci( self ) :
		self.sci.tick()

if __name__ == "__main__" :
	app = SciencesApp( False )
	app.MainLoop()
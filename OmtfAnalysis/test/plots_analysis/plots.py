#!/cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw/CMSSW_12_4_8/external/slc7_amd64_gcc10/bin/python3

#import ROOT
import sys
import math
#import libPyROOT
from ROOT import *

import plotsDataEmul
import plotsEff
import plotsEvent
import plotsMuon
import plotsTime
import plotsMenu
import plotsSynch
import plotsSecMuSel
import plotsDiMu
import plotsL1Dist

print("Hello ROOT")
fileName = "../omtfAnalysis.root"

print ('Read data from: ', fileName)
gROOT.Reset()
f = TFile(fileName);
f.ls();

#--------- HERE plots

canvas = TObjArray()
#plotsEvent.plotAll(canvas)
#plotsMuon.plotAll(canvas)
#plotsEff.plotAll(canvas)
#    plotsSecMuSel.plotAll(canvas)
#plotsDataEmul.plotAll(canvas)
plotsTime.plotAll(canvas)

#plotsMenu.plotAll(canvas)
#plotsSynch.plotAll(canvas)
#plotsDiMu.plotAll(canvas)
#plotsL1Dist.plotAll(canvas)

#--------- HERE pause 
input('press enter to exit')

#--------- HERE plots
for canva in canvas :
  canvaName =  canva.ClassName()
  if canvaName != 'TCanvas' : continue
  pictName  = "fig_png/"+canva.GetName()+".png"
  canva.Print(pictName,'png')




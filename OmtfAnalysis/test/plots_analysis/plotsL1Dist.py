#!/usr/bin/python

import sys
import math
from ROOT import *
from plotsUtils import *

def cL1DistOmtfLayers(canvas):
  c = TCanvas("cL1MDistOmtf","cL1DistOmtf",1000,600)
  canvas.Add(c)

  hQ0=gROOT.FindObject("hL1DistOmtfLayers")
  hQ0.SetStats(0)
  hQ0.SetMinimum(0.)
  hQ0.DrawCopy()

  h=gROOT.FindObject("hL1DistOmtfLayersQ12")
  h.SetLineColor(1)
  h.DrawCopy('same')

  h.SetFillColor(2)
  h.SetFillStyle(3345)
  h.GetXaxis().SetRange(1,6)
  h.DrawCopy('same')

  h.SetFillColor(4)
  h.SetFillStyle(3344)
  h.GetXaxis().SetRange(7,10)
  h.DrawCopy('same')

  h.SetFillColor(8)
  h.SetFillStyle(3354)
  h.GetXaxis().SetRange(11,18)
  h.DrawCopy('same')

#  line = TLine()
#  line.SetLineColor(2)
#  line.DrawLine(5.5,0.5,5.5,vMax)
  c.Update()
  return

def cL1DistBoard(canvas):
  c = TCanvas("cL1DistBoard","cL1DistBoard",1200,600)
  canvas.Add(c)
  c.Divide(2)
  c.cd(1)
  hE= gROOT.FindObject("hL1DistBoardEta")
  hE.SetStats(0)
  hE.DrawCopy('box text' )
  c.cd(2)
  hP= gROOT.FindObject("hL1DistBoardPhi")
  hP.SetStats(0)
  hP.DrawCopy('box text' )
  c.Update()
  return

def cL1DistDeltaR(canvas):
  c = TCanvas("cL1DistDeltaR","cL1DistDeltaR",1200,400)
  canvas.Add(c)
  c.Divide(3)
  p1 = c.cd(1)
  h= gROOT.FindObject("hL1Dist_DeltaR_Bar")
  p1.SetLogx() 
  h.SetStats(0)
  h.GetXaxis().SetRange(4,20)
  h.DrawCopy('colz')
  p2 = c.cd(2)
  h= gROOT.FindObject("hL1Dist_DeltaR_Ove")
  p2.SetLogx() 
  h.SetStats(0)
  h.GetXaxis().SetRange(4,20)
  h.DrawCopy('colz')
  p3 = c.cd(3)
  h= gROOT.FindObject("hL1Dist_DeltaR_End")
  p3.SetLogx() 
  h.SetStats(0)
  h.GetXaxis().SetRange(4,20)
  h.DrawCopy('colz')


def plotAll(canvas) :
  cL1DistOmtfLayers(canvas)
  cL1DistBoard(canvas)
  cL1DistDeltaR(canvas)
  return



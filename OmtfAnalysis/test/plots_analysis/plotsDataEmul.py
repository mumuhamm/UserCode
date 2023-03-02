#!/usr/bin/python

import sys
import math
from ROOT import *
from plotsUtils import *

def cDataEmulDistribution(canvas):
  c = TCanvas("cDataEmulDistribution","cDataEmulDistribution",1200,600)
  canvas.Add(c)
  c.Divide(2)
  c.cd(1)
  hE=gROOT.FindObject("hDataEmulDistributionData")
  hE.SetStats(0)
#  hE.Print("all")
  hE.DrawCopy('box text' )
  c.cd(2)
  hP= gROOT.FindObject("hDataEmulDistributionEmul")
  hP.SetStats(0)
  hP.DrawCopy('box text' )
  c.Update()
  return

def cDataEmulNotAgree(canvas):
  c = TCanvas("cDataEmulNotAgree","cDataEmulNotAgree",1200,600)
  canvas.Add(c)
  c.Divide(2)
  c.cd(1)
  hE= gROOT.FindObject("hDataEmulNotAgreeEta")
  hE.SetStats(0)
  hE.DrawCopy('box text' )
  c.cd(2)
  hP= gROOT.FindObject("hDataEmulNotAgreePhi")
  hP.SetStats(0)
  hP.DrawCopy('box text' )
  c.Update()
  return

def cDataEmulPt(canvas):
  c = TCanvas('cDataEmulPt','cDataEmulPt',900,900)
  canvas.Add(c)
  h = gROOT.FindObject('hDataEmulPt')
  h.SetStats(0)
  h.GetXaxis().SetRange(5,32)
  h.GetYaxis().SetRange(5,32)
  h.GetXaxis().SetTitleOffset(1.4)
  h.GetYaxis().SetTitleOffset(1.4)
  h.SetXTitle("data p_{T} [GeV]");
  h.SetYTitle("emul p_{T} [GeV]");
  h.SetMarkerSize(0.65)
  c.SetLogx() 
  c.SetLogy() 
  h.DrawCopy('colo text')
  c.Update()
  return

def cDataEmulPhi(canvas):
  c = TCanvas('cDataEmulPhi','cDataEmulPhi',600,600)
  canvas.Add(c)
  h = gROOT.FindObject('hDataEmulPhi')
  h.SetStats(0)
  h.GetXaxis().SetTitleOffset(1.4)
  h.GetYaxis().SetTitleOffset(1.4)
  h.SetXTitle("data phi [GMT code]");
  h.SetYTitle("emul phi [GMT code]");
  h.DrawCopy('colo')
  return

def cDataEmulEta(canvas):
  c = TCanvas('cDataEmulEta','cDataEmulEta',850,800)
  canvas.Add(c)
  h = gROOT.FindObject('hDataEmulEta')
  h.SetStats(0)
  c.SetTopMargin(0.07)
  c.SetLeftMargin(0.17)
  h.GetXaxis().SetTitleOffset(1.5)
  h.GetYaxis().SetTitleOffset(2.5)
  h.SetXTitle("data eta [GMT code]")
  h.SetYTitle("emul eta [GMT code]")
  h.DrawCopy('box')
  return

def cDataEmulIssue(canvas):
  c = TCanvas('cDataEmulIssue','cDataEmulIssue',600,600)
  canvas.Add(c)
  c.SetRightMargin(0.01)
  c.SetLogy()
  c.SetGridy()
  c.SetTicky()
  h = gROOT.FindObject('hDataEmulIssue')
  nEvnts = h.GetBinContent(1)
  h.Scale(1/nEvnts)
  h.SetMaximum(1.5)
  h.SetMinimum(1.5e-4)
  h.SetStats(0)
  h.GetXaxis().SetRange(2,7)
  h.GetYaxis().SetTitleOffset(1.5)
  h.SetYTitle("event fraction");
  h.DrawCopy()
  c.Update()
  return

def cDataEmulHistory(canvas):
  c = TCanvas('cDataEmulHistory','cDataEmulHistory',1200,600)
  canvas.Add(c)
  gr = gROOT.FindObject('hGraphDataEmulHistory')
  gr.SetName('DataEmulHistory')
  h = runHistoFromGraph(gr)
  fillHistoFromGraph(h,gr)
  h.SetStats(0)
  h.DrawCopy()
  c.Update()
  return

def cDataEmulCompare(canvas):
  c = TCanvas('cDataEmulCompare','cDataEmulCompare',1200,600)
  canvas.Add(c)
  c.Divide(2)
  pad1 = c.cd(1)
  pad1.SetRightMargin(0.01)
  h = gROOT.FindObject('hDataEmulCompare')
  nEvnts = h.GetEntries()
  h.Scale(1/nEvnts)
  h.SetMinimum(1.e-4)
  h.SetStats(0)
  h.Print("all") 
  h.DrawCopy()
  pad2 = c.cd(2)
  pad2.SetLeftMargin(0.14)
  h = gROOT.FindObject('hDataEmulCompareComb')
  h.SetStats(0)
  h.DrawCopy('text')
  c.Update()
  return

def cDataEmulBX(canvas):
  c = TCanvas('cDataEmulBX','cDataEmulBX',1200,600)
  canvas.Add(c)
  c.Divide(2)
  pad1 = c.cd(1)
#  pad1.SetRightMargin(0.01)
  hD = gROOT.FindObject('hDataEmulBxD')
  hE = gROOT.FindObject('hDataEmulBxE')
  print ('hDataEmulBxD : ',hD.GetEntries(),' entries')
  print ('hDataEmulBxE : ',hE.GetEntries(),' entries')
#  h.Scale(1/nEvnts)
#  h.SetMinimum(1.e-4)
  hE.SetLineColor(4)
  hE.SetFillColor(4)
  hE.SetFillStyle(3354)
  hE.SetStats(0)
  hE.DrawCopy('')
  hE.DrawCopy('text same')
  hD.SetLineColor(2)
  hD.SetFillColor(2)
  hD.SetFillStyle(3345)
  hD.DrawCopy('same')
  pad2 = c.cd(2)
  pad2.SetLeftMargin(0.14)
  h = gROOT.FindObject('hDataEmulCheckProb')
  h.SetStats(0)
  h.DrawCopy('text')
  wrong = 0
  all  = 0
  for binx in range(1,h.GetNbinsX()+1) :
    for biny in range(1,h.GetNbinsY()+1) :
      if (biny != 1) : wrong +=  h.GetBinContent(binx,biny)
      all +=  h.GetBinContent(binx,biny)
  print (" all: ",all," wrong: ",wrong)
  xpos=0.60
  ypos=0.86
  legendFontSize = 0.030
  t=TLatex()
  t.SetNDC(1)
  t.SetTextSize(legendFontSize)
  t.SetTextColor(2)
  aver ="Avg wrong = {0:.4f}".format(wrong/all)
  t.DrawLatex(xpos, ypos, aver)
  c.Update()
  return


def plotAll(canvas) :
  cDataEmulPhi(canvas)
  cDataEmulEta(canvas)
  cDataEmulNotAgree(canvas)
  cDataEmulIssue(canvas)
#  cDataEmulHistory(canvas)
  cDataEmulPt(canvas)
  cDataEmulCompare(canvas)
  cDataEmulDistribution(canvas)
  cDataEmulBX(canvas)
  return

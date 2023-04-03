#!/cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw/CMSSW_12_4_8/external/slc7_amd64_gcc10/bin/python3

from ROOT import *
gROOT.Reset()
#f = TFile('../omtfHelper.root');
#f = TFile('../../jobs/vc_Muon/crab_Run2022G/omtfHelper.root');
f = TFile('../../jobs/vd_JetMET/crab_Run2022G/omtfHelper.root');
#f = TFile('../../jobs/v6_Express/crab_Run2022G_from362755/omtfHelper.root');
f.ls();


detBxStat=DetBxStatObj()
cycle=1
while gROOT.FindObject(detBxStat.GetName()+";"+str(cycle)) :
  nameObj=detBxStat.GetName()+";"+str(cycle)
  detBxStat+=gROOT.FindObject(nameObj)
#  print ("cycle: ",cycle, nameObj)
  cycle+=1
detBxStat.print()
print ("---")

detPullXStat=DetBxStatObj("DetPullXStat")
cycle=1
while gROOT.FindObject(detPullXStat.GetName()+";"+str(cycle)) :
  nameObj=detPullXStat.GetName()+";"+str(cycle)
  detPullXStat+=gROOT.FindObject(nameObj)
#  print ("cycle: ",cycle, nameObj)
  cycle+=1
#detPullXStat.print()
print ("---")

def table (h):
  print ('chamber   bx=-1   bx=0  bx=+1')
  for ch in range(1,37):
    bCh=h.GetXaxis().FindBin(ch)
    vm1= h.GetBinContent(bCh,h.GetYaxis().FindBin(-1))
    v0 = h.GetBinContent(bCh,h.GetYaxis().FindBin( 0))
    vp1= h.GetBinContent(bCh,h.GetYaxis().FindBin( 1))
    print ('{0:5s}/{1:2d} {2:6.0f} {3:6.0f} {4:6.0f}'.format(h.GetTitle()[1:6],bCh,vm1,v0,vp1))
   
c1=TCanvas("cME13_Inside","cME13_Inside",1000,600)
c1.Divide(1,2)
c1.cd(1)
hP=gROOT.FindObject("hME13P_Inside")
hP.SetStats(0)
hP.GetYaxis().SetNdivisions(107)
hP.SetYTitle(" BX ")
hP.SetXTitle(" chamber ")
hP.DrawCopy('box text')
#table(hP)

c1.cd(2)
hN=gROOT.FindObject("hME13N_Inside")
hN.SetStats(0)
hN.SetYTitle(" BX ")
hN.SetXTitle(" chamber ")
hN.GetYaxis().SetNdivisions(107)
hN.DrawCopy('box text')
#table(hN)
c1.Update()
c1.Print(c1.GetName()+".png","png")

c2=TCanvas("cME13_Strip","cME13_Strip",1000,600)
c2.Divide(1,2)
c2.cd(1)
hP=gROOT.FindObject("hME13P_Strip")
hP.SetStats(0)
hP.GetYaxis().SetNdivisions(107)
hP.SetYTitle(" BX ")
hP.SetXTitle(" chamber ")
hP.DrawCopy('box text')
c2.cd(2)
hN=gROOT.FindObject("hME13N_Strip")
hN.SetStats(0)
hN.SetYTitle(" BX ")
hN.SetXTitle(" chamber ")
hN.GetYaxis().SetNdivisions(107)
hN.DrawCopy('box text')
c2.Update()
c2.Print(c2.GetName()+".png","png")
  
def plot_chambers(name, wd, sr) :
  print ('chambers:', name, wd, sr, DetSpecObj.DET.CSC)
  if name=='RPCe' or name=='CSC' :
    maxch = 36
  else :
    maxch = 12
  title=name+'_'+str(wd)+'_'+str(sr)+'_xx' 
  c=TCanvas('c'+title,title,1000,500)
  h=TH2D(title,title,maxch,1-0.5,maxch+0.5, 7,-3.5,3.5)
  for ch in range(1,maxch+1) :
    bxStat = detBxStat.getBxStat( DetSpecObj(DetSpecObj.name2type(name), wd, sr, ch) ) 
    for bx in range(-3,4) :
      h.Fill(ch, bx, bxStat(bx))

  h.SetStats(0)
  h.SetYTitle(" BX ")
  h.SetXTitle(" chamber ")
  h.GetYaxis().SetNdivisions(107)
  h.DrawCopy('box text')
  c.Update()
  c.Print(c.GetName()+".png")
#  input("press a key")

#bxstat = detBxStat.getBxStat( DetSpecObj(DetSpecObj.DET.RPCe, 1,2,24) )
#bxstat.print()

c3A=TCanvas("cDistStripRpc","cDistStripRpc",1000,500)
c3A.Divide(2)
c3A.cd(1)
h=gROOT.FindObject("hRpcDistX")
h.DrawCopy()
c3A.cd(2)
h=gROOT.FindObject("hRpcPullX")
h.DrawCopy()
c3A.Update()
c3A.Print(c3A.GetName()+".png","png")

c3B=TCanvas("cDistStripCsc","cDistStripCsc",1000,500)
c3B.Divide(2)
c3B.cd(1)
h=gROOT.FindObject("hCscDistX")
h.DrawCopy()
c3B.cd(2)
h=gROOT.FindObject("hCscPullX")
h.DrawCopy()
c3B.Update()
c3B.Print(c3B.GetName()+".png")

c3C=TCanvas("cCompHit","cCompHit",1000,500)
c3C.Divide(2)
c3C.cd(1)
h=gROOT.FindObject("hRpcHitDistX")
h.DrawCopy()
c3C.cd(2)
h=gROOT.FindObject("hCscHitDistX")
h.DrawCopy()
c3C.Update()
c3C.Print(c3C.GetName()+".png","png")

c4=TCanvas("cCscDistr","cCscDistr",800,800)
h=gROOT.FindObject("hCscDistr")
h.DrawCopy()
c4.Print(c4.GetName()+".png","png")

c5=TCanvas("cDistHitPhi","cDistHitPhi",800,400)
c5.Divide(2)
c5.cd(1)
h=gROOT.FindObject("hRpcHitDistPhi")
h.DrawCopy()
c5.cd(2)
h=gROOT.FindObject("hCscHitDistPhi")
h.DrawCopy()
h.DrawCopy()
c5.Update()
c5.Print(c5.GetName()+".png","png")

c6=TCanvas("cRPC","cRPC",500,800)
c6.Divide(1,2)
c6.cd(1)
h=gROOT.FindObject("hDistX_Muon")
h.DrawCopy()
c6.cd(2)
h=gROOT.FindObject("hPullX_Muon")
h.DrawCopy()
h.DrawCopy()
c6.Update()
c6.Print(c6.GetName()+".png","png")

c7=TCanvas("cDtBxQ","cDtBxQ",1000,500)
c7.Divide(2,1)
c7.cd(1)
h=gROOT.FindObject("hDtBxQ2")
h.DrawCopy()
h.Print("all")
c7.cd(2)
h=gROOT.FindObject("hDtBxQ4")
h.DrawCopy()
h.Print("all")
c7.Update()
c7.Print(c7.GetName()+".png","png")

c8=TCanvas("cDtPhi","cDtPhi",1000,500)
c8.Divide(2,1)
c8.cd(1)
h=gROOT.FindObject("hDtPhi")
h.DrawCopy()
c8.cd(2)
h=gROOT.FindObject("hDtDPhi")
h.DrawCopy()
c8.Update()
c8.Print(c8.GetName()+".png","png")

#f.ls()


plot_chambers('CSC',  -4, 2) 
plot_chambers('CSC',  -3, 2) 
plot_chambers('CSC',  -2, 2) 
plot_chambers('CSC',  -1, 2) 
plot_chambers('CSC',  -1, 3) 
plot_chambers('CSC',   1, 3) 
plot_chambers('CSC',   1, 2) 
plot_chambers('CSC',   2, 2) 
plot_chambers('CSC',   3, 2) 
plot_chambers('CSC',   4, 2) 

plot_chambers('RPCe',-3,3)
plot_chambers('RPCe',-2,3)
plot_chambers('RPCe',-1,3)
plot_chambers('RPCe',-1,2)

plot_chambers('RPCb',-2,1)
plot_chambers('RPCb',-2,2)
plot_chambers('RPCb',-2,3)
plot_chambers('RPCb',-2,4)

plot_chambers('RPCb', 2,1)
plot_chambers('RPCb', 2,2)
plot_chambers('RPCb', 2,3)
plot_chambers('RPCb', 2,4)

plot_chambers('RPCe', 1,2)
plot_chambers('RPCe', 1,3)
plot_chambers('RPCe', 2,3)
plot_chambers('RPCe', 3,3)
 
def plot_BxStatChamber(name, wd, sr, histo) :
  if name=='RPCe' or name=='CSC' :
    maxch = 36
  else :
    maxch = 12
  for ch in range(1,maxch+1) :
    bxStat = detBxStat.getBxStat( DetSpecObj(DetSpecObj.name2type(name), wd, sr, ch) ) 
    for bx in range(-3,4) :
      histo.Fill(bx, bxStat(bx))


def plot_BxStatRPC() :
  c=TCanvas('c_BxStat_RPC','c_BxStat_RPC',1500,400)
  c.Divide(4,1)
  h=TH1D('h_BxStat_RPC','h_BxStat_RPC',8,-3.5,4.5)
  h.SetStats(0)
  h.SetXTitle(" BX ")
  h.SetYTitle("#events")
  h.GetYaxis().SetNdivisions(107)

  p=c.cd(1)
  p.SetLogy()
  h.SetTitle('RPC_e-')
  plot_BxStatChamber('RPCe',-3,3,h)
  plot_BxStatChamber('RPCe',-2,3,h)
  plot_BxStatChamber('RPCe',-1,3,h)
  plot_BxStatChamber('RPCe',-1,2,h)
  h.DrawCopy('histo')

  p=c.cd(2)
  p.SetLogy()
  h.Reset()
  h.SetTitle('RPC_w-2')
  plot_BxStatChamber('RPCb',-2,1,h)
  plot_BxStatChamber('RPCb',-2,2,h)
  plot_BxStatChamber('RPCb',-2,3,h)
  plot_BxStatChamber('RPCb',-2,4,h)
  h.DrawCopy('histo')

  p=c.cd(3)
  p.SetLogy()
  h.Reset()
  h.SetTitle('RPC_w+2')
  plot_BxStatChamber('RPCb', 2,1,h)
  plot_BxStatChamber('RPCb', 2,2,h)
  plot_BxStatChamber('RPCb', 2,3,h)
  plot_BxStatChamber('RPCb', 2,4,h)
  h.DrawCopy('histo')

  p=c.cd(4)
  p.SetLogy()
  h.Reset()
  h.SetTitle('RPC_e+')
  plot_BxStatChamber('RPCe', 1,2,h)
  plot_BxStatChamber('RPCe', 1,3,h)
  plot_BxStatChamber('RPCe', 2,3,h)
  plot_BxStatChamber('RPCe', 3,3,h)
  h.DrawCopy('histo')

  c.Update()
  c.Print(c.GetName()+".png")
  input("press a key")

def plot_BxStatCSC() :
  c=TCanvas('c_BxStat_CSC','c_BxStat_CSC',900,400)
  c.Divide(2,1)
  h=TH1D('h_BxStat_CSC','h_BxStat_CSC',8,-3.5,4.5)
  h.SetStats(0)
  h.SetXTitle(" BX ")
  h.SetYTitle("#events")
  h.GetYaxis().SetNdivisions(107)

  p=c.cd(1)
  p.SetLogy()
  h.SetTitle('CSC-')
  plot_BxStatChamber('CSC',-4,2,h)
  plot_BxStatChamber('CSC',-3,2,h)
  plot_BxStatChamber('CSC',-2,2,h)
  plot_BxStatChamber('CSC',-1,2,h)
  plot_BxStatChamber('CSC',-1,3,h)
  h.DrawCopy('histo')

  p=c.cd(2)
  p.SetLogy()
  h.Reset()
  h.SetTitle('CSC+')
  plot_BxStatChamber('CSC', 4,2,h)
  plot_BxStatChamber('CSC', 3,2,h)
  plot_BxStatChamber('CSC', 2,2,h)
  plot_BxStatChamber('CSC', 1,2,h)
  plot_BxStatChamber('CSC', 1,3,h)
  h.DrawCopy('histo')

  c.Update()
  c.Print(c.GetName()+".png")
  input("press a key")

plot_BxStatRPC()
plot_BxStatCSC()

input("press a key")


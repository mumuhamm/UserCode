#include "UserCode/OmtfAnalysis/interface/AnaL1Distribution.h"

#include "TObjArray.h"
#include "TH1D.h"
#include "TH2D.h"
#include "UserCode/OmtfDataFormats/interface/TrackObj.h"
#include "UserCode/OmtfDataFormats/interface/MuonObj.h"
#include "UserCode/OmtfDataFormats/interface/MuonObjColl.h"
#include "UserCode/OmtfDataFormats/interface/EventObj.h"
#include "UserCode/OmtfDataFormats/interface/L1ObjColl.h"
#include "UserCode/OmtfAnalysis/interface/Utilities.h"
#include "DataFormats/Math/interface/deltaR.h"


#include <ostream>
#include <iostream>
#include <cmath>
#include <bitset>


namespace { 

  TH1D *hL1DistOmtfLayers, *hL1DistOmtfLayersQ12;
  TH2D *hL1DistBoardEta, *hL1DistBoardPhi;

  std::string reg[3]={"_Bar","_Ove","_End"};

}

AnaL1Distribution::AnaL1Distribution(const edm::ParameterSet& cfg)
  : debug(false), theCfg (cfg)
{}

void AnaL1Distribution::init(TObjArray& histos)
{
  unsigned int nOmtfLayers =  omtfUtilities::layerNames.size();
  hL1DistOmtfLayers  = new TH1D("hL1DistOmtfLayers","hL1DistOmtfLayers", nOmtfLayers,-0.5,nOmtfLayers-0.5); histos.Add(hL1DistOmtfLayers); 
  hL1DistOmtfLayersQ12 = new TH1D("hL1DistOmtfLayersQ12","hL1DistOmtfLayersQ12", nOmtfLayers,-0.5,nOmtfLayers-0.5); histos.Add(hL1DistOmtfLayersQ12); 
  for (unsigned int ibin=1; ibin<=nOmtfLayers; ibin++) hL1DistOmtfLayers->GetXaxis()->SetBinLabel(ibin,omtfUtilities::layerNames[ibin-1].c_str()); 


  hL1DistBoardEta = new TH2D("hL1DistBoardEta","hL1DistBoardEta",13,-6.5, 6.5, omtfUtilities::nEtaBins, 0.5, omtfUtilities::nEtaBins+0.5); histos.Add(hL1DistBoardEta);
  hL1DistBoardPhi = new TH2D("hL1DistBoardPhi","hL1DistBoardPhi",13,-6.5, 6.5, 24, -15, 105.); histos.Add(hL1DistBoardPhi);
  for (unsigned int iProc = 0; iProc  <=5; iProc++) {
    for (int endcap = -1; endcap <=1; endcap+=2) {
      OmtfName board(iProc,endcap);
      hL1DistBoardEta->GetXaxis()->SetBinLabel( board+7, board.name().c_str());
      hL1DistBoardPhi->GetXaxis()->SetBinLabel( board+7, board.name().c_str());
    }
  }
  for (unsigned int ibin=1; ibin <= omtfUtilities::nEtaBins; ibin++) {
    int etaCode = omtfUtilities::etaBinVal[ibin-1];
    std::string slabel = std::to_string( etaCode );
    hL1DistBoardEta->GetYaxis()->SetBinLabel( ibin, slabel.c_str());
  }

 
  std::string base("hL1Dist");
  for (unsigned int ir=0; ir<3; ++ir) {
    std::string name=base+"_DeltaR"+reg[ir];
    TH2D *h= new TH2D(name.c_str(),name.c_str(), L1PtScale::nPtBins, L1PtScale::ptBins, 20, 0.,1. ); h->Sumw2();
    histos.Add(h); theHistoMap[name]=h;
  }


}

void AnaL1Distribution::run(const EventObj* ev, const MuonObjColl *muonColl, const TrackObj* track, const L1ObjColl * l1Objs)
{

  L1Obj::TYPE typeOMTF = L1Obj::OMTF;
  L1ObjColl omtfColl = l1Objs->selectByType(typeOMTF);
  std::vector<L1Obj> vdata = omtfColl.selectByBx(0,0);
  //
  // all triggers
  //
  for (const auto & mu : vdata) {
    std::bitset<18> hitLayers(mu.hits);
    for (unsigned int hitLayer=0; hitLayer<18;hitLayer++) if(hitLayers[hitLayer]) {
      hL1DistOmtfLayers->Fill(hitLayer);
      if (mu.q>=12) hL1DistOmtfLayersQ12->Fill(hitLayer);
    }
    hL1DistBoardEta->Fill( OmtfName(mu.iProcessor, mu.position), omtfUtilities::code2HistoBin(abs(mu.eta)) );
    hL1DistBoardPhi->Fill( OmtfName(mu.iProcessor, mu.position), mu.phi );
  }


  //
  // how far is closest muon to the L1 muon track  BX=0
  //
  const std::vector<L1Obj>  l1mtfs = l1Objs->selectByType(L1Obj::uGMT).selectByBx(0,0);
  const std::vector<MuonObj> & muons = *muonColl;
  for (const auto & l1mtf : l1mtfs) {
    double bestDR = 999.;
    double bestPt = 0.;
    double bestEta = 999.;
//    bool matched = false;
    for (const auto & muon : muons) {
      if (!muon.isValid()) continue;
      double deltaR = reco::deltaR( l1mtf.etaValue(), l1mtf.phiValue(), muon.l1Eta, muon.l1Phi);
      if (deltaR < bestDR) {
//        if (deltaR < 0.4) matched = true;
        bestDR = deltaR;  
        bestPt = muon.pt();
        bestEta = muon.eta();
      }
    }
    unsigned int iregion;
    if ( fabs(bestEta) < 0.83) iregion = 0;
    else if ( fabs(bestEta) < 1.24) iregion = 1;
    else iregion = 2;
    theHistoMap["hL1Dist_DeltaR"+reg[iregion]]->Fill(bestPt, bestDR);

  }

  
  

}

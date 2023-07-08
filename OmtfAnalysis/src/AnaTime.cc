#include "UserCode/OmtfAnalysis/interface/AnaTime.h"

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
  TH1D *hTimeOmtf_A,  *hTimeBmtf_A,   *hTimeEmtf_A;  
  TH1D *hTimeOmtf_Q,  *hTimeBmtf_Q,   *hTimeEmtf_Q;  
  TH1D *hTimeOmtf_M,  *hTimeBmtf_M,   *hTimeEmtf_M;  
  TH1D *hTimeOmtf_QM, *hTimeBmtf_QM,  *hTimeEmtf_QM;  
  TH1D *hTimeOmtf_W,  *hTimeBmtf_W,  *hTimeEmtf_W;  
  TH1D *hTimeOmtf_QW, *hTimeBmtf_QW, *hTimeEmtf_QW;  
  TH1D *hTimeOmtf_emu_A, *hTimeOmtf_emu_Q, *hTimeOmtf_emu_M, *hTimeOmtf_emu_QM, *hTimeOmtf_emu_W, *hTimeOmtf_emu_QW;

  TH2D *hTimeBmtfOmtf, *hTimeOmtfEmtf, *hTimeOmtfOmtf_E;

  TH1D *hTimeDeltaR_Q, *hTimeDeltaR_QW, 
       *hTimeDeltaR_Q_B1, *hTimeDeltaR_Q_B2, *hTimeDeltaR_Q_B3, 
       *hTimeDeltaR_QW_B1, *hTimeDeltaR_QW_B2, *hTimeDeltaR_QW_B3;
  TH1D *hTimeLayers;

  TH2D *hTimeOmtfTrackDPhiT, *hTimeOmtfTrackDPhiM, *hTimeOmtfTrackDEtaT, *hTimeOmtfTrackDEtaM;
  TH1D *hTimeOmtfTrackDRM;

  TH2D *hTimeOmtfTrackBXT, *hTimeOmtfTrackBXM;
  TH1D *hTimeOmtfTrackBX0, *hTimeOmtfTrackBX1;
  TH2D *hTimeOmtfDrTrackMuon;

template <typename T> int sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

}

AnaTime::AnaTime(const edm::ParameterSet& cfg)
  : debug(false), theCfg (cfg)
{}

void AnaTime::init(TObjArray& histos)
{
  hTimeBmtf_A = new TH1D("hTimeBmtf_A","hTimeBmtf_A",5,-2.5,2.5); histos.Add(hTimeBmtf_A); 
  hTimeBmtf_Q = new TH1D("hTimeBmtf_Q","hTimeBmtf_Q",5,-2.5,2.5); histos.Add(hTimeBmtf_Q); 
  hTimeBmtf_M = new TH1D("hTimeBmtf_M","hTimeBmtf_M",5,-2.5,2.5); histos.Add(hTimeBmtf_M); 
  hTimeBmtf_QM = new TH1D("hTimeBmtf_QM","hTimeBmtf_QM",5,-2.5,2.5); histos.Add(hTimeBmtf_QM); 
  hTimeBmtf_W = new TH1D("hTimeBmtf_W","hTimeBmtf_W",5,-2.5,2.5); histos.Add(hTimeBmtf_W); 
  hTimeBmtf_QW = new TH1D("hTimeBmtf_QW","hTimeBmtf_QW",5,-2.5,2.5); histos.Add(hTimeBmtf_QW); 

  hTimeEmtf_A = new TH1D("hTimeEmtf_A","hTimeEmtf_A",5,-2.5,2.5); histos.Add(hTimeEmtf_A); 
  hTimeEmtf_Q = new TH1D("hTimeEmtf_Q","hTimeEmtf_Q",5,-2.5,2.5); histos.Add(hTimeEmtf_Q); 
  hTimeEmtf_M = new TH1D("hTimeEmtf_M","hTimeEmtf_M",5,-2.5,2.5); histos.Add(hTimeEmtf_M); 
  hTimeEmtf_QM = new TH1D("hTimeEmtf_QM","hTimeEmtf_QM",5,-2.5,2.5); histos.Add(hTimeEmtf_QM); 
  hTimeEmtf_W = new TH1D("hTimeEmtf_W","hTimeEmtf_W",5,-2.5,2.5); histos.Add(hTimeEmtf_W); 
  hTimeEmtf_QW = new TH1D("hTimeEmtf_QW","hTimeEmtf_QW",5,-2.5,2.5); histos.Add(hTimeEmtf_QW); 

  hTimeOmtf_A = new TH1D("hTimeOmtf_A","hTimeOmtf_A",7,-3.5,3.5); histos.Add(hTimeOmtf_A); 
  hTimeOmtf_Q = new TH1D("hTimeOmtf_Q","hTimeOmtf_Q",7,-3.5,3.5); histos.Add(hTimeOmtf_Q); 
  hTimeOmtf_M = new TH1D("hTimeOmtf_M","hTimeOmtf_M",7,-3.5,3.5); histos.Add(hTimeOmtf_M); 
  hTimeOmtf_QM = new TH1D("hTimeOmtf_QM","hTimeOmtf_QM",7,-3.5,3.5); histos.Add(hTimeOmtf_QM); 
  hTimeOmtf_W = new TH1D("hTimeOmtf_W","hTimeOmtf_W",7,-3.5,3.5); histos.Add(hTimeOmtf_W); 
  hTimeOmtf_QW = new TH1D("hTimeOmtf_QW","hTimeOmtf_QW",7,-3.5,3.5); histos.Add(hTimeOmtf_QW); 

  hTimeOmtf_emu_A = new TH1D("hTimeOmtf_emu_A","hTimeOmtf_emu_A",5,-2.5,2.5); histos.Add(hTimeOmtf_emu_A); 
  hTimeOmtf_emu_Q = new TH1D("hTimeOmtf_emu_Q","hTimeOmtf_emu_Q",5,-2.5,2.5); histos.Add(hTimeOmtf_emu_Q); 
  hTimeOmtf_emu_M = new TH1D("hTimeOmtf_emu_M","hTimeOmtf_emu_M",5,-2.5,2.5); histos.Add(hTimeOmtf_emu_M); 
  hTimeOmtf_emu_QM = new TH1D("hTimeOmtf_emu_QM","hTimeOmtf_emu_QM",5,-2.5,2.5); histos.Add(hTimeOmtf_emu_QM); 
  hTimeOmtf_emu_W = new TH1D("hTimeOmtf_emu_W","hTimeOmtf_emu_W",5,-2.5,2.5); histos.Add(hTimeOmtf_emu_W); 
  hTimeOmtf_emu_QW = new TH1D("hTimeOmtf_emu_QW","hTimeOmtf_emu_QW",5,-2.5,2.5); histos.Add(hTimeOmtf_emu_QW); 

  hTimeDeltaR_Q = new TH1D("hTimeDeltaR_Q","hTimeDeltaR_Q",   100,0.,4.);  histos.Add(hTimeDeltaR_Q);
  hTimeDeltaR_QW = new TH1D("hTimeDeltaR_QW","hTimeDeltaR_QW",100,0.,4.);  histos.Add(hTimeDeltaR_QW);
  hTimeDeltaR_Q_B3 = new TH1D("hTimeDeltaR_Q_B3","hTimeDeltaR_Q_B3",100,0.,4.);  histos.Add(hTimeDeltaR_Q_B3);
  hTimeDeltaR_Q_B2 = new TH1D("hTimeDeltaR_Q_B2","hTimeDeltaR_Q_B2",100,0.,4.);  histos.Add(hTimeDeltaR_Q_B2);
  hTimeDeltaR_Q_B1 = new TH1D("hTimeDeltaR_Q_B1","hTimeDeltaR_Q_B1",100,0.,4.);  histos.Add(hTimeDeltaR_Q_B1);
  hTimeDeltaR_QW_B3 = new TH1D("hTimeDeltaR_QW_B3","hTimeDeltaR_QW_B3",100,0.,4.);  histos.Add(hTimeDeltaR_QW_B3);
  hTimeDeltaR_QW_B2 = new TH1D("hTimeDeltaR_QW_B2","hTimeDeltaR_QW_B2",100,0.,4.);  histos.Add(hTimeDeltaR_QW_B2);
  hTimeDeltaR_QW_B1 = new TH1D("hTimeDeltaR_QW_B1","hTimeDeltaR_QW_B1",100,0.,4.);  histos.Add(hTimeDeltaR_QW_B1);

  unsigned int nOmtfLayers =  omtfUtilities::layerNames.size();
  hTimeLayers =  new TH1D("hTimeLayers","hTimeLayers", nOmtfLayers,-0.5,nOmtfLayers-0.5); histos.Add(hTimeLayers);
  for (unsigned int ibin=1; ibin<=nOmtfLayers; ibin++) hTimeLayers->GetXaxis()->SetBinLabel(ibin,omtfUtilities::layerNames[ibin-1].c_str());



  hTimeBmtfOmtf = new TH2D("hTimeBmtfOmtf","hTimeBmtfOmtf",5,-2.5,2.5, 5,-2.5,2.5); histos.Add(hTimeBmtfOmtf);
  hTimeOmtfEmtf = new TH2D("hTimeOmtfEmtf","hTimeOmtfEmtf",5,-2.5,2.5, 5,-2.5,2.5); histos.Add(hTimeOmtfEmtf);
  hTimeOmtfOmtf_E= new TH2D("hTimeOmtfOmtf_E","hTimeOmtfOmtf_E",5,-2.5,2.5, 5,-2.5,2.5); histos.Add(hTimeOmtfOmtf_E);

  hTimeOmtfTrackDPhiT = new TH2D("hTimeOmtfTrackDPhiT","hTimeOmtfTrackDPhiT",50,0.,25., 50, -1.,1.); histos.Add(hTimeOmtfTrackDPhiT);
  hTimeOmtfTrackDPhiM = new TH2D("hTimeOmtfTrackDPhiM","hTimeOmtfTrackDPhiM",50,0.,25., 50, -1.,1.); histos.Add(hTimeOmtfTrackDPhiM);
  hTimeOmtfTrackDEtaT = new TH2D("hTimeOmtfTrackDEtaT","hTimeOmtfTrackDEtaT",50,0.,25., 50, -1.,1.); histos.Add(hTimeOmtfTrackDEtaT);
  hTimeOmtfTrackDEtaM = new TH2D("hTimeOmtfTrackDEtaM","hTimeOmtfTrackDEtaM",50,0.,25., 50, -1.,1.); histos.Add(hTimeOmtfTrackDEtaM);
//  hTimeOmtfTrackDRM   = new TH2D("hTimeOmtfTrackDRM",  "hTimeOmtfTrackDRM",  50,0.,25., 50, -1.,1.); histos.Add(hTimeOmtfTrackDRM);
  hTimeOmtfTrackDRM   = new TH1D("hTimeOmtfTrackDRM",  "hTimeOmtfTrackDRM",  50, 0.,2.); histos.Add(hTimeOmtfTrackDRM);
  hTimeOmtfTrackBXT = new TH2D("hTimeOmtfTrackBXT", "hTimeOmtfTrackBXT", 50,0.,25.,4, -1.,3.); histos.Add(hTimeOmtfTrackBXT);
  hTimeOmtfTrackBXM = new TH2D("hTimeOmtfTrackBXM", "hTimeOmtfTrackBXM", 50,0.,25.,4, -1.,3.); histos.Add(hTimeOmtfTrackBXM);
  hTimeOmtfTrackBX0 = new TH1D("hTimeOmtfTrackBX0", "hTimeOmtfTrackBX0", 50,0.,25.); histos.Add(hTimeOmtfTrackBX0);
  hTimeOmtfTrackBX1 = new TH1D("hTimeOmtfTrackBX1", "hTimeOmtfTrackBX1", 50,0.,25.); histos.Add(hTimeOmtfTrackBX1);
  hTimeOmtfDrTrackMuon = new TH2D("hTimeOmtfDrTrackMuon","hTimeOmtfDrTrackMuon",50,0.,25.,50, -1.,1.); histos.Add(hTimeOmtfDrTrackMuon);
}

void AnaTime::run(const EventObj* ev, const MuonObjColl *muonColl, const TrackObj* track, const L1ObjColl * l1Objs)
{
  std::vector<L1Obj::TYPE> mtfs= {L1Obj::BMTF, L1Obj::OMTF, L1Obj::EMTF, L1Obj::OMTF_emu};
  //
  // all triggers
  //
  const std::vector<L1Obj> & l1mtfs = *l1Objs;
  const std::vector<MuonObj> & muons = *muonColl;

  bool printdeb = false;
  for (const auto & l1mtf : l1mtfs) {
    bool matched  = false;
    bool matchedW = false;
    bool qualOK = (l1mtf.q >= 12);
    for (const auto & muon : muons) { 
      if (!muon.isValid()) continue;
//      double deltaR = reco::deltaR( l1mtf.etaValue(), l1mtf.phiValue(), muon.eta(), muon.phi());
      double deltaR = reco::deltaR( l1mtf.etaValue(), l1mtf.phiValue(), muon.l1Eta, muon.l1Phi);
      double deltaRW = reco::deltaR( l1mtf.etaValue(), l1mtf.phiValue(), -muon.l1Eta, muon.l1Phi+M_PI/2.);
      if (qualOK && l1mtf.type==L1Obj::OMTF) { 
        hTimeDeltaR_Q->Fill(deltaR); 
        hTimeDeltaR_QW->Fill(deltaRW); 
        if (l1mtf.bx == -3) hTimeDeltaR_Q_B3->Fill(deltaR); 
        if (l1mtf.bx == -2) hTimeDeltaR_Q_B2->Fill(deltaR); 
        if (l1mtf.bx == -1) hTimeDeltaR_Q_B1->Fill(deltaR); 
        if (l1mtf.bx == -3) hTimeDeltaR_QW_B3->Fill(deltaRW); 
        if (l1mtf.bx == -2) hTimeDeltaR_QW_B2->Fill(deltaRW); 
        if (l1mtf.bx == -1) hTimeDeltaR_QW_B1->Fill(deltaRW); 
        if ( deltaR < 0.2 && l1mtf.bx < 0) {
          printdeb = false;
          std::bitset<18> hitLayers(l1mtf.hits);
          for (unsigned int hitLayer=0; hitLayer<18;hitLayer++) if(hitLayers[hitLayer]) hTimeLayers->Fill(hitLayer);
        }
      }
      if (deltaR  < 0.4)  matched=true;
      if (deltaRW < 0.4) matchedW=true;
    }
    TH1D *hA, *hQ, *hM, *hQM, *hW, *hQW; 
    hA=hQ=hM=hQM=hW=hQW=0; 
    switch (l1mtf.type) {
        case (L1Obj::BMTF) : hA=hTimeBmtf_A; hQ=hTimeBmtf_Q; hM=hTimeBmtf_M;  hQM=hTimeBmtf_QM;  hW=hTimeBmtf_W;  hQW=hTimeBmtf_QW; break;
        case (L1Obj::EMTF) : hA=hTimeEmtf_A; hQ=hTimeEmtf_Q; hM=hTimeEmtf_M;  hQM=hTimeEmtf_QM;  hW=hTimeEmtf_W;  hQW=hTimeEmtf_QW; break;
        case (L1Obj::OMTF) : hA=hTimeOmtf_A; hQ=hTimeOmtf_Q; hM=hTimeOmtf_M;  hQM=hTimeOmtf_QM;  hW=hTimeOmtf_W;  hQW=hTimeOmtf_QW; break;
        case (L1Obj::OMTF_emu) : hA=hTimeOmtf_emu_A; hQ=hTimeOmtf_emu_Q; hM=hTimeOmtf_emu_M;  hQM=hTimeOmtf_emu_QM;  hW=hTimeOmtf_emu_W;  hQW=hTimeOmtf_emu_QW; break;
        default: ;
    }
    if (hA!=0) {
      hA->Fill(l1mtf.bx); 
      if (qualOK) hQ->Fill(l1mtf.bx); 
      if (matched) hM->Fill(l1mtf.bx);  
      if (qualOK && matched) hQM->Fill(l1mtf.bx);  
      if (matchedW) hW->Fill(l1mtf.bx);  
      if (qualOK && matchedW) hQW->Fill(l1mtf.bx);  
    }
  }

  //
  // coincidence between triggers.
  //
  for (const auto & l1mtf_1 : l1mtfs) {
    for (const auto & l1mtf_2 : l1mtfs) {
      double deltaEta = l1mtf_1.etaValue()-l1mtf_2.etaValue();
      double deltaPhi = reco::deltaPhi( l1mtf_1.phiValue(),  l1mtf_2.phiValue());

      if ( (fabs(deltaEta) > 0.2) || (fabs(deltaPhi) >0.05) ) continue;
      if (l1mtf_1.type==L1Obj::BMTF && l1mtf_2.type ==  L1Obj::OMTF && l1mtf_2.q>=12) {
         hTimeBmtfOmtf->Fill(l1mtf_1.bx,l1mtf_2.bx);
//         if (l1mtf_2.bx <0 && l1mtf_1.bx==0) { printdeb=true;
//           std::cout <<" deta: "<<deltaEta<<" dphi: "<<deltaPhi<<std::endl;
//           std::cout << l1mtf_2<<std::endl;
//           std::cout << l1mtf_1<<std::endl;
//         }
      }
      if (l1mtf_1.type==L1Obj::OMTF && l1mtf_1.q>=12  && l1mtf_2.type ==  L1Obj::EMTF) {
         hTimeOmtfEmtf->Fill(l1mtf_1.bx,l1mtf_2.bx);
//         if (l1mtf_1.bx <0 && l1mtf_2.bx==0) { printdeb=true;
//           std::cout <<" deta: "<<deltaEta<<" dphi: "<<deltaPhi<<std::endl;
//           std::cout << l1mtf_1<<std::endl;
//           std::cout << l1mtf_2<<std::endl;
//         }
      }
      if (l1mtf_1.type==L1Obj::OMTF && l1mtf_2.type ==  L1Obj::OMTF_emu) {
         hTimeOmtfOmtf_E->Fill(l1mtf_1.bx,l1mtf_2.bx);
      }
    }
  }
  if (printdeb) {
    std::cout <<"-------- PREFIRE debug: "<<std::endl; 
    if (muonColl) std::cout << *muonColl << std::endl;
    if (l1Objs)  std::cout << *l1Objs<< std::endl;
  } 

/*

  //
  // track/muon matching to l1omtf
  //
  typedef std::vector<L1Obj> L1ObjVec;
  L1ObjVec omtfVec = l1Objs->selectByType(L1Obj::OMTF).selectByBx(0,0);
  double detaM = 9999.;
  double dphiM = 9999.;
  double dR = 9999;
  for (auto & l1Omtf : omtfVec) {

//  if (track->pt() > 1. && omtfColl) {
//    L1Obj l1Omtf = omtfColl.getL1Objs().front();
//    double dphiT =  reco::deltaPhi(l1Omtf.phiValue(),track->phi())*track->charge(); 
//    double detaT =  (l1Omtf.etaValue() - track->eta())*sgn(track->eta());
//    hTimeOmtfTrackDPhiT->Fill(track->pt(), dphiT);
//    hTimeOmtfTrackDEtaT->Fill(track->pt(), detaT);
//    hTimeOmtfTrackBXT->Fill(track->pt(), l1Omtf.bx);
//    if(l1Omtf.bx==0)hTimeOmtfTrackBX0->Fill(track->pt());
//    if(l1Omtf.bx==1)hTimeOmtfTrackBX1->Fill(track->pt());

    if (muon && ( (fabs(muon->l1Eta)-1.04) < 0.3) ){

      double aDeta =  (l1Omtf.etaValue() - muon->l1Eta)*sgn(muon->eta());
      double aDphi =  reco::deltaPhi(l1Omtf.phiValue(),muon->l1Phi)*muon->charge(); 
      double aDR = reco::deltaR(l1Omtf.etaValue(), l1Omtf.phiValue(), muon->l1Eta, muon->l1Phi);
//      std::cout <<" L1: "<<l1Omtf.etaValue()<<", "<<l1Omtf.phiValue()<<"    muon: "<<muon->l1Eta<<", "<< muon->l1Phi <<"   dR: "<<aDR<<std::endl;
      if (aDR < dR) {
        dR = aDR;
        detaM = aDeta;
        dphiM = aDphi;
      } 

//      hTimeOmtfTrackBXM->Fill(muon->pt(), l1Omtf.bx);
//      hTimeOmtfDrTrackMuon->Fill(track->pt(), reco::deltaR(track->eta(), track->phi(), muon->eta(), muon->phi()));
    }
  } 
  if (muon) {
    hTimeOmtfTrackDRM->Fill(dR);
    hTimeOmtfTrackDPhiM->Fill(muon->pt(), dphiM);
    hTimeOmtfTrackDEtaM->Fill(muon->pt(), detaM);
  }

//  L1ObjColl omtfColl = l1Objs->selectByType(L1Obj::OMTF).selectByBx(0,0);
//  if (track->pt() > 1. && omtfColl) {
//    L1Obj l1Omtf = omtfColl.getL1Objs().front();
//    double dphiT =  reco::deltaPhi(l1Omtf.phiValue(),track->phi())*track->charge(); 
//    double detaT =  (l1Omtf.etaValue() - track->eta())*sgn(track->eta());
//    hTimeOmtfTrackDPhiT->Fill(track->pt(), dphiT);
//    hTimeOmtfTrackDEtaT->Fill(track->pt(), detaT);
//    hTimeOmtfTrackBXT->Fill(track->pt(), l1Omtf.bx);
//    if(l1Omtf.bx==0)hTimeOmtfTrackBX0->Fill(track->pt());
//    if(l1Omtf.bx==1)hTimeOmtfTrackBX1->Fill(track->pt());
//    if(muon) {
//      double detaM =  (l1Omtf.etaValue() - muon->eta())*sgn(muon->eta());
//      double dphiM =  reco::deltaPhi(l1Omtf.phiValue(),muon->phi())*muon->charge(); 
//      hTimeOmtfTrackDPhiM->Fill(muon->pt(), dphiM);
//      hTimeOmtfTrackDEtaM->Fill(muon->pt(), detaM);
//      hTimeOmtfTrackBXM->Fill(muon->pt(), l1Omtf.bx);
//      hTimeOmtfDrTrackMuon->Fill(track->pt(), reco::deltaR(track->eta(), track->phi(), muon->eta(), muon->phi()));
//    }
//  } 

  //
  // triggers matched to muons
  //
//  if (!muon || !muon->isValid()) return;
//  for (const auto & mtf : mtfs) {
//    std::vector<L1Obj> l1mtfs = l1Objs->selectByType(mtf);
//    if (l1mtfs.size()==0) continue;
//    for (const auto & l1mtf : l1mtfs) {
//      double deltaR = reco::deltaR( l1mtf.etaValue(), l1mtf.phiValue(), muon->eta(), muon->phi());
////      std::cout <<"TIME: "<< l1mtf<< " deltaR: "<< deltaR << std::endl;
//      if (fabs(l1mtf.etaValue() - muon->eta()) > 0.2) continue;
//      if (deltaR > 0.8) continue;
////    if (l1mtf.q <12) continue;
////      if (l1mtf.bx !=0) std::cout <<"xxxxxx" << std::endl;
//      switch (mtf) {
//        case (L1Obj::BMTF) : hTimeBmtf->Fill(l1mtf.bx); break; 
//        case (L1Obj::OMTF) : hTimeOmtf->Fill(l1mtf.bx); break; 
//        case (L1Obj::EMTF) : hTimeEmtf->Fill(l1mtf.bx); break; 
//        default: ;
//      }
//    }
//  }
*/

}

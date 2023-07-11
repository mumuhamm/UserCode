#include "OmtfTreeMaker.h"

#include <vector>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Handle.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "TFile.h"
#include "TTree.h"

#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
#include "DataFormats/L1TMuon/interface/RegionalMuonCandFwd.h"
#include "UserCode/OmtfAnalysis/interface/OmtfGmtData.h"
#include "L1Trigger/L1TMuonOverlap/interface/OmtfName.h"

#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "SimDataFormats/Track/interface/SimTrack.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "UserCode/OmtfAnalysis/interface/ConverterRPCRawSynchroSynchroCountsObj.h"
#include "UserCode/OmtfDataFormats/interface/DetBxStatObj.h"



template <class T> T sqr( T t) {return t*t;}

OmtfTreeMaker::OmtfTreeMaker(const edm::ParameterSet& cfg)
  : theConfig(cfg), theCounter(0), theFile(0), theTree(0), 
    bitsL1(0), bitsHLT(0),
    event(0), 
    muonColl(0), l1ObjColl(0), 
    synchroCounts(0), closestTrack(0),
    theMenuInspector(cfg.getParameter<edm::ParameterSet>("menuInspector"), consumesCollector()), 
    theBestMuonFinder(cfg.getParameter<edm::ParameterSet>("bestMuonFinder"), consumesCollector()),
    theL1ObjMaker(cfg.getParameter<edm::ParameterSet>("l1ObjMaker"), consumesCollector()), 
    theSynchroGrabber(cfg.getParameter<edm::ParameterSet>("linkSynchroGrabber"), consumesCollector()),
    theClosestTrackFinder(cfg.getParameter<edm::ParameterSet>("closestTrackFinder"), consumesCollector()),
    theSynchroCheck(cfg.getParameter<edm::ParameterSet>("synchroCheck"), consumesCollector())
{
inputSim = consumes<edm::SimTrackContainer>(edm::InputTag("g4SimHits"));
vertexSim = consumes<edm::SimVertexContainer>(edm::InputTag("g4SimHits"));
 }
  

void OmtfTreeMaker::beginRun(const edm::Run &ru, const edm::EventSetup &es)
{
  std::cout <<"**** BEGIN RUN called!" << std::endl;
  theMenuInspector.checkRun(ru,es);
}

void OmtfTreeMaker::beginJob()
{
  theFile = new TFile(theConfig.getParameter<std::string>("treeFileName").c_str(),"RECREATE");
  theTree = new TTree("tOmtf","OmtfTree");

  theTree->Branch("event","EventObj",&event,32000,99);
  theTree->Branch("muonColl", "MuonObjColl", &muonColl, 32000,99);
  theTree->Branch("l1ObjColl","L1ObjColl",&l1ObjColl,32000,99);

  theTree->Branch("bitsL1" ,"TriggerMenuResultObj",&bitsL1 ,32000,99);
  theTree->Branch("bitsHLT","TriggerMenuResultObj",&bitsHLT,32000,99);
  theTree->Branch("synchroCounts","SynchroCountsObjVect",&synchroCounts,32000,99);
  theTree->Branch("closestTrack","TrackObj",&closestTrack, 32000, 99);

  theHelper.SetOwner();
  theBestMuonFinder.initHistos(theHelper);
  theSynchroGrabber.initHistos(theHelper);
  theClosestTrackFinder.initHistos(theHelper);
  theSynchroCheck.initHistos(theHelper);

}

void OmtfTreeMaker::endJob()
{
  theFile->Write();
  delete theFile;

  std::string helperFile = theConfig.getParameter<std::string>("histoFileName");
  TFile f(helperFile.c_str(),"RECREATE");
  theHelper.Write();
  f.Close();
}

OmtfTreeMaker::~OmtfTreeMaker()
{
  std::cout <<"OmtfTreeMaker: Event counter is: "<<theCounter<<std::endl;
}

void OmtfTreeMaker::analyze(const edm::Event &ev, const edm::EventSetup &es)
{
  //
  // initial filter. Optionally do not further use events without muon
  //
  event = new EventObj;
  event->bx = ev.bunchCrossing();
  event->orbit = ev.orbitNumber();
  event->time = ev.time().value();
  event->id = ev.id().event();
  event->run = ev.run();
  event->lumi = ev.luminosityBlock();

  const reco::Muon * theMuon = theBestMuonFinder.result(ev,es);

  if (theConfig.getParameter<bool>("onlyBestMuEvents") && (!theMuon) ) return;
  theCounter++;

  //
  // fill event information
  //

  //
  // create other objects structure
  //
  muonColl = new MuonObjColl (theBestMuonFinder.muons(ev,es));
//  muonColl = new MuonObjColl;
  l1ObjColl = new L1ObjColl;

  bitsL1 = new TriggerMenuResultObj();
  bitsHLT = new TriggerMenuResultObj();

  synchroCounts = new SynchroCountsObjVect;

  closestTrack = new TrackObj();

  //
  // fill algoBits info
  //
  //
  static edm::RunNumber_t lastRun = 0;
  if (ev.run() != lastRun) {
    lastRun = ev.run();
    bitsL1->names  = theMenuInspector.namesAlgoL1();
    bitsHLT->names = theMenuInspector.namesAlgoHLT();
  }
  bitsL1->firedAlgos = theMenuInspector.firedAlgosL1(ev,es);
  bitsHLT->firedAlgos = theMenuInspector.firedAlgosHLT(ev,es);

  //
  // associate HLT info to muonColl objs
  //
  theMenuInspector.associateHLT(ev,es,muonColl);


  // get L1 candidates
  std::vector<L1Obj> l1Objs = theL1ObjMaker(ev);
  if (l1Objs.size()) {
    l1ObjColl->set(l1Objs);
    l1ObjColl->set( std::vector<bool>(l1Objs.size(),false));
    l1ObjColl->set( std::vector<double>(l1Objs.size(),0.));
  }

    
  //
  // fill LinkSynchroAnalysis data
  //
  if (theMuon && theMuon->isGlobalMuon()) {
    theSynchroGrabber.setMuon(theMuon);
    RPCRawSynchro::ProdItem rawCounts  = theSynchroGrabber.counts(ev,es);
    synchroCounts->data = ConverterRPCRawSynchroSynchroCountsObj::toSynchroObj(rawCounts);
  }

  
/*
  edm::Handle<edm::SimTrackContainer> simTk;
  edm::Handle<edm::SimVertexContainer> simVx;
  ev.getByToken(inputSim, simTk);
  ev.getByToken(vertexSim, simVx);
  std::vector<SimTrack> mySimTracks = *(simTk.product());
  std::vector<SimVertex> mySimVertex = *(simVx.product());

bool debug=1;
if (debug) {
  std::cout<<std::endl <<"#"<<theCounter<<" "<< *event << std::endl;
  for (const auto & sv : mySimVertex) std::cout <<" vtx_id: "<<sv.vertexId()<<" position_perp: "<< sv.position().Rho() <<" pos :"<<sv.position()<< std::endl;
}


  for (std::vector<SimTrack>::const_iterator it=mySimTracks.begin(); it<mySimTracks.end(); it++) {
    const SimTrack & track = *it;
    if ( track.type() == -99) continue;
    if ( track.vertIndex() != 0) continue;
//    if ( track.vertIndex() >1) continue;
//    if (mySimVertex[track.vertIndex()].position().rho() > 50.) continue;

    //sucessful muon, add to count

    double phi_sim = track.momentum().phi(); //momentum azimutal angle
    double pt_sim = track.momentum().pt(); //transverse momentum
    double eta_sim = track.momentum().eta(); //pseudorapidity
    muonColl->data().push_back(MuonObj(pt_sim, eta_sim, phi_sim, track.type()/(-13)) ); 

if (debug) std::cout << " pt_sim: " << pt_sim <<" eta_sim: "<<eta_sim<<" phi_sim: "<<phi_sim
                 <<" vtx: "<<track.vertIndex()<<" type: "<<track.type() // 13 or -13 is a muon
                 << "pos: "<<mySimVertex[track.vertIndex()].position().rho()
                 << std::endl; 
  }
*/

//
bool debug=0;
  if (debug) { // || l1ObjColl->selectByType(L1Obj::OMTF_emu)) {
    std::cout << *muonColl << std::endl;
    std::cout << *l1ObjColl << std::endl;
    std::cout << std::endl;
  }
  theSynchroCheck.checkInside(theMuon, ev, es);
  theSynchroCheck.checkStripCsc(theMuon, ev, es);
  theSynchroCheck.checkStripRpc(theMuon, ev, es);
  theSynchroCheck.checkDigiDt(theMuon, ev, es);
  theSynchroCheck.checkHitRpc(theMuon, ev, es);
  theSynchroCheck.checkHitCsc(theMuon, ev, es);

  L1ObjColl omtfColl = l1ObjColl->selectByType(L1Obj::OMTF);
  if (omtfColl) {
    reco::Track track = theClosestTrackFinder.result(ev,es, omtfColl.getL1Objs().front().etaValue(), 
                                                            omtfColl.getL1Objs().front().phiValue());
    closestTrack->setKine(track.pt(), track.eta(), track.phi(), track.charge());
  }

  //
  // fill ntuple + cleanup
  //
  //if (omtfResult,size()) 
  theTree->Fill();
  delete event; event = 0;
  delete muonColl; muonColl = 0;
  delete bitsL1;  bitsL1= 0;
  delete bitsHLT;  bitsHLT= 0;
  delete l1ObjColl; l1ObjColl = 0;
  delete closestTrack; closestTrack = 0;
}

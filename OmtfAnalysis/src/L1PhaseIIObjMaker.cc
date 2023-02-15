#include "UserCode/OmtfAnalysis/interface/L1PhaseIIObjMaker.h"

#include <iostream>
#include <sstream>

#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"

#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuRegionalCand.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTCand.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTExtendedCand.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTReadoutCollection.h"
#include "L1Trigger/RPCTrigger/interface/RPCConst.h"

#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
#include "DataFormats/L1TMuon/interface/RegionalMuonCandFwd.h"
#include "DataFormats/L1Trigger/interface/Muon.h"

using namespace std;
namespace {
  edm::EDGetTokenT<l1t::TrackerMuonCollection> theGmtEmulToken, theGmtDataToken;
}

L1PhaseIIObjMaker::L1PhaseIIObjMaker(const  edm::ParameterSet & cfg, edm::ConsumesCollector&& cColl)
  :  theConfig(cfg),
     lastEvent(0),lastRun(0)
{
  if (theConfig.exists("gmtDataSrc"))  theGmtDataToken  =  cColl.consumes<l1t::TrackerMuonCollection>(theConfig.getParameter<edm::InputTag>("L1TkMuonsGmt"));  
  if (theConfig.exists("gmtEmulSrc"))  theGmtEmulToken  =  cColl.consumes<l1t::TrackerMuonCollection>(theConfig.getParameter<edm::InputTag>("gmtEmulSrc"));
}

void L1PhaseIIObjMaker::run(const edm::Event &ev)
{
  if (lastEvent==ev.id().event() && lastRun==ev.run()) return;
  lastEvent = ev.id().event() ;
  lastRun = ev.run();
  theL1PhaseIIObjs.clear();

  if ( !theGmtDataToken.isUninitialized())  makeGmtCandidates(ev, L1PhaseIIObj::uGMT    , theL1PhaseIIObjs);
  if ( !theGmtEmulToken.isUninitialized())  makeGmtCandidates(ev, L1PhaseIIObj::uGMT_emu, theL1PhaseIIObjs);

}

bool L1PhaseIIObjMaker::makeGmtCandidates(const edm::Event &iEvent,  L1PhaseIIObj::TYPE type, std::vector<L1PhaseIIObj> &result)
{  
  edm::Handle<l1t::TrackerMuonCollection> candidates;
  switch (type) {
    case  L1PhaseIIObj::uGMT     : { iEvent.getByToken(theGmtDataToken, candidates); break; }
    case  L1PhaseIIObj::uGMT_emu : { iEvent.getByToken(theGmtEmulToken, candidates); break; }
    default: { std::cout <<"Invalid type : " << type << std::endl; abort(); }
  }

  for(const auto & aCand: *candidates.product()){
    L1PhaseIIObj obj;
    obj.type =  type;
    obj.phi = aCand.phPhi();
    obj.eta = aCand.phEta();
    obj.pt = aCand.phPt();
    obj.q   = 12;                             
    obj.bx = 0;
    obj.charge = aCand.phCharge();
    theL1PhaseIIObjs.push_back(obj);
  }
  return true; 
}

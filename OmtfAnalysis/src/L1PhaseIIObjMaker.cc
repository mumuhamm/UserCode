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
  edm::EDGetTokenT<l1t::RegionalMuonCandBxCollection> theOmtfEmulToken, theOmtfDataToken, theEmtfDataToken, theBmtfDataToken;
  edm::EDGetTokenT<l1t::MuonBxCollection> theGmtEmulToken;
  edm::EDGetTokenT<l1t::TrackerMuonCollection> theGmtDataToken;
}

L1PhaseIIObjMaker::L1PhaseIIObjMaker(const  edm::ParameterSet & cfg, edm::ConsumesCollector&& cColl)
  :  theConfig(cfg),
     lastEvent(0),lastRun(0)
{
  if (theConfig.exists("omtfEmulSrc")) theOmtfEmulToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("omtfEmulSrc") );
  if (theConfig.exists("omtfDataSrc")) theOmtfDataToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("omtfDataSrc") );
  if (theConfig.exists("bmtfDataSrc")) theBmtfDataToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("bmtfDataSrc") );
  if (theConfig.exists("emtfDataSrc")) theEmtfDataToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("emtfDataSrc") );
  // Tu
  // if (theConfig.exists("gmtEmulSrc"))  theGmtDataToken  =  cColl.consumes<l1t::TrackerMuonCollection>(edm::InputTag("L1TkMuonsGmt"));
  if (theConfig.exists("gmtDataSrc"))  theGmtDataToken  =  cColl.consumes<l1t::TrackerMuonCollection>(theConfig.getParameter<edm::InputTag>("L1TkMuonsGmt"));
  //
  if (theConfig.exists("gmtEmulSrc"))  theGmtEmulToken  =  cColl.consumes<l1t::MuonBxCollection>( theConfig.getParameter<edm::InputTag>("gmtEmulSrc"));
 
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

  cout << "Marny sukces" << endl;
//   edm::Handle<l1t::TrackerMuonCollection> candidates;
//   switch (type) {
//     case  L1PhaseIIObj::uGMT     : { iEvent.getByToken(theGmtDataToken, candidates); break; }
//     case  L1PhaseIIObj::uGMT_emu : { iEvent.getByToken(theGmtEmulToken, candidates); break; }
//     default: { std::cout <<"Invalid type : " << type << std::endl; abort(); }
//   }
// //  int bxNumber = 0;
//   //for (int bxNumber=-2; bxNumber<=2; bxNumber++) {
//   for (int bxNumber=candidates->getFirstBX(); bxNumber<=candidates->getLastBX(); bxNumber++) {
//   for (l1t::MuonBxCollection::const_iterator it = candidates.product()->begin(bxNumber);
//       it != candidates.product()->end(bxNumber);
//       ++it) {
//     L1PhaseIIObj obj;
//     obj.type =  type;
// //    obj.phi = it->hwPhiAtVtx(); 
// //    obj.eta = it->hwEtaAtVtx();        // eta = hwEta/240.*2.61
//     obj.phi = it->hwPhi(); 
//     obj.eta = it->hwEta();        // eta = hwEta/240.*2.61
//     obj.pt  = it->hwPt();         // pt = (hwPt-1.)/2.
//     obj.q   = it->hwQual();                             
//     obj.bx = bxNumber;
//     obj.charge = it->hwCharge();  // charge  =  pow(-1,hwSign)
//     result.push_back(obj);
//   }
//   }
  return true; 

// w naszej wersji nie bedzie petli po bxNumber bo nasza wersja TrackerMuon collection
// Zrobic analogicza petle po TrackerMuonCollection z parametrami TrackerMuon

}

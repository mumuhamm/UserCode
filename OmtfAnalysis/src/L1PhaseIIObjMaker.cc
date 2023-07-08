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
  edm::EDGetTokenT<l1t::TrackerMuonCollection> theGmtEmulToken, theGmtDataToken;
}

L1PhaseIIObjMaker::L1PhaseIIObjMaker(const  edm::ParameterSet & cfg, edm::ConsumesCollector&& cColl)
  :  theConfig(cfg),
     lastEvent(0),lastRun(0)
{
  if (theConfig.exists("omtfEmulSrc")) theOmtfEmulToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("omtfEmulSrc") );
  if (theConfig.exists("omtfDataSrc")) theOmtfDataToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("omtfDataSrc") );
  if (theConfig.exists("bmtfDataSrc")) theBmtfDataToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("bmtfDataSrc") );
  if (theConfig.exists("emtfDataSrc")) theEmtfDataToken =  cColl.consumes<l1t::RegionalMuonCandBxCollection>(  theConfig.getParameter<edm::InputTag>("emtfDataSrc") );
                                                                                      
 if (theConfig.exists("gmtDataSrc"))  theGmtDataToken  =  cColl.consumes<l1t::TrackerMuonCollection>(theConfig.getParameter<edm::InputTag>("gmtDataSrc"));  
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
  if (!theOmtfDataToken.isUninitialized())  makeRegCandidates(ev, L1PhaseIIObj::OMTF    , theL1PhaseIIObjs);
  if (!theOmtfEmulToken.isUninitialized())  makeRegCandidates(ev, L1PhaseIIObj::OMTF_emu, theL1PhaseIIObjs);
  if (!theBmtfDataToken.isUninitialized())  makeRegCandidates(ev, L1PhaseIIObj::BMTF    , theL1PhaseIIObjs);
  if (!theEmtfDataToken.isUninitialized())  makeRegCandidates(ev, L1PhaseIIObj::EMTF    , theL1PhaseIIObjs); 

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
   // std::cout<< " for GMT : phPhi: "<< aCand.phPhi()<<"\n";
    obj.eta = aCand.phEta();
    obj.pt = aCand.phPt();
    obj.q   = 12;                             
    obj.bx = 0;
    obj.charge = aCand.phCharge();
    result.push_back(obj);
  }
  return true; 
}
bool L1PhaseIIObjMaker::makeRegCandidates(const edm::Event &iEvent,  L1PhaseIIObj::TYPE type, std::vector<L1PhaseIIObj> &result)
{
  edm::Handle<l1t::RegionalMuonCandBxCollection> candidates;
  switch (type) {
    case  L1PhaseIIObj::OMTF_emu: { iEvent.getByToken(theOmtfEmulToken, candidates); break; }
    case  L1PhaseIIObj::OMTF    : { iEvent.getByToken(theOmtfDataToken, candidates); break; }
    case  L1PhaseIIObj::BMTF    : { iEvent.getByToken(theBmtfDataToken, candidates); break; }
    case  L1PhaseIIObj::EMTF    : { iEvent.getByToken(theEmtfDataToken, candidates); break; }
    default: { std::cout <<"Invalid type : " << type << std::endl; abort(); }
  }
 
  for (int bxNumber=candidates->getFirstBX(); bxNumber<=candidates->getLastBX(); bxNumber++) {    
    for (l1t::RegionalMuonCandBxCollection::const_iterator it = candidates.product()->begin(bxNumber);
       it != candidates.product()->end(bxNumber);
       ++it) {

    L1PhaseIIObj phaseIIobj;
    phaseIIobj.type =  type;
    phaseIIobj.iProcessor = it->processor(); // [0..5]

    phaseIIobj.position =   (it->trackFinderType() == l1t::omtf_neg || it->trackFinderType() == l1t::emtf_neg) ? -1 :
                   ( (it->trackFinderType() == l1t::omtf_pos || it->trackFinderType() == l1t::emtf_pos) ? +1 : 0 );
    std::cout<<" for regional candidate: hwphi :"<< it->hwPhi()<<"\n";
    phaseIIobj.phi = it->hwPhi();  // phi_Rad = [ (15.+processor*60.)/360. + hwPhi/576. ] *2*M_PI
    phaseIIobj.eta = it->hwEta();  // eta = hwEta/240.*2.61
    phaseIIobj.pt = it->hwPt();         // pt = (hwPt-1.)/2.
    phaseIIobj.charge = it->hwSign();   // charge=  pow(-1,hwSign)

    std::map<int, int> hwAddrMap = it->trackAddress();
    phaseIIobj.q   = it->hwQual();
    phaseIIobj.hits   = hwAddrMap[0];
    phaseIIobj.bx = bxNumber;
    phaseIIobj.refLayer = hwAddrMap[1];    
    phaseIIobj.disc = hwAddrMap[2];    
    result.push_back(phaseIIobj);   
  }
  }
  return true;
}


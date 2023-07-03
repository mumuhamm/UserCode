#include "UserCode/OmtfAnalysis/interface/MenuInspector.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Handle.h"

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
/*
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuRegionalCand.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTCand.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTExtendedCand.h"
#include "DataFormats/L1GlobalMuonTrigger/interface/L1MuGMTReadoutCollection.h"
*/
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenuFwd.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerRecord.h"

#include "UserCode/OmtfDataFormats/interface/MuonObjColl.h"
#include "DataFormats/Math/interface/deltaR.h"



#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <bitset>

#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "CondFormats/DataRecord/interface/L1TUtmTriggerMenuRcd.h"
#include "CondFormats/L1TObjects/interface/L1TUtmTriggerMenu.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerResultsByName.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"


namespace {
  edm::EDGetTokenT<edm::TriggerResults> theTrigResultToken;
  edm::EDGetTokenT<GlobalAlgBlkBxCollection> theGlobalAlgToken;
}


MenuInspector::MenuInspector(const edm::ParameterSet& cfg, edm::ConsumesCollector cColl)
  : lastEvent(0), lastRun(0),
    theCounterIN(0), theCounterL1(0), theCounterHLT(0),
    theWarnNoColl(cfg.getUntrackedParameter<bool>("warnNoColl",true)),
    theL1MenuToken(cColl.esConsumes<edm::Transition::BeginRun>())
{ 
  theTrigResultToken = cColl.consumes<edm::TriggerResults>(edm::InputTag("TriggerResults","","HLT"));
  theGlobalAlgToken  = cColl.consumes<GlobalAlgBlkBxCollection>(edm::InputTag("hltGtStage2Digis"));
  l1tUtmTriggerMenuToken = cColl.esConsumes<edm::Transition::BeginRun>();

  cColl.consumes<trigger::TriggerEvent>(edm::InputTag("hltTriggerSummaryAOD","","HLT"));

  std::vector<std::string> names = cfg.getParameter<std::vector<std::string> >("namesCheckHltMuMatch");
  for (auto name : names) theNamesCheckHltMuMatchIdx[name]=-1;
}

bool MenuInspector::checkRun(const edm::Run& run, const edm::EventSetup & es)
{
  //
  // L1
  //
//  edm::ESHandle<L1TUtmTriggerMenu> menu;
//  es.get<L1TUtmTriggerMenuRcd>().get(menu);
  auto const & menu = es.getData(theL1MenuToken);
//  const L1TUtmTriggerMenu & menu = es.getData(theL1MenuToken);

  theNamesAlgoL1.clear();
  theNamesAlgoL1.resize(menu.getAlgorithmMap().size(),"");
//  std::cout <<" size of indexes: "<< menu.getAlgorithmMap().size() << std::endl;
  for (auto const & keyval: menu.getAlgorithmMap()) {
    std::string const & name  = keyval.second.getName();
    unsigned int        index = keyval.second.getIndex();
//    std::cout << " L1  Index: " << index << " name: " << name << std::endl;
    if (index >= theNamesAlgoL1.size() ) theNamesAlgoL1.resize( index+1,"");  
    theNamesAlgoL1[index]=name;
  }
//  std::cout <<" size of indexes: "<< theNamesAlgoL1.size() << std::endl;
//  for (unsigned int i=0; i< theNamesAlgoL1.size(); ++i) std::cout <<" L1 indes: " << i << " algo: "<<theNamesAlgoL1[i] << std::endl;

  //
  // HLT
  //
  bool changed(true);
  theTriggerParSetID = theHltConfig.processPSet().id(); 
  if (theHltConfig.init(run,es,"HLT",changed)) {
    if (changed) {
//      theHltConfig.dump("Streams");
//      theHltConfig.dump("Datasets");
//      theHltConfig.dump("Triggers");
//      theHltConfig.dump("PrescaleTable");
//      theHltConfig.dump("ProcessPSet");
      theNamesAlgoHLT.clear();
      for (auto & im : theNamesCheckHltMuMatchIdx) im.second = -1;

      //for goes up to .size()-1, since the last is "Final" decision.
      for (unsigned int idx =0;  idx < theHltConfig.size()-1; idx++) {
        std::string name = theHltConfig.triggerName(idx);
       // std::cout <<" HLT index: "<< idx << "name: "<< name << std::endl;
        theNamesAlgoHLT.push_back( name );
        for (auto & im : theNamesCheckHltMuMatchIdx) if (name.find(im.first) != std::string::npos) im.second = idx; 
      }
    }
  } 
  return true; 
}

MenuInspector::~MenuInspector()
{
  std::cout <<"MenuInspector, IN: "<<theCounterIN<<"  AfterL1: "<< theCounterL1 << " AfterHLT: "<<theCounterHLT<< std::endl;
}

bool MenuInspector::run(const edm::Event &ev, const edm::EventSetup &es)
{
  if (lastEvent==ev.id().event() && lastRun==ev.run()) return false;
  lastEvent = ev.id().event() ;
  lastRun = ev.run();

  theFiredL1 = runFiredAlgosL1(ev,es);
  theFiredHLT = runFiredAlgosHLT(ev,es);

  return true;
}

bool MenuInspector::associateHLT(const edm::Event &ev, const edm::EventSetup &es, MuonObjColl * muonColl)
{
  run(ev,es);

  bool debug = 0;
  //get HLT result
  edm::Handle<trigger::TriggerEvent> triggerAOD;
  ev.getByLabel(edm::InputTag("hltTriggerSummaryAOD","","HLT"), triggerAOD);
  if (!triggerAOD.isValid()) return false;
  const trigger::TriggerObjectCollection & triggerObjects = triggerAOD->getObjects();

  edm::Handle<edm::TriggerResults> triggerResults;
  ev.getByLabel(edm::InputTag("TriggerResults","","HLT"), triggerResults);
  if (!triggerResults.isValid()) return false;

  std::vector<MuonObj> & muons = muonColl->data();

//  std::cout <<"SIZE of theNamesCheckHltMuMatchIdx : " << theNamesCheckHltMuMatchIdx.size() << std::endl;

  for (const auto & checkHlt : theNamesCheckHltMuMatchIdx) {
//    std::cout <<"checkHlt: "<<checkHlt.first<<" "<<checkHlt.second<<std::endl;
    int checkAlgoIndex = checkHlt.second; 
    if (checkAlgoIndex < 0) continue;
    bool isIsoAlgo = (theNamesAlgoHLT[checkAlgoIndex].find("Iso") != std::string::npos); 
    if( std::find(theFiredHLT.begin(), theFiredHLT.end(), checkAlgoIndex) == theFiredHLT.end() ) continue; 

//  std::cout <<" HERE, fired index:" <<checkAlgoIndex<< theHltConfig.triggerName(checkAlgoIndex)<< std::endl;
    const std::vector<std::string> moduleLabels(theHltConfig.moduleLabels(checkAlgoIndex));
//  {for (const auto & ml : moduleLabels) std::cout <<"Module label: " << ml << std::endl;}
//  unsigned int moduleFireIndex = theHltConfig.size(checkAlgoIndex)-2;  //not works enymore for run3
    unsigned int moduleFireIndex = triggerResults->index(checkAlgoIndex)-1;

    // check if better way exists, this one is crazy....
//  std::cout <<" moduleLabels[moduleFireIndex] : " <<  moduleLabels[moduleFireIndex] << std::endl;
    unsigned hltFilterIndex = triggerAOD->filterIndex( edm::InputTag ( moduleLabels[moduleFireIndex], "", "HLT") ); 
    if (hltFilterIndex >= triggerAOD->sizeFilters())  { std::cout <<" PROBLEM, wrong filter index, skip" << std::endl; continue;}

    trigger::Keys triggerKeys(triggerAOD->filterKeys(hltFilterIndex));
    unsigned nTriggers = triggerKeys.size();
    if (debug) std::cout <<" fired algo: " << theNamesAlgoHLT[checkAlgoIndex]<<" module: "<<moduleLabels[moduleFireIndex] <<", #triggers: " << nTriggers<<std::endl;
    for (size_t iTrig = 0; iTrig < nTriggers; ++iTrig) {
      trigger::TriggerObject triggerObject = triggerObjects[triggerKeys[iTrig]];
      bool matched = false;
      for (auto & muon : muons) {
        double dR = reco::deltaR(muon, triggerObject);
        if (dR < 0.1) { matched = true; if (isIsoAlgo) muon.isMatchedIsoHlt = true; else  muon.isMatchedHlt = true; }
      }
      if (debug) std::cout <<"--> ID: "<< triggerObject.id()<<" PT: "<<triggerObject.pt() <<" ETA: "<< triggerObject.eta() <<" PHI:"<< triggerObject.phi()<<" MATCHED: "<<matched << std::endl;
      
    }
  } 

  return true;

}

bool MenuInspector::filter(edm::Event&ev, const edm::EventSetup&es)
{
/*
  theCounterIN++;
  if ( !filterL1(ev,es) ) return false;
  theCounterL1++;
  if ( !filterHLT(ev,es) ) return false;
  theCounterHLT++;
*/
  return true;
}



std::vector<unsigned int>  MenuInspector::runFiredAlgosL1(const edm::Event&ev, const edm::EventSetup&es) 
{
  std::vector<unsigned int> result;

  edm::Handle<GlobalAlgBlkBxCollection> ugt;
  ev.getByToken(theGlobalAlgToken, ugt);
  if (!ugt.isValid()) {
    // if (theWarnNoColl) std::cout << " PROBLEM, record uGT not OK " << std::endl;
    return result;
  }

  GlobalAlgBlk const * glbAlgBlk  = & ugt->at(0, 0);
  if (!glbAlgBlk) { std::cout << " PROBLEM, no glbAlgBlk, return " << std::endl; return result; }
//  line below print GT record with initial, prescaled and final decision.
//  if (glbAlgBlk) {glbAlgBlk->print( std::cout); std::cout<<std::dec;}
  for (unsigned int idx = 0 ; idx < theNamesAlgoL1.size(); idx++) {
    bool isAccept = glbAlgBlk->getAlgoDecisionFinal(idx);
    if (isAccept) result.push_back(idx);
//  line below prints name of fired algos
//  if (isAccept) std::cout <<" FIRED: "<< theNamesAlgoL1[idx] << std::endl;
  } 

  return result;
}

std::vector<unsigned int> MenuInspector::runFiredAlgosHLT(const edm::Event&ev, const edm::EventSetup&es) 
{
  std::vector<unsigned int> result;

  //
  // get trigger result
  //
  edm::Handle<edm::TriggerResults> triggerResults;
  ev.getByLabel(edm::InputTag("TriggerResults","","HLT"), triggerResults);
  if (!triggerResults.isValid()) { 
    if (theWarnNoColl)std::cout << "firedAlgosHLT, PROBLEM, record not OK"<< std::endl; 
    return result; 
  }
  
  //
  // sanity check that names corresponding to trigger bits are as expected 
  //
  const edm::TriggerNames & triggerNames = ev.triggerNames(*triggerResults);
  assert(triggerResults->size()==theHltConfig.size());
  if (theTriggerParSetID != triggerNames.parameterSetID() ) {
    for (unsigned int triggerIndex =0; triggerIndex < theHltConfig.size()-1; ++triggerIndex) {   //skip "Final" decision indes
      std::string triggerName = theHltConfig.triggerName(triggerIndex);
      unsigned int triggerIndexTmp = theHltConfig.triggerIndex(triggerName);
      assert(triggerIndex==triggerIndexTmp);
      assert(triggerIndex==triggerNames.triggerIndex(triggerName));
    }
    theTriggerParSetID = triggerNames.parameterSetID();
  }

  //
  // fill result table
  //
  for (unsigned int triggerIndex=0; triggerIndex < theHltConfig.size(); ++triggerIndex) {
    bool isAccept = triggerResults->accept(triggerIndex);
    if (isAccept) result.push_back(triggerIndex);
//  line below prints HLT fired triggers
//  if (isAccept) std::cout <<std::dec<<  triggerIndex <<" ("<< theHltConfig.triggerName(triggerIndex)<< std::endl;;
  }
 
  return result;
}

#ifndef MenuInspector_H
#define MenuInspector_H

#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/Provenance/interface/RunID.h"
#include "DataFormats/Provenance/interface/EventID.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/Provenance/interface/ParameterSetID.h"

#include "CondFormats/L1TObjects/interface/L1GtTriggerMenuFwd.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerRecord.h"

#include "CondFormats/L1TObjects/interface/L1TUtmTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1TUtmTriggerMenuRcd.h"



#include <vector>
#include <string>
#include <map>

class MuonObjColl;

namespace edm {class ParameterSet; class Event; class EventSetup; class Run; }

class MenuInspector { 
public:
  MenuInspector(const edm::ParameterSet&, edm::ConsumesCollector cColl);
//, edm::esConsumes<edm::Transition::BeginRun> && esConsum);
  virtual ~MenuInspector();

  const std::vector<std::string> & namesAlgoHLT() const { return theNamesAlgoHLT; }
  const std::vector<std::string> & namesAlgoL1() const { return theNamesAlgoL1; }

  std::vector<unsigned int> firedAlgosHLT(const edm::Event &ev, const edm::EventSetup &es) { run(ev,es); return theFiredHLT;} 
  std::vector<unsigned int> firedAlgosL1(const edm::Event &ev, const edm::EventSetup &es)  { run(ev,es); return theFiredL1;}

  bool associateHLT(const edm::Event&, const edm::EventSetup&, MuonObjColl * muonColl);

  virtual bool checkRun(const edm::Run&, const edm::EventSetup &es);

private:
  edm::EventNumber_t lastEvent;
  edm::RunNumber_t   lastRun;

  bool run(const edm::Event &ev, const edm::EventSetup &es);
  std::vector<unsigned int> runFiredAlgosHLT(const edm::Event&, const edm::EventSetup&);
  std::vector<unsigned int> runFiredAlgosL1(const edm::Event&, const edm::EventSetup&);

  virtual bool beginRun(edm::Run& r, const edm::EventSetup & es) { return checkRun(r,es); }

  virtual bool filter(edm::Event&, const edm::EventSetup&);
//  virtual bool filterL1(edm::Event&, const edm::EventSetup&);
//  virtual bool filterHLT(edm::Event&, const edm::EventSetup&);

  unsigned int theCounterIN, theCounterL1, theCounterHLT;

  HLTConfigProvider theHltConfig;
  edm::ParameterSetID theTriggerParSetID;
  bool theWarnNoColl;

  std::vector<std::string> theNamesAlgoHLT, theNamesAlgoL1;
  std::vector<unsigned int> theFiredHLT;
  std::vector<unsigned int> theFiredL1;
  std::map<std::string, int> theNamesCheckHltMuMatchIdx;
  std::map<std::string, int> theNamesIndicesMarkedPrescaled;

};
#endif


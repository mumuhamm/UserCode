#ifndef L1PhaseIIObjMaker_H
#define L1PhaseIIObjMaker_H

#include <vector>
#include "UserCode/OmtfDataFormats/interface/L1PhaseIIObj.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Provenance/interface/RunID.h"
#include "DataFormats/Provenance/interface/EventID.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

namespace edm {class Event; }

class L1PhaseIIObjMaker {
public:
  L1PhaseIIObjMaker(const  edm::ParameterSet & cfg, edm::ConsumesCollector&& cColl);
  const std::vector<L1PhaseIIObj> & operator()(const edm::Event &ev) { run(ev); return theL1PhaseIIObjs; }

private:
  void run(const edm::Event &ev);
  bool makeRegCandidates(const edm::Event &ev, L1PhaseIIObj::TYPE t, std::vector<L1PhaseIIObj> &result);
  bool makeGmtCandidates(const edm::Event &ev, L1PhaseIIObj::TYPE t, std::vector<L1PhaseIIObj> &result);

private:
/*
  template <class T> L1PhaseIIObj makeL1PhaseIIObj( T& t, L1PhaseIIObj::TYPE type) {
    L1PhaseIIObj obj;
    obj.bx = t.bx();
    obj.q  = t.quality();
    obj.pt = t.ptValue();
    obj.eta = t.etaValue();
    obj.phi = t.phiValue();
    //obj.charge = t.charge();
    obj.type = type;
    return obj;
  }
*/
private:
  edm::ParameterSet   theConfig;
  std::vector<L1PhaseIIObj>  theL1PhaseIIObjs;
  edm::EventNumber_t lastEvent;
  edm::RunNumber_t   lastRun;

};
#endif


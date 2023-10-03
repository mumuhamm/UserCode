#ifndef OmtfTreeAnalysis_H
#define OmtfTreeAnalysis_H

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "TObjArray.h"

class AnaEvent;
class AnaEff;
class AnaMuonDistribution;
class AnaDataEmul;
class AnaDiMu;
class AnaMenu;
class AnaSecMuSelector;
class AnaTime;
class AnaSynch;
class AnaL1Distribution;

namespace edm { class Event; class EventSetup; }

//class OmtfTreeAnalysis : public edm::one::EDAnalyzer<edm::one::SharedResources,edm::one::WatchRuns> {
class OmtfTreeAnalysis : public edm::one::EDAnalyzer<edm::one::WatchRuns> {
public:
  OmtfTreeAnalysis(const edm::ParameterSet & cfg);
  virtual ~OmtfTreeAnalysis(){}
  virtual void beginJob();
  virtual void beginRun(const edm::Run&,  const edm::EventSetup& es);
  virtual void   endRun(const edm::Run&,  const edm::EventSetup& es) { }
  virtual void analyze(const edm::Event&, const edm::EventSetup& es);
  virtual void endJob();

private:
  TObjArray theHistos;
  edm::ParameterSet theConfig;

  AnaEvent            *theAnaEvent;
  AnaMuonDistribution *theAnaMuonDistribution;
  AnaMenu             *theAnaMenu;
  AnaDataEmul         *theAnaDataEmul;
  AnaEff              *theAnaEff;
  AnaSecMuSelector    *theAnaSecMu;
  AnaTime             *theAnaTime;
  AnaSynch            *theAnaSynch;
  AnaDiMu             *theAnaDiMu;
  AnaL1Distribution   *theAnaL1Dist;


}; 

#endif

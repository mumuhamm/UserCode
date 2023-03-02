#ifndef UserCode_OmtfAnalysis_SynchroCheck_H
#define UserCode_OmtfAnalysis_SynchroCheck_H

#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/CSCDigi/interface/CSCCorrelatedLCTDigiCollection.h"
#include "DataFormats/RPCRecHit/interface/RPCRecHitCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCRecHit2DCollection.h"
#include "DataFormats/RPCDigi/interface/RPCDigiCollection.h"


namespace edm { class ParameterSet; class Event; class EventSetup; }
namespace reco { class Muon; }
class GlobalTrackingGeometry;
class GlobalTrackingGeometryRecord;
class CSCGeometry;
class RPCGeometry;
class MuonGeometryRecord;
class MagneticField;
class IdealMagneticFieldRecord;
class TObjArray;
class Propagator;
class TrackingComponentsRecord;
class TH1D;
class TH2D;
class DetBxStatObj;

class SynchroCheck {
public:
  SynchroCheck(const edm::ParameterSet & cfg, edm::ConsumesCollector cColl);
  ~SynchroCheck();
  void checkHitCsc(const reco::Muon *aMuon, const edm::Event &ev, const edm::EventSetup &es);
  void checkHitRpc(const reco::Muon *aMuon, const edm::Event &ev, const edm::EventSetup &es);
  void checkStripRpc(const reco::Muon *aMuon, const edm::Event &ev, const edm::EventSetup &es);
  void checkStripCsc(const reco::Muon *aMuon, const edm::Event &ev, const edm::EventSetup &es);
  void checkInside(const reco::Muon *aMuon, const edm::Event &ev, const edm::EventSetup &es);
  void initHistos( TObjArray & histos);

private:
  TH1D *hCscDistX, *hCscPullX;
  TH1D *hRpcDistX, *hRpcPullX;
  TH1D *hRpcHitDistX, *hCscHitDistX;
  TH2D *hME13P_Strip, *hME13N_Strip;
  TH2D *hME13P_Inside, *hME13N_Inside;
  TH2D *hCscDistr;
  TH1D *hRpcHitDistPhi, *hCscHitDistPhi;
  DetBxStatObj *theDetBxStat; 
  DetBxStatObj *theDetPullXStat; 

  const edm::EDGetTokenT<CSCCorrelatedLCTDigiCollection> theLctToken;
  const edm::EDGetTokenT<RPCDigiCollection> theRpcDigiToken;
  const edm::EDGetTokenT<CSCRecHit2DCollection> theCscToken;
  const edm::EDGetTokenT<RPCRecHitCollection> theRpcToken;
  const edm::ESGetToken<GlobalTrackingGeometry, GlobalTrackingGeometryRecord> theGeomteryToken;
  const edm::ESGetToken<CSCGeometry, MuonGeometryRecord> theCscGeomToken;
  const edm::ESGetToken<RPCGeometry, MuonGeometryRecord> theRpcGeomToken;
  const edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> theFieldToken;
  const edm::ESGetToken<Propagator, TrackingComponentsRecord> thePropagatorAnyToken;

};

#endif

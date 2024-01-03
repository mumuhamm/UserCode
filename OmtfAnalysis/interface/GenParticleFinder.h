#ifndef L1RpcTriggerAnalysis_GenParticlefinder_H
#define L1RpcTriggerAnalysis_GenParticlefinder_H

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Provenance/interface/RunID.h"
#include "DataFormats/Provenance/interface/EventID.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "UserCode/OmtfDataFormats/interface/GenObj.h"
#include "UserCode/OmtfDataFormats/interface/GenObjColl.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "MuonAnalysis/MuonAssociators/interface/PropagateToMuon.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "MuonAnalysis/MuonAssociators/interface/PropagateToMuonSetup.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "CondFormats/AlignmentRecord/interface/TrackerSurfaceDeformationRcd.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "DataFormats/GeometryVector/interface/GlobalVector.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MuonAnalysis/MuonAssociators/interface/PropagateToMuon.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

namespace edm { class Event; class EventSetup; }
namespace reco { class Muon; }
namespace edm { class EDAnalyzer; }

#include <vector>

class TObjArray;

class GenParticlefinder {

public:
  GenParticlefinder( const edm::ParameterSet& cfg, edm::ConsumesCollector&& cColl);
 
  const reco::GenParticle* result( const edm::Event &ev, const edm::EventSetup &es) { run(ev,es); return theGenPart; }
  std::vector<GenObj> genparticles( const edm::Event &ev, const edm::EventSetup &es) { run(ev,es); return theGenObjs; }
  //void getHandles(const edm::Event &ev, const edm::EventSetup &es);
private:

  void getSimVertex(const edm::Event &ev);
  void getGenParticles(const edm::Event &ev, const edm::EventSetup &es);
  void getTrackingParticles(const edm::Event &ev);
  
  bool run(const edm::Event &ev, const edm::EventSetup &es);

private:
  edm::EventNumber_t lastEvent;
  edm::RunNumber_t   lastRun;
  edm::ParameterSet  theConfig;

  unsigned int theAllParticles;
  const reco::GenParticle* theGenPart;
  const edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> theBFieldToken;
  const SimVertex theSimVertex;
  std::vector<GenObj> theGenObjs; 

  edm::ParameterSet muProp1stParams;
  edm::ParameterSet muProp2ndParams;
  
  const PropagateToMuonSetup muPropagatorSetup1st_;
  const PropagateToMuonSetup muPropagatorSetup2nd_;

  PropagateToMuon muPropagator1st_;
  PropagateToMuon muPropagator2nd_;

   

    
  PropagateToMuon muPropagatorToArbitraryStations;
  

};
#endif

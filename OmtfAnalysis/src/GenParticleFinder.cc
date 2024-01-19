#include "UserCode/OmtfAnalysis/interface/GenParticleFinder.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Handle.h"


#include "UserCode/OmtfAnalysis/interface/Utilities.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "TObjArray.h"
#include "TH1D.h"
#include "TH2D.h"

#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
using namespace std;
using namespace edm;


GenParticlefinder::GenParticlefinder(const edm::ParameterSet& cfg, edm::ConsumesCollector&& cColl)
  : lastEvent(0), lastRun(0), theConfig(cfg), 
    theAllParticles(0), theGenPart(0),theBFieldToken(cColl.esConsumes()),
    muPropagatorSetup1st_(cfg.getParameter<edm::ParameterSet>("muProp1st"),  std::move(cColl)),//consumesCollector()),
    muPropagatorSetup2nd_(cfg.getParameter<edm::ParameterSet>("muProp2nd"),  std::move(cColl))//consumesCollector())
{ 

  if (theConfig.exists("genColl")){
    edm::InputTag genCollTag =  theConfig.getParameter<edm::InputTag>("genColl");
    cColl.consumes<reco::GenParticleCollection>(genCollTag);
  }

  if (theConfig.exists("trackingParticle")){
    edm::InputTag trackingPartTag =  theConfig.getParameter<edm::InputTag>("trackingParticle");
    cColl.consumes<TrackingParticleCollection>(trackingPartTag);
  }  
  
   if (theConfig.exists("simVertex")){
    edm::InputTag simVertexTag =  theConfig.getParameter<edm::InputTag>("simVertex");
    cColl.consumes<TrackingParticleCollection>(simVertexTag);
  }  
  
  
}

void GenParticlefinder::getGenParticles(const edm::Event &ev, const edm::EventSetup &es){
  //getHandles(ev, es);
  muPropagator1st_ = muPropagatorSetup1st_.init(es);
  muPropagator2nd_ = muPropagatorSetup2nd_.init(es);
  const MagneticField &theBField = es.getData(theBFieldToken);
  const MagneticField *theMagneticField = &theBField;

  edm::Handle<reco::GenParticleCollection> genparticles;
  edm::InputTag genCollTag =  theConfig.getParameter<edm::InputTag>("genColl");
  ev.getByLabel( genCollTag, genparticles);
  if (!genparticles.isValid()) return;
  
  for (reco::GenParticleCollection::const_iterator im = genparticles->begin(); im != genparticles->end(); ++im) {
    int motherPdgId = im->numberOfMothers()>0 ? im->mother()->pdgId(): 0;
    GlobalPoint genglobalpoint(im->vx(), im->vy(), im->vz());
    GlobalVector genglobalmomvector(im->px(), im->py(), im->pz());
    FreeTrajectoryState ftrajstate(genglobalpoint, genglobalmomvector, im->charge(), theMagneticField);
    TrajectoryStateOnSurface stateAtMuSt1 = muPropagator1st_.extrapolate(ftrajstate);
    TrajectoryStateOnSurface stateAtMuSt2 = muPropagator2nd_.extrapolate(ftrajstate);
    
    if (stateAtMuSt1.isValid()&& stateAtMuSt2.isValid()) {
            std::cout << "genPart_Propagatedeta_AtSt2 = " << stateAtMuSt2.globalPosition().eta() << std::endl;
            std::cout << "genPart_Propagatedphi_AtSt2 = " << stateAtMuSt2.globalPosition().phi() << std::endl;
            GenObj genObj(im->charge(),im->pdgId(),im->status(),motherPdgId);
            genObj.setVertexXYZ(im->vx(),im->vy(),im->vz());
            genObj.setPtEtaPhiM(im->pt(),stateAtMuSt2.globalPosition().eta(),stateAtMuSt2.globalPosition().phi(),im->mass());    
            theGenObjs.push_back(genObj);
  }
 }  
}

void GenParticlefinder::getTrackingParticles(const edm::Event &ev){

  edm::Handle<TrackingParticleCollection> trackingParticleHandle;
  edm::InputTag trackingPartTag =  theConfig.getParameter<edm::InputTag>("trackingParticle");
  ev.getByLabel(trackingPartTag, trackingParticleHandle);
  if (!trackingParticleHandle.isValid()) return;
  
  for (TrackingParticleCollection::const_iterator iTP = trackingParticleHandle->begin();
       iTP!=trackingParticleHandle->end();++iTP){
      
    if(iTP->eventId().bunchCrossing() != 0) continue;
    if (abs(iTP->pdgId()) != 13) continue;
    
    int motherPdgId = 0;
    GenObj genObj(iTP->charge(),iTP->pdgId(),iTP->status(),motherPdgId);
    genObj.setVertexXYZ(iTP->vx(),iTP->vy(),iTP->vz());
    genObj.setPtEtaPhiM(iTP->pt(),iTP->eta(),iTP->phi(),iTP->mass());    
    theGenObjs.push_back(genObj);
  }  
}

bool GenParticlefinder::run(const edm::Event &ev, const edm::EventSetup &es)
{

  if (lastEvent==ev.id().event() && lastRun==ev.run()) return false;
  lastEvent = ev.id().event() ;
  lastRun = ev.run();
  theGenPart = 0;
  theGenObjs.clear();

  if(theConfig.exists("genColl")) getGenParticles(ev,es);
  if(theConfig.exists("trackingParticle")) getTrackingParticles(ev);
     
  //
  // sort resulting container by pT, in descending order
  //
  std::sort(theGenObjs.begin(), theGenObjs.end(), []( const GenObj &m1, const GenObj &m2) { return m1.pt() > m2.pt(); } );
  
  return true;
}


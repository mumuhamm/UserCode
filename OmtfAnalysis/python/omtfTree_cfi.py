import FWCore.ParameterSet.Config as cms

#
# OMTF tree 
#
omtfTree = cms.EDAnalyzer("OmtfTreeMaker",
  histoFileName = cms.string("omtfHelper.root"),
  treeFileName = cms.string("omtfTree_mc.root"),

  menuInspector = cms.PSet( 
    namesCheckHltMuMatch = cms.vstring(
      "HLT_IsoMu20_v","HLT_IsoMu24_v","HLT_IsoMu27_v"
    ),

    warnNoColl = cms.untracked.bool(False) 
  ),

   linkSynchroGrabber = cms.PSet(
     rawSynchroTag = cms.InputTag("muonRPCDigis"),
     writeHistograms = cms.untracked.bool(True),
     deltaR_MuonToDetUnit_cutoff = cms.double(0.3),
     checkInside = cms.bool(True),
     linkMonitorPSet = cms.PSet(
       useFirstHitOnly = cms.untracked.bool(True),
       dumpDelays = cms.untracked.bool(True) # set to True for LB delay plots
     ),
     synchroSelector = cms.PSet(
       checkRpcDetMatching_minPropagationQuality = cms.int32(0),
       checkRpcDetMatching_matchingScaleValue = cms.double(3),
       checkRpcDetMatching_matchingScaleAuto  = cms.bool(True),
       checkUniqueRecHitMatching_maxPull = cms.double(2.),
       checkUniqueRecHitMatching_maxDist = cms.double(5.)
     )
   ),
  
  l1ObjMaker = cms.PSet(
    #omtfEmulSrc = cms.InputTag('simOmtfDigis','OMTF',''),
    #bmtfDataSrc = cms.InputTag('simKBmtfDigis','BMTF',''),
    #emtfDataSrc = cms.InputTag('simEmtfDigis','EMTF',''),
    #gmtEmulSrc = cms.InputTag('simGmtStage2Digis','',''),    
    #data---
    #omtfEmulSrc = cms.InputTag('omtfEmulator','OMTF',''),
    omtfDataSrc = cms.InputTag('gmtStage2Digis','OMTF'),
    emtfDataSrc = cms.InputTag('gmtStage2Digis','EMTF'),
    bmtfDataSrc = cms.InputTag('gmtStage2Digis','BMTF'),
    gmtDataSrc = cms.InputTag('gmtStage2Digis','Muon'),
    #gmtEmulSrc = cms.InputTag('emulGmtStage2Digis',''),
    #------------     
    warnNoColl = cms.untracked.bool(True)
  ),
  l1PhaseIIObjMaker = cms.PSet(
    gmtEmulSrc = cms.InputTag('l1tTkMuonsGmt','',''),   
    warnNoColl = cms.untracked.bool(True)
  ),
  genObjectFinder = cms.PSet(
      genColl = cms.InputTag("genParticles"),
      trackingParticle = cms.InputTag("mix","MergedTrackTruth"),
      warnNoColl = cms.untracked.bool(True)
  ),                                 
  closestTrackFinder = cms.PSet(
    trackColl = cms.InputTag("generalTracks"),
    warnNoColl = cms.untracked.bool(False)
  ),                         

  onlyBestMuEvents = cms.bool(False),
  bestMuonFinder = cms.PSet(
    muonColl = cms.InputTag("muons"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    warnNoColl = cms.untracked.bool(True),
    requireInnerTrack = cms.bool(True),
    requireOuterTrack = cms.bool(False),
    requireGlobalTrack = cms.bool(False),
    requireLoose       = cms.bool(True),
    minPt = cms.double(3.),
    maxTIP = cms.double(0.2),
    maxAbsEta = cms.double(2.4),
    minNumberTrackerHits = cms.int32(6),
    minNumberRpcHits = cms.int32(0),
    minNumberDtCscHits = cms.int32(0),
    minNumberOfMatchedStations = cms.int32(0),
    cutTkIsoRel = cms.double(0.1),
    cutPFIsoRel = cms.double(0.15),
    deltaPhiUnique = cms.double(1.0),
    deltaEtaUnique = cms.double(0.5),
    minPtUnique = cms.double(2.0),
    looseUnique = cms.bool(True)
  ),
   synchroCheck = cms.PSet(
    srcCSC = cms.InputTag('omtfStage2Digis'),
    srcRPC = cms.InputTag('omtfStage2Digis')
  ),
)

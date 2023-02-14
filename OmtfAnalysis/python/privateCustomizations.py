import FWCore.ParameterSet.Config as cms

##########################################
##########################################
def customize_L1TkMuonsGmt(process):

    process.CalibratedDigis.dtDigiTag = "simMuonDTDigis" 
    process.CalibratedDigis.scenario = 0

    process.dtTriggerPhase2PrimitiveDigis.debug = False
    process.dtTriggerPhase2PrimitiveDigis.dump = False
    process.dtTriggerPhase2PrimitiveDigis.scenario = 0

    process.l1tTkMuonsGmt.isolation.IsodumpForHLS = 0
    return process
##########################################
##########################################
def customize_outputCommands(process):
    process.FEVTSIMoutput.outputCommands.extend(cms.untracked.vstring('drop *',
                                                                      'keep *_genParticles_*_*',
                                                                      'keep *SimVertex*_*_*_*',
                                                                      'keep *Track*_*_*_*',                                                                                                                                        
                                                                      'keep *_prunedTrackingParticles_*_*',
                                                                      'keep *_generalTracks_*_*',
                                                                      'keep *_MergedTrackTruth_*_*',  
                                                                      'keep *_simMuonDTDigis_*_*',
                                                                      'keep *_simMuonCSCDigis_*_*',
                                                                      'keep *_simMuonRPCDigis_*_*',
                                                                      'keep *_simBmtfDigis_*_*',
                                                                      'keep *_simKBmtfDigis_*_*',
                                                                      'keep *_simOmtfDigis_*_*',
                                                                      'keep *_simEmtfDigis_*_*',   
                                                                      'keep *_simGmtStage2Digis_*_*',
                                                                      'keep *_simCscTriggerPrimitiveDigis_*_*',
                                                                      'keep *_simDtTriggerPrimitiveDigis_*_*',  
                                                                      'keep *_dtTriggerPhase2PrimitiveDigis_*_*',                                                                       
                                                                      'keep *_l1tTTTracksFromExtendedTrackletEmulation_*_*',
                                                                      'keep *_l1tTTTracksFromTrackletEmulation_*_*',
                                                                      'keep *_l1tTkStubsGmt_*_*',
                                                                      'keep *_l1tTkMuonsGmt_*_*',
                                                                      'keep *_Phase2TrackerDigi_*_*',
                                                                      'keep *_TTClusterAssociatorFromPixelDigis_*_*',
                                                                      'keep *_TTTrackAssociatorFromPixelDigisExtended_*_*',
                                                                      'keep *_TTStubsFromPhase2TrackerDigis_*_*',
                                                                      'keep *_TTClustersFromPhase2TrackerDigis_*_*',
                                                                      'keep *_TTTracks*_*_*',                                                                      
                                                                      'keep *_globalMuons_*_*',                                        
                                                                      'keep *_muons_*_*',                                                                      
    ))
    return process
##########################################
##########################################
def customize_extra_outputCommands(process):
    process.FEVTSIMoutput.outputCommands.extend(cms.untracked.vstring(                                                                                                                      
                                                                      'keep *_g4SimHits_MuonCSCHits_*',
                                                                      'keep *_g4SimHits_MuonDTHits_*',
                                                                      'keep *_g4SimHits_MuonGEMHits_*',
                                                                      'keep *_g4SimHits_MuonME0Hits_*',
                                                                      'keep *_g4SimHits_MuonRPCHits_*',
                                                                      'keep *_g4SimHits_Stopped*_*',
                                                                      'keep *_standAloneMuons_*_*',
                                                                      'keep *_muons_*_*',
                                                                      'keep TrackingRecHitsOwned_*_*_*',
                                                                      'keep csctfTrackStubCSCTriggerContainer_*_*_*',
                                                                      'keep edmTriggerResults_*_*_*'
    ))
    return process
##########################################
##########################################
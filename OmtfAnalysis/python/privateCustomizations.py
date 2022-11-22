import FWCore.ParameterSet.Config as cms

##########################################
##########################################
def customize_L1TkMuonsGmt(process):
    process.L1TkMuonsGmt.trackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth")
    process.L1TkMuonsGmt.mcTruthTrackInputTag = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks")
    process.L1TkMuonsGmt.isolation.IsodumpForHLS = 0
    return process
##########################################
##########################################
def customize_outputCommands(process):
    process.FEVTSIMoutput.outputCommands.extend(cms.untracked.vstring('keep *_simMuonDTDigis_*_*',
                                                                      'keep *_simMuonCSCDigis_*_*',
                                                                      'keep *_simMuonRPCDigis_*_*',
                                                                      'keep *_simBmtfDigis_*_*',
                                                                      'keep *_simKBmtfDigis_*_*',
                                                                      'keep *_simOmtfDigis_*_*',
                                                                      'keep *_simEmtfDigis_*_*',
                                                                      'keep *_simGmtStage2Digis_*_*',
                                                                      'keep *_gmtMuons_*_*',
                                                                      'keep *_L1TkMuonsGmt_*_*',
                                                                      'keep *_g4SimHits_MuonCSCHits_*',
                                                                      'keep *_g4SimHits_MuonDTHits_*',
                                                                      'keep *_g4SimHits_MuonGEMHits_*',
                                                                      'keep *_g4SimHits_MuonME0Hits_*',
                                                                      'keep *_g4SimHits_MuonRPCHits_*',
                                                                      'keep *_g4SimHits_Stopped*_*',
                                                                      'keep *_TTClusterAssociatorFromPixelDigis_*_*',
                                                                      'keep *_simCscTriggerPrimitiveDigis_*_*',
                                                                      'keep *_simDtTriggerPrimitiveDigis_*_*',
                                                                      'keep *_MergedTrackTruth_*_*'
    ))
    return process
##########################################
##########################################

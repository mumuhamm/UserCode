## import skeleton process
import FWCore.ParameterSet.Config as cms

process = cms.Process("DAS")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      'root://cms-xrd-global.cern.ch//store/mc/Phase2Spring23DIGIRECOMiniAOD/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU140_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v2/2560000/00ce3255-aa8a-465b-883e-d61154233a82.root'
    )
)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('thinned_MB_PU140.root'),
    outputCommands = cms.untracked.vstring(['drop *',
                                                                      'keep *_genParticles_*_*',
                                                                      'keep *_prunedTrackingParticles_*_*',
                                                                      'keep *_generalTracks_*_*',
                                                                      'keep *_MergedTrackTruth_*_*',
                                                                      'keep *_simMuonDTDigis_*_*',
                                                                      'keep *_simMuonCSCDigis_*_*',
                                                                      'keep *_simMuonRPCDigis_*_*',
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
                                                                      'keep *_globalMuons_*_*',                                        
                                                                      'keep *_muons_*_*',  ])
)

process.end = cms.EndPath(process.out)

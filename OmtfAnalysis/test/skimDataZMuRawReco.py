## import skeleton process
import FWCore.ParameterSet.Config as cms

process = cms.Process("DAS")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023Reco_cff')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')






from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_Prompt_v4', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'file:111d9cd0-8bfe-41f2-9848-3b546649e4ca.root'
)
)



"""
process.load('EventFilter.DTRawToDigi.dtunpacker_cfi')
process.muonDTDigis.inputLabel = cms.InputTag('rawDataCollector')
process.dtdigis = cms.Path(process.muonDTDigis)

#process.load('EventFilter.RPCRawToDigi.rpcUnpacker_cfi')
import EventFilter.RPCRawToDigi.rpcUnpacker_cfi
process.muonRPCDigis = EventFilter.RPCRawToDigi.rpcUnpacker_cfi.rpcunpacker.clone()
process.muonRPCDigis.InputLabel = cms.InputTag("rawDataCollector")
process.rpcdigis = cms.Path(process.muonRPCDigis)


from EventFilter.CSCRawToDigi.muonCSCDCCUnpacker_cfi import muonCSCDCCUnpacker
process.muonCSCDigis = muonCSCDCCUnpacker.clone(
    # This mask is needed by the examiner
    ExaminerMask = 0x1FEBF7F6
)
process.cscdigis = cms.Path(process.muonCSCDigis)
'keep *_muonDTDigis_*_*',
'keep *_muonRPCDigis_*_*',
'keep *_muonCSCDigis_*_*',

"""

process.load('EventFilter.L1TRawToDigi.omtfStage2Digis_cfi')
process.omtfStage2Digis.inputLabel = cms.InputTag('rawDataCollector')
process.omtfStage2Digis.skipRpc   = cms.bool(False)
process.omtfdigis = cms.Path(process.omtfStage2Digis)


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('thinned_ZMuRawReco.root'),
    outputCommands = cms.untracked.vstring(['drop *',
                                                                      'keep *_TriggerResults_*_*',
                                                                      'keep edmTriggerResults_*_*_*',
                                                                      'keep edmTriggerResults_*__*',
                                                                      'keep *_l1bits_*_*',
                                                                      'keep *_hltTriggerSummaryAOD_*_*',
                                                                      'keep *_hltGtStage2ObjectMap_*_*',
                                                                      'keep *_omtfStage2Digis_*_*',
                                                                      'keep *_gmtStage2Digis_Muon_*',
                                                                      'keep *_gtStage2Digis_Muon_*',
                                                                      'keep *_gmtStage2Digis_OMTF_*',
                                                                      'keep *_gmtStage2Digis_BMTF_*',
                                                                      'keep *_gmtStage2Digis_EMTF_*',
                                                                      'keep l1tMuonBXVector_*_*_*',
                                                                      'keep l1tRegionalMuonCandBXVector_*_*_*',
                                                                      'keep *_gtDigis_*_*',
                                                                      'keep *_displacedMuons__*',
                                                                      'keep *_offlineBeamSpot_*_*',
                                                                      'keep *_displacedTracks_*_*',
                                                                      'keep *_standAloneMuons_*_*',
                                                                      'keep *_generalTracks_*_*',
                                                                      'keep TrackingRecHitsOwned_*_*_*',
                                                                      'keep Trajectorys_*_*_*',
                                                                      'keep recoTrackExtras_*_*_*',
                                                                      'keep recoMuonTrackLinkss_*_*_*',
                                                                      'keep recoTracks_*_*_*',
                                                                      'keep *_offlinePrimaryVertices_*_*',
                                                                      'keep *_offlinePrimaryVerticesWithBS_*_*',
                                                                      'keep *_globalMuons_*_*',                                        
                                                                      'keep *_muons__*',
                                                                      'keep TrajectorySeeds_*_*_*',
                                                                      'keep recoMuons_*_*_*',
                                                                      'keep TrackCandidates_*_*_*',
                                                                      'keep recoMuons_*__*',])
)


process.keepCollection = cms.EndPath(process.out)
#process.schedule = cms.Schedule(process.dtdigis, process.rpcdigis, process.cscdigis, process.keepCollection)
process.schedule = cms.Schedule(process.omtfdigis, process.keepCollection)


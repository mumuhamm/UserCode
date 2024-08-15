import FWCore.ParameterSet.Config as cms
import copy
process = cms.Process('OMTFanalysis')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",

                            fileNames = cms.untracked.vstring(
                                #'file:///scratch_cmsse/akalinow/CMS/Data/Run2022A/SingleMuon/RAW-RECO/ZMu-10Dec2022-v2/2560000/f436671f-98cd-4481-b8a5-949b512ba774.root'                                
                                #'root://cms-xrd-global.cern.ch//store/data/Run2022A/SingleMuon/RAW-RECO/ZMu-10Dec2022-v2/2560000/f436671f-98cd-4481-b8a5-949b512ba774.root'
                    #'root://cms-xrd-global.cern.ch//store/data/Run2022B/SingleMuon/RAW-RECO/ZMu-PromptReco-v1/000/355/558/00000/59b3ee22-5304-4dd0-bd4d-16d2b659c964.root' 
                                #'root://cmsxrootd-kit.gridka.de:1094//store/data/Run2022B/SingleMuon/RAW-RECO/ZMu-PromptReco-v1/000/355/100/00000/672cc5a4-0957-45c3-a46a-a5e06d3a2e50.root'               
                #'file:/eos/user/a/almuhamm/OMTF_UW/Simulated_Samples/ForMyStudy/Qm_4thApril/0000/SingleMu_OneOverPt_1_100_m_298.root'
                #'root://cms-xrd-global.cern.ch//store/mc/Run3Winter23Reco/DoubleMuon_Pt-1To1000_gun/GEN-SIM-RECO/126X_mcRun3_2023_forPU65_v1-v2/2560000/006cd832-bf41-4895-a97c-81ac6bbab7b9.root'
#                                'root://cms-xrd-global.cern.ch//store/data/Run2023B/Muon1/RAW-RECO/ZMu-PromptReco-v1/000/366/469/00000/70d9986d-9df0-46c8-b6be-9d96a8113ccc.root'
#'root://cms-xrd-global.cern.ch//store/data/Run2024F/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/382/216/00000/2e2bbd9a-3b2d-466c-bc8c-4a6bed50486d.root'
#'root://cms-xrd-global.cern.ch//store/data/Run2024F/Muon1/RAW-RECO/ZMu-PromptReco-v1/000/381/984/00000/48418523-be4c-4a8a-bce0-fb1beac22dc7.root'
'root://cms-xrd-global.cern.ch//store/data/Run2024F/Muon1/RAW-RECO/ZMu-PromptReco-v1/000/382/213/00000/9d3ed822-bbcb-43f2-96b0-3b22f8d72244.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()
)



process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(50)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')

"""
process.load("L1Trigger.DTTrigger.dtTriggerPrimitiveDigis_cfi")
process.dtTriggerPrimitiveDigis.digiTag = "muonDTDigis"
process.CalibratedDigis.lutDumpFlag = cms.untracked.bool(False)


#DTTriggerPhase2
process.load("L1Trigger.DTTriggerPhase2.dtTriggerPhase2PrimitiveDigis_cfi")
process.dtTriggerPhase2PrimitiveDigis.digiTag = cms.InputTag("CalibratedDigis")
process.dtTriggerPhase2PrimitiveDigis.debug = False
process.dtTriggerPhase2PrimitiveDigis.dump = False
process.dtTriggerPhase2PrimitiveDigis.scenario = 0
"""


#####OMTF PhaseI Emulator
#simOmtfDigis_extrapolSimple_cfi.py

#import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi
import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi.simOmtfDigis.clone()


process.omtfEmulator.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcCSC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcRPC = cms.InputTag('omtfStage2Digis')



process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x00012_oldSample_3_30Files_grouped1_classProb17_recalib2.xml")
process.omtfEmulator.rpcMaxClusterSize = cms.int32(3)
process.omtfEmulator.rpcMaxClusterCnt = cms.int32(2)
process.omtfEmulator.rpcDropAllClustersIfMoreThanMax = cms.bool(True)

process.omtfEmulator.goldenPatternResultFinalizeFunction = cms.int32(9)
process.omtfEmulator.noHitValueInPdf = cms.bool(True)
process.omtfEmulator.minDtPhiQuality = cms.int32(2)
process.omtfEmulator.minDtPhiBQuality = cms.int32(4)
process.omtfEmulator.lctCentralBx = cms.int32(6)
process.omtfEmulator.sorterType = cms.string("byLLH")
process.omtfEmulator.ghostBusterType = cms.string("byRefLayer")
import L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff
process.omtfParameter=L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff.omtfParams.clone()
#process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0009.xml")#phase 1
process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0008.xml") #phase 2


"""
process.L1MuonAnalyzerOmtf= cms.EDAnalyzer("L1MuonAnalyzerOmtf",
                                 etaCutFrom = cms.double(0.82), #OMTF eta range
                                 etaCutTo = cms.double(1.24),
                                 L1OMTFInputTag  = cms.InputTag("gmtStage2Digis","OMTF"),
                                 #nn_pThresholds = cms.vdouble(nn_pThresholds), 
                                 analysisType = cms.string(analysisType),

                                 simTracksTag = cms.InputTag('g4SimHits'),
                                 simVertexesTag = cms.InputTag('g4SimHits'),

                                 matchUsingPropagation = cms.bool(True),
                                 muonMatcherFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/muonMatcherHists_100files_smoothStdDev_withOvf.root") #if you want to make this file, remove this entry#if you want to make this file, remove this entry
                                 #muonMatcherFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/muonMatcherHists_noPropagation_t74.root")
                                        )


process.l1MuonAnalyzerOmtfPath = cms.Path(process.L1MuonAnalyzerOmtf)
"""
process.load('UserCode.OmtfAnalysis.omtfTree_cfi')
process.muAnalyzerPath = cms.Path(process.omtfTree)

process.omtf_step = cms.Sequence(process.omtfStage2Digis+process.omtfEmulator)
#process.omtf_step = cms.Sequence(process.gmtStage2Digis+process.omtfEmulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.DTPhase2DigisPath = cms.Path(process.omtf_step)
#process.DTPhase2DigisPath = cms.Path(process.CalibratedDigis * process.dtTriggerPhase2PrimitiveDigis * process.omtf_step)

process.schedule = cms.Schedule( process.muAnalyzerPath, process.DTPhase2DigisPath)


#Setup FWK for multithreaded
process.options.numberOfThreads = 1
process.options.numberOfStreams = 0
process.options.numberOfConcurrentLuminosityBlocks = 1
process.options.eventSetup.numberOfConcurrentIOVs = 1


#process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")
process.load("TrackingTools.RecoGeometry.RecoGeometries_cff")
process.load("TrackingTools.TrackRefitter.TracksToTrajectories_cff")
#process.load("TrackingTools.TrackRefitter.globalMuonTrajectories_cff")

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion


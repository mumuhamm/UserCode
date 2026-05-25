import FWCore.ParameterSet.Config as cms
import copy
process = cms.Process('OMTFanalysis')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load('Configuration.StandardSequences.RawToDigi_cff')
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
'root:///eos/user/a/almuhamm/01.MuonTech/WorkArea_ForLXPLUS9/CMSSW_14_1_0_pre7/src/UserCode/OmtfAnalysis/test/thinned_ZMuRawReco.root'
#'root:///eos/user/a/almuhamm/01.MuonTech/WorkArea_ForLXPLUS9/CMSSW_14_1_0_pre7/src/UserCode/OmtfAnalysis/test/111d9cd0-8bfe-41f2-9848-3b546649e4ca.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()
)







process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(50)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_Prompt_v4', '')



#process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
#process.load('EventFilter.L1TRawToDigi.bmtfDigis_cfi')
#process.load('EventFilter.L1TRawToDigi.emtfStage2Digis_cfi')
#process.load('EventFilter.L1TRawToDigi.gmtStage2Digis_cfi')
#process.load('EventFilter.L1TRawToDigi.caloStage2Digis_cfi')
#process.load('EventFilter.L1TXRawToDigi.twinMuxStage2Digis_cfi')
#process.load('EventFilter.L1TRawToDigi.omtfStage2Digis_cfi')
#process.omtfStage2Digis.inputLabel = cms.InputTag('rawDataCollector')
#process.omtfStage2Digis.skipRpc   = cms.bool(False)

"""
#if muonDTDigis are explicitly required 
process.load('EventFilter.DTRawToDigi.dtunpacker_cfi')
process.muonDTDigis.inputLabel = cms.InputTag('rawDataCollector')

#DTTrigger -Run3
process.load("L1Trigger.DTTrigger.dtTriggerPrimitiveDigis_cfi")
process.dtTriggerPrimitiveDigis.digiTag = "muonDTDigis"




#DTTriggerPhase2
process.load("L1Trigger.DTTriggerPhase2.dtTriggerPhase2PrimitiveDigis_cfi")
process.dtTriggerPhase2PrimitiveDigis.digiTag = cms.InputTag("CalibratedDigis")
process.dtTriggerPhase2PrimitiveDigis.debug = False
process.dtTriggerPhase2PrimitiveDigis.dump = False
process.dtTriggerPhase2PrimitiveDigis.scenario = 0
"""


#####OMTF PhaseI Emulator

import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi
#import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi.simOmtfDigis.clone()




process.omtfEmulator.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcCSC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcRPC = cms.InputTag('omtfStage2Digis')




#process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x00012_oldSample_3_30Files_grouped1_classProb17_recalib2.xml")
#process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2SimplifiedFP_t17_classProb17_recalib2_minDP0_v3.xml")
process.omtfEmulator.rpcMaxClusterSize = cms.int32(3)
process.omtfEmulator.rpcMaxClusterCnt = cms.int32(2)
process.omtfEmulator.rpcDropAllClustersIfMoreThanMax = cms.bool(True)


process.omtfEmulator.goldenPatternResultFinalizeFunction = cms.int32(10)
process.omtfEmulator.noHitValueInPdf = cms.bool(True)
process.omtfEmulator.minDtPhiQuality = cms.int32(2)
process.omtfEmulator.minDtPhiBQuality = cms.int32(4)
process.omtfEmulator.lctCentralBx = cms.int32(6)
process.omtfEmulator.sorterType = cms.string("byLLH")
process.omtfEmulator.ghostBusterType = cms.string("byRefLayer")
import L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff
process.omtfParameter=L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff.omtfParams.clone()
#import L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_extrapolSimple_cff
#process.omtfParameter=L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_extrapolSimple_cff.omtfParams.clone()

#process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0009.xml")#phase1-Displaced
process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0008.xml") #phase1


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

process.omtf_step = cms.Sequence( process.omtfEmulator)
#process.omtf_step = cms.Sequence(process.omtfStage2Digis + process.omtfEmulator)
#process.omtf_step = cms.Sequence(process.dtTriggerPrimitiveDigis+process.omtfEmulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.DTDigisPath = cms.Path(process.omtfStage2Digis * process.muonDTDigis * process.dtTriggerPrimitiveDigis * process.omtf_step)
#process.DTDigisPath = cms.Path(process.dtTriggerPrimitiveDigis * process.omtf_step)
process.DTDigisPath = cms.Path(process.omtf_step)
process.schedule = cms.Schedule( process.muAnalyzerPath, process.DTDigisPath)


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


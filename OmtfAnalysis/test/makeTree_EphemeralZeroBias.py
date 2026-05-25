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
#'root://cms-xrd-global.cern.ch//store/data/Run2024F/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/382/216/00000/2e2bbd9a-3b2d-466c-bc8c-4a6bed50486d.root'  
#'root://cms-xrd-global.cern.ch//store/data/Run2024F/Muon1/RAW-RECO/ZMu-PromptReco-v1/000/381/984/00000/48418523-be4c-4a8a-bce0-fb1beac22dc7.root'
#'root://cms-xrd-global.cern.ch//store/data/Run2024F/Muon1/RAW-RECO/ZMu-PromptReco-v1/000/382/213/00000/9d3ed822-bbcb-43f2-96b0-3b22f8d72244.root'
'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/EphemeralZeroBias0/RAW/v1/000/384/276/00000/2cfb70e4-bc7f-4e28-90d7-604f69a9d98f.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()  
)
'''
prefixPath = '/scratch_cmsse/akalinow/CMS/Data/SingleMu/12_5_2_p1_22_02_2023/SingleMu_ch0_OneOverPt_12_5_2_p1_22_02_2023/12_5_2_p1_22_02_2023/230222_141552/0000'
import glob
fileList = glob.glob(prefixPath+'/*.root')
fileList = ['file:'+aFile for aFile in fileList]
process.source.fileNames = fileList
'''

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(50)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_mc_FULL','')
####Reco-Muon

process.load('EventFilter.L1TRawToDigi.bmtfDigis_cfi')
process.load('EventFilter.L1TRawToDigi.emtfStage2Digis_cfi')
process.load('EventFilter.L1TRawToDigi.gmtStage2Digis_cfi')
process.gmtStage2Digis.InputLabel = cms.InputTag("rawDataCollector")
process.gmtStage2Digis.Setup = cms.string("stage2::GMTSetup")
process.gmtStage2Digis.FedIds = cms.vint32(1402)
process.load('EventFilter.L1TRawToDigi.caloStage2Digis_cfi')
process.load('EventFilter.L1TXRawToDigi.twinMuxStage2Digis_cfi')
process.load('EventFilter.L1TRawToDigi.omtfStage2Digis_cfi')
process.omtfStage2Digis.inputLabel = cms.InputTag('rawDataCollector')
process.omtfStage2Digis.skipRpc   = cms.bool(False)


process.recomuon = cms.EDFilter("MuonRefSelector",
                                        src = cms.InputTag("muons"),
                                        cut = cms.string('pt > 0.5 && abs(eta) > 0.83 && abs(eta) < 1.23  && isGlobalMuon == 1' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1)
                                        )


####OMTF Emulator
import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi
#import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi.simOmtfDigis.clone()
process.omtfEmulator.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcCSC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcRPC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.lctCentralBx = cms.int32(8);
process.omtfEmulator.bxMin = cms.int32(-3)
process.omtfEmulator.bxMax = cms.int32(4)
process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2SimplifiedFP_t17_classProb17_recalib2_minDP0_v3.xml")
process.omtfEmulator.rpcMaxClusterSize = cms.int32(3)
process.omtfEmulator.rpcMaxClusterCnt = cms.int32(2)
process.omtfEmulator.rpcDropAllClustersIfMoreThanMax = cms.bool(True)

process.omtfEmulator.dtRefHitMinQuality =  cms.int32(4)
process.omtfEmulator.goldenPatternResultFinalizeFunction = cms.int32(10)
process.omtfEmulator.noHitValueInPdf = cms.bool(True)
process.omtfEmulator.minDtPhiQuality = cms.int32(2)
process.omtfEmulator.minDtPhiBQuality = cms.int32(4)
process.omtfEmulator.sorterType = cms.string("byLLH")
process.omtfEmulator.ghostBusterType = cms.string("byRefLayer")
import L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff
process.omtfParameter=L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff.omtfParams.clone()
process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0009.xml")

#process.raw2digi_step = cms.Path(process.muonRPCDigis+process.muonCSCDigis+process.bmtfDigis+process.emtfStage2Digis+process.twinMuxStage2Digis+process.gmtStage2Digis+process.caloStage2Digis)

####OMTF Analyzer
process.load('UserCode.OmtfAnalysis.omtfTree_cfi')
process.muAnalyzerPath = cms.Path(process.omtfTree)
#process.ntup = cms.Sequence((process.muAnalyzerPath)*recomuon)
############################

process.omtf_step = cms.Sequence(process.gmtStage2Digis + process.omtfStage2Digis +  process.omtfEmulator)
process.ntup = cms.Sequence(process.recomuon)

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step, process.omtf_step, process.muAnalyzerPath, process.endjob_step)
#process.schedule = cms.Schedule(process.ntup, process.endjob_step)
process.ZeroBiasPath = cms.Path(process.omtf_step)
process.schedule = cms.Schedule( process.muAnalyzerPath, process.ZeroBiasPath)

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

import FWCore.ParameterSet.Config as cms
import copy
process = cms.Process('OMTFanalysis')
from pathlib import Path
import os
import random
import sys
import re
from os import listdir
from os.path import isfile, join
import glob
version = "cmssw1410pre0_CosmicData"

verbose = True
runDebug = "INFO" # or "INFO" DEBUG
useExtraploationAlgo = True

"""
if verbose:
    process.MessageLogger = cms.Service("MessageLogger",
       #suppressInfo       = cms.untracked.vstring('AfterSource', 'PostModule'),
       destinations   = cms.untracked.vstring(
                                               #'detailedInfo',
                                               #'critical',
                                               #'cout',
                                               'cerr',
                                               'omtfEventPrint'
                    ),
       categories        = cms.untracked.vstring('l1tOmtfEventPrint', 'OMTFReconstruction'),
       omtfEventPrint    = cms.untracked.PSet(
                         filename  = cms.untracked.string('log_' + version),
                         extension = cms.untracked.string('.txt'),
                         threshold = cms.untracked.string('INFO'),
                         default = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
                         #INFO   =  cms.untracked.int32(20),
                         #DEBUG   = cms.untracked.int32(20),
                         l1tOmtfEventPrint = cms.untracked.PSet( limit = cms.untracked.int32(1000000000) ),
                         OMTFReconstruction = cms.untracked.PSet( limit = cms.untracked.int32(1000000000) )
                       ),
       debugModules = cms.untracked.vstring('omtfStatge2Digis', 'omtfParameter')
    )

"""

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi') 
process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')#Configuration/Geometry/python/GeometryExtended2026D88_cff.py
#process.load('Configuration.Geometry.GeometryExtended2026D88_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


# Input source

process.source = cms.Source("PoolSource",

                            fileNames = cms.untracked.vstring(                                                               

#'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/09512332-1389-415d-8b7f-234eed09fcd1.root',
'root://eoscms.cern.ch//eos/cms/store/data/Run2024B/EphemeralZeroBias11/RAW/v1/000/378/981/00000/0003fbf8-449b-4903-928d-51a540da3c0b.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()
)
"""


process.source = cms.Source("PoolSource",

                            fileNames = cms.untracked.vstring(                                                               
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/09512332-1389-415d-8b7f-234eed09fcd1.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/25e1cb61-2880-430c-97e3-0632e47885ea.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/508d653a-7903-44cf-a4d0-1c7eda3e7330.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/7b4f9858-ad7f-4558-892a-7af2a638fbc5.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/964589a1-244a-4858-8bd4-1905b6442a2e.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/d0fd3ae5-9bce-4781-896d-e1abc5b2951d.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/d6b9c272-99c2-4701-ba99-9109b95a4354.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/14c79dfd-48d5-4adc-8948-275f09413a71.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/2076f268-7ee0-45d0-9a1b-f33fefdc688d.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/44cb1771-a056-47d9-8bef-77ba1e278373.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/6a4c6e2e-b782-4ff9-95d2-74c5cfbdf1a4.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/d57c2dde-f0db-42d4-808f-3727b50517a9.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/f9b6f437-44f3-457a-b86d-b5e6640d43ed.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/184/00000/fbe84ecc-c87c-444f-8fc8-3b99cfec107c.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/195/00000/c65c8ee0-5a9b-4e1a-9353-fe27f023d1e4.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/200/00000/a8e72e7a-b495-4f3a-b1e1-eeac16ed1cf9.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/200/00000/cb5a2dcd-3c15-429a-8587-09ab5e1b1ecf.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/201/00000/ee2758a0-bbf4-426e-9248-5c9db3136a6b.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/203/00000/d8deb107-1883-4933-b951-5b50b50011a9.root',
'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/205/00000/7cde2a5b-d016-43f2-88fc-c317c800bfdb.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()  
)

"""

#########################################################################################################################################################################
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(5)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))



process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('EventFilter.L1TRawToDigi.bmtfDigis_cfi')
process.load('EventFilter.L1TRawToDigi.emtfStage2Digis_cfi')
process.load('EventFilter.L1TRawToDigi.gmtStage2Digis_cfi')
process.load('EventFilter.L1TXRawToDigi.twinMuxStage2Digis_cfi')
process.load('EventFilter.L1TRawToDigi.omtfStage2Digis_cfi')
#process.load('EventFilter.L1TRawToDigi.omtfStage2Raw_cfi')
#process.load('EventFilter.L1TRawToDigi.caloLayer1Digis_cfi')
process.load('EventFilter.L1TRawToDigi.caloStage2Digis_cfi')
#process.load("CondTools/RPC/RPCLinkMap_sqlite_cff")




from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_mc_FULL','')
####Reco-Muon
process.recomuon = cms.EDFilter("MuonRefSelector",
                                        src = cms.InputTag("muons"),
                                        cut = cms.string('pt > 0.5 && abs(eta) > 0.83 && abs(eta) < 1.23  && isGlobalMuon == 1' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1)
                                        )


########################## Raw2Digi 
process.digiCompare = cms.EDAnalyzer("OmtfDigiCompare",
  srcRPC_OMTF = cms.InputTag('omtfStage2Digis'),
  srcRPC_PACT = cms.InputTag('muonRPCDigis'),

  srcCSC_OMTF = cms.InputTag('omtfStage2Digis'),
  srcCSC_CSC  = cms.InputTag('emtfStage2Digis'),
# srcCSC_CSC  = cms.InputTag("muonCSCDigis","MuonCSCCorrelatedLCTDigi"),
  srcALCT     = cms.InputTag("muonCSCDigis","MuonCSCALCTDigi"),
  useALCT     = cms.bool(True),

  srcOMTF_DATA = cms.InputTag('omtfStage2Digis'),
  srcOMTF_EMUL = cms.InputTag('gmtStage2Digis','OMTF'),
#  srcOMTF_EMUL = cms.InputTag('simOmtfDigis','OMTF'),

  srcDTPh_BMTF = cms.InputTag('twinMuxStage2Digis','PhIn'),
  srcDTTh_BMTF = cms.InputTag('twinMuxStage2Digis','ThIn'),
  srcDTPh_OMTF = cms.InputTag('omtfStage2Digis'),
  srcDTTh_OMTF = cms.InputTag('omtfStage2Digis'),
)



#####OMTF PhaseI Emulator
#if useExtraploationAlgo :
import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi.simOmtfDigis.clone()

"""
else :
    import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi
    process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi.simOmtfDigis.clone()
process.load('L1Trigger.Configuration.L1TRawToDigi_cff')
process.load('EventFilter.L1TRawToDigi.omtfStage2Digis_cfi') #unpacker
"""



process.omtfEmulator.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcCSC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcRPC = cms.InputTag('omtfStage2Digis')


"""
process.omtfEmulator.srcDTPh = cms.InputTag('dttfDigis')
process.omtfEmulator.srcDTTh = cms.InputTag('dttfDigis')
process.omtfEmulator.srcCSC = cms.InputTag('csctfDigis')
process.omtfEmulator.srcRPC = cms.InputTag('muonRPCDigis')
"""

"""
process.omtfEmulator.muonMatcherFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/muonMatcherHists_100files_smoothStdDev_withOvf.root")
process.omtfEmulator.sorterType = cms.string("byLLH")
process.omtfEmulator.ghostBusterType = cms.string("GhostBusterPreferRefDt") 
if useExtraploationAlgo :
    #process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuonOverlapPhase1/test/expert/omtf/Patterns_ExtraplMB1nadMB2FullAlgo_t16_classProb17_recalib2.xml")
    process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2SimplifiedFP_t17_classProb17_recalib2_minDP0_v3.xml")
    process.omtfEmulator.dtRefHitMinQuality =  cms.int32(4)
    process.omtfEmulator.usePhiBExtrapolationFromMB1 = cms.bool(True)
    process.omtfEmulator.usePhiBExtrapolationFromMB2 = cms.bool(True)
else :
    process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2SimplifiedFP_t17_classProb17_recalib2_minDP0_v3.xml")
"""


process.omtfEmulator.rpcMaxClusterSize = cms.int32(3)
process.omtfEmulator.rpcMaxClusterCnt = cms.int32(2)
process.omtfEmulator.rpcDropAllClustersIfMoreThanMax = cms.bool(True)
process.omtfEmulator.goldenPatternResultFinalizeFunction = cms.int32(10)
process.omtfEmulator.noHitValueInPdf = cms.bool(True)
process.omtfEmulator.minDtPhiQuality = cms.int32(2)
process.omtfEmulator.minDtPhiBQuality = cms.int32(4)
process.omtfEmulator.lctCentralBx = cms.int32(8)
process.omtfEmulator.bxMin = cms.int32(-3)
process.omtfEmulator.bxMax = cms.int32(4)

process.emulGmtCaloSumDigis = cms.EDProducer('L1TMuonCaloSumProducer',
    caloStage2Layer2Label = cms.InputTag("caloStage2Digis",'CaloTower'),
)
process.emulGmtStage2Digis = cms.EDProducer('L1TMuonProducer',
    barrelTFInput  = cms.InputTag("gmtStage2Digis", "BMTF"),
    overlapTFInput = cms.InputTag("omtfEmulator", "OMTF"),
#    overlapTFInput = cms.InputTag("gmtStage2Digis", "OMTF"),
    forwardTFInput = cms.InputTag("gmtStage2Digis", "EMTF"),
    #triggerTowerInput = cms.InputTag("simGmtCaloSumDigis", "TriggerTower2x2s"),
    triggerTowerInput = cms.InputTag("emulGmtCaloSumDigis", "TriggerTowerSums"),
    autoBxRange = cms.bool(True), # if True the output BX range is calculated from the inputs and 'bxMin' and 'bxMax' are ignored
    bxMin = cms.int32(-3),
    bxMax = cms.int32(4),
    autoCancelMode = cms.bool(True), # if True the cancel out methods are configured depending on the FW version number and 'emtfCancelMode' is ignored
    emtfCancelMode = cms.string("coordinate") # 'tracks' or 'coordinate'
)



process.raw2digi_step = cms.Path(process.muonRPCDigis+process.muonCSCDigis+process.bmtfDigis+process.emtfStage2Digis+process.twinMuxStage2Digis+process.gmtStage2Digis+process.caloStage2Digis)
process.omtf_step = cms.Path(process.omtfStage2Digis+process.omtfEmulator+process.digiCompare+process.emulGmtCaloSumDigis+process.emulGmtStage2Digis)
#process.omtf_step = cms.Path(process.omtfStage2Digis+process.omtfStage2Raw+process.omtfStage2Digis2+process.digiComapre+process.omtfEmulator)
process.endjob_step = cms.EndPath(process.endOfProcess)

#process.schedule = cms.Schedule(process.raw2digi_step, process.omtf_step, process.endjob_step)

#process.omtf_step = cms.Path(process.omtfStage2Digis+process.omtfEmulator)
#process.omtf_step = cms.Path(process.omtfEmulator)
process.ntup = cms.Sequence(process.recomuon)





####OMTF Analyzer
process.load('UserCode.OmtfAnalysis.omtfTree_cfi')
process.muAnalyzerPath = cms.Path(process.omtfTree)

#process.ntup = cms.Sequence((process.muAnalyzerPath)*recomuon)
############################

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step, process.omtf_step, process.muAnalyzerPath, process.endjob_step)
process.schedule = cms.Schedule(process.raw2digi_step, process.omtf_step, process.muAnalyzerPath, process.endjob_step)

#process.schedule = cms.Schedule(process.omtf_step, process.muAnalyzerPath, process.endjob_step)
#process.schedule = cms.Schedule(process.ntup, process.endjob_step)

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

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
'root://cms-xrd-global.cern.ch//store/data/Run2024E/Cosmics/AOD/PromptReco-v1/000/380/949/00000/b0bb874d-6571-46a8-9711-55d98b0578ee.root'
#'root://eoscms.cern.ch//eos/cms/store/data/Run2024B/EphemeralZeroBias11/RAW/v1/000/378/981/00000/0003fbf8-449b-4903-928d-51a540da3c0b.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()
)
"""


process.source = cms.Source("PoolSource",

                            fileNames = cms.untracked.vstring(                                                               
'root://cms-xrd-global.cern.ch//store/data/Run2024E/Cosmics/AOD/PromptReco-v1/000/380/949/00000/b0bb874d-6571-46a8-9711-55d98b0578ee.root'

#'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/179/00000/09512332-1389-415d-8b7f-234eed09fcd1.root',
#'root://cms-xrd-global.cern.ch//store/data/Run2024A/Cosmics/RAW-RECO/CosmicTP-PromptReco-v1/000/378/205/00000/7cde2a5b-d016-43f2-88fc-c317c800bfdb.root'
),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()  
)

"""

#########################################################################################################################################################################
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(5)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))






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



#####OMTF PhaseI Emulator
#if useExtraploationAlgo :
import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi.simOmtfDigis.clone()



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

"""
process.emulGmtCaloSumDigis = cms.EDProducer('L1TMuonCaloSumProducer',
    caloStage2Layer2Label = cms.InputTag("caloStage2Digis",'CaloTower'),
)
process.emulGmtStage2Digis = cms.EDProducer('L1TMuonProducer',
    barrelTFInput  = cms.InputTag("gmtStage2Digis", "BMTF"),
    overlapTFInput = cms.InputTag("omtfEmulator", "OMTF"),
    #overlapTFInput = cms.InputTag("gmtStage2Digis", "OMTF"),
    forwardTFInput = cms.InputTag("gmtStage2Digis", "EMTF"),
    #triggerTowerInput = cms.InputTag("caloStage2Digis", "TriggerTower2x2s"),
    #triggerTowerInput = cms.InputTag("caloStage2Digis", "TriggerTowerSums"),
    autoBxRange = cms.bool(True), # if True the output BX range is calculated from the inputs and 'bxMin' and 'bxMax' are ignored
    bxMin = cms.int32(-3),
    bxMax = cms.int32(4),
    autoCancelMode = cms.bool(True), # if True the cancel out methods are configured depending on the FW version number and 'emtfCancelMode' is ignored
    emtfCancelMode = cms.string("coordinate") # 'tracks' or 'coordinate'
)
"""
process.omtf_step = cms.Path(process.omtfEmulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
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
process.schedule = cms.Schedule( process.muAnalyzerPath, process.endjob_step)

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

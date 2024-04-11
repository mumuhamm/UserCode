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

verbose = True
runDebug = "INFO" # or "INFO" DEBUG
useExtraploationAlgo = True
version = "cmssw1400pre3_phaseII_prEmulation_extrapolationON"

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi') 
process.load('Configuration.Geometry.GeometryExtended2026D86Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D95_cff')
#process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')

#process.load('Configuration.Geometry.GeometryExtended2026D88_cff.py')
#process.load('Configuration.Geometry.GeometryExtended2026D99_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")

###########################################################################################################################
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
       debugModules = cms.untracked.vstring('omtfEmulatorPhase2', 'omtfParameter')
    )
    #process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)
if not verbose:
    process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
    process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),
                                         #SkipEvent = cms.untracked.vstring('ProductNotFound')
                                     )
"""
#######################################################################################3
# Input source
process.source = cms.Source("PoolSource",

                            fileNames = cms.untracked.vstring(                                                                

                                #'root:///eos/user/a/almuhamm/ZMu_Test/simPrivateProduction/XTo2LLPTo4Mu_cTau5m_50Files_SmallStatistics.root'
                                'root://cms-xrd-global.cern.ch//store/mc/Phase2Spring23DIGIRECOMiniAOD/MinBias_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU140_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v2/2560000/00ce3255-aa8a-465b-883e-d61154233a82.root'

),
                            secondaryFileNames = cms.untracked.vstring(),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring()  
)

#prefixPath = '/eos/cms/store/user/eyigitba/dispDiMu/crabOut/CRAB_PrivateMC/HTo2LongLivedTo2mu2jets_MH-1000_MFF-150_CTau-1000mm_TuneCP5_13p6TeV_pythia8/231105_154703/0000'
#prefixPath  = '/eos/cms/store/user/eyigitba/dispDiMu/crabOut/CRAB_PrivateMC/HTo2LongLivedTo2mu2jets_MH-1000_MFF-350_CTau-3500mm_TuneCP5_13p6TeV_pythia8/*/*'
#prefixPath  =  '/eos/cms/store/user/eyigitba/dispDiMu/crabOut/CRAB_PrivateMC/*/*/*'
#prefixPath = '/eos/user/a/akalinow/Data/SingleMu/13_1_0_12_02_2024/*/*/*/*'
#prefixPath = '/eos/user/a/akalinow/Data/SingleMu/13_1_0_13_02_2024/*/*/*/*'
#prefixPath1 ='/eos/user/a/akalinow/Data/SingleMu/13_1_0_03_01_2024/*/*/*/*'
#prefixPath1 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/13_1_0_03_04_2024/SingleMu_ch0_OneOverPt_Run2029_13_1_0_03_04_2024/13_1_0_03_04_2024/240403_083618/0000'
#prefixPath2 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/13_1_0_03_04_2024/SingleMu_ch2_OneOverPt_Run2029_13_1_0_03_04_2024/13_1_0_03_04_2024/240403_083731/0000'
#prefixPath1 ='/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/MinBias_TuneCP5_14TeV-pythia8/crab_MinBias_TuneCP5_14TeV-pythia8_Phase2Spring23DIGIRECOMiniAOD-PU200/240304_104359/0000'
prefixPath1 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/MinBias_TuneCP5_14TeV-pythia8/crab_MinBias_TuneCP5_14TeV-pythia8_Phase2Spring23DIGIRECOMiniAOD-PU140/240227_004426/0000'
#prefixPath1 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/13_1_0_11_03_2024/*/*/*/*'
#prefixPath1 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/13_1_0_07_03_2024/*/*/*/*'
#prefixPath1 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/Displaced_cTau5m_XTo2LLTo4Mu_condPhase2_GP2024/13_1_0_23_03_2024_XTo2LLPTo4Mu/240323_145610/0000'
fileList1 = glob.glob(prefixPath1 + '/*.root')
#fileList2 = glob.glob(prefixPath2 + '/*.root')
#fileList = fileList1 + fileList2
random.shuffle(fileList1)
fileList_mix = ['file:' + aFile for aFile in fileList1]
process.source.fileNames = fileList_mix


#########################################################################################################################################################################


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)


from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_mc_FULL','')
#process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun3_2023_realistic_v10','')
process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun4_realistic_v7','')

#####OMTF phaseII EMulator
##

#Calibrate Digi
process.load("L1Trigger.DTTriggerPhase2.CalibratedDigis_cfi")
process.CalibratedDigis.dtDigiTag = "simMuonDTDigis"
process.CalibratedDigis.scenario = 0

#DTTriggerPhase2
process.load("L1Trigger.DTTriggerPhase2.dtTriggerPhase2PrimitiveDigis_cfi")
process.dtTriggerPhase2PrimitiveDigis.digiTag = cms.InputTag("CalibratedDigis")
process.dtTriggerPhase2PrimitiveDigis.debug = False
process.dtTriggerPhase2PrimitiveDigis.dump = False
process.dtTriggerPhase2PrimitiveDigis.scenario = 0




#####OMTF PhaseI Emulator
import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_extrapolSimple_cfi.simOmtfDigis.clone()

#process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2SimplifiedFP_t17_classProb17_recalib2_minDP0_v3.xml")
#process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2SimplifiedFP_t17_classProb17_recalib2.xml")
#process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2FullAlgo_t16_classProb17_recalib2.xml")


#####OMTF phaseII EMulator


import L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_extrapol_cfi
process.omtfEmulatorPhase2=L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_extrapol_cfi.simOmtfPhase2Digis.clone()
process.omtfEmulatorPhase2.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2DTQualAndEtaFixedP_ValueP1Scale_t20_v1_SingleMu_iPt_and_OneOverPt_classProb17_recalib2_minDP0.xml")
process.omtfEmulatorPhase2.dtRefHitMinQuality =  cms.int32(4)
process.omtfEmulatorPhase2.rpcMaxClusterSize = cms.int32(3)
process.omtfEmulatorPhase2.rpcMaxClusterCnt = cms.int32(2)
process.omtfEmulatorPhase2.rpcDropAllClustersIfMoreThanMax = cms.bool(True)
process.omtfEmulatorPhase2.goldenPatternResultFinalizeFunction = cms.int32(10)
process.omtfEmulatorPhase2.noHitValueInPdf = cms.bool(True)
process.omtfEmulatorPhase2.minDtPhiQuality = cms.int32(2)
process.omtfEmulatorPhase2.minDtPhiBQuality = cms.int32(4)
process.omtfEmulatorPhase2.lctCentralBx = cms.int32(8)
process.omtfEmulatorPhase2.bxMin = cms.int32(-3)
process.omtfEmulatorPhase2.bxMax = cms.int32(4)
process.omtfEmulatorPhase2.srcDTPhPhase2 = cms.InputTag("dtTriggerPhase2PrimitiveDigis")
process.omtfEmulatorPhase2.srcDTThPhase2 = cms.InputTag("dtTriggerPhase2PrimitiveDigis")
process.omtfEmulatorPhase2.dropDTPrimitives = cms.bool(True)
process.omtfEmulatorPhase2.usePhase2DTPrimitives = cms.bool(True)
process.omtfEmulatorPhase2.dumpResultToXML = cms.bool(True)
#process.omtfEmulatorPhase2.XMLDumpFileName = cms.string("TestEvents_1400pre3_ctau5m_phase2IntegrationBranch_pats24cmsdata.xml"),
#process.omtfEmulatorPhase2.dumpDetailedResultToXML = cms.bool(True)

if(runDebug == "DEBUG") :
    process.omtfEmulatorPhase2.eventCaptureDebug = cms.bool(True)
else :
    process.omtfEmulatorPhase2.eventCaptureDebug = cms.bool(False)

import L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff
process.omtfParameter=L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff.omtfParams.clone()
#process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0009.xml")#phase 1
process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0209.xml") #phase 2

####OMTF Analyzer
process.load('UserCode.OmtfAnalysis.omtfTree_cfi')
process.muAnalyzerPath = cms.Path(process.omtfTree)


#process.raw2digi_step = cms.Sequence(process.muonRPCDigis+process.muonCSCDigis+process.bmtfDigis+process.emtfStage2Digis+process.twinMuxStage2Digis+process.gmtStage2Digis+process.caloStage2Digis)
#process.omtf_step = cms.Sequence(process.omtfStage2Digis+process.omtfEmulator+process.omtfEmulatorPhase2)
#process.omtf_step = cms.Sequence(process.omtfEmulator+process.omtfEmulatorPhase2)
process.omtf_step = cms.Sequence(process.omtfEmulatorPhase2)

#process.ntup = cms.Sequence((process.muAnalyzerPath)*recomuon)
#process.ntup = cms.Sequence(process.recomuon)


# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)

process.DTPhase2DigisPath = cms.Path(process.omtf_step)
#process.DTPhase2DigisPath = cms.Path(process.CalibratedDigis * process.dtTriggerPhase2PrimitiveDigis * process.omtf_step) #Reprocess the DTTP,Repeat Exercise for two set, with/without


# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step, process.muAnalyzerPath, process.endjob_step)     #RAW2DIGI-notworking me right now, beamspot?
process.schedule = cms.Schedule(process.DTPhase2DigisPath, process.muAnalyzerPath, process.endjob_step)   

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

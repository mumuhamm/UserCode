# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms
process = cms.Process("L1TMuonEmulation")
from pathlib import Path
import os
import random
import sys
import re
from os import listdir
from os.path import isfile, join
import glob
import copy
import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")

dumpHitsFileName = 'OMTFHits_patsminDP0_v3_MuonMatcher_smoothStdDev_hwToL0X0209' 
version = 'CMSSW141XPre0_PhII_Extrapolation_cTau5m_XTo2LLTo4Mu_' + timestamp 

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
       omtfEventPrint = cms.untracked.PSet(    
                         filename  = cms.untracked.string('log_' + version),
                         extension = cms.untracked.string('.txt'),                
                         threshold = cms.untracked.string('DEBUG'),
                         default = cms.untracked.PSet( limit = cms.untracked.int32(10000) ), 
                         #INFO   =  cms.untracked.int32(0),
                         #DEBUG   = cms.untracked.int32(0),
                         l1tOmtfEventPrint = cms.untracked.PSet( limit = cms.untracked.int32(1000000000) ),
                         OMTFReconstruction = cms.untracked.PSet( limit = cms.untracked.int32(1000000000) )
                       ),
       debugModules = cms.untracked.vstring('simOmtfDigis') 
    )
  
    process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
if not verbose:
    process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(50000)
    process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False), 
                                         #SkipEvent = cms.untracked.vstring('ProductNotFound') 
                                     )

"""
# import of standard configurations

#process.load('Configuration.Geometry.GeometryExtended2026D88Reco_cff')
#process.load('Configuration.Geometry.GeometryDD4hepExtendedRun4D107Reco_cff.py')
#process.load('Configuration.Geometry.GeometryExtended2026D88_cff')
process.load('Configuration.Geometry.GeometryExtended2026D95Reco_cff')


from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun3_2023_realistic_v10', '') 
process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun4_realistic_v5', '') 

# input files (up to 255 files accepted)
process.source = cms.Source('PoolSource',
fileNames = cms.untracked.vstring(

    #                              'root:///eos/user/a/almuhamm/ZMu_Test/XTo2LLPTo4Mu_Sample/SingleMuon_XTo2LLPTo4Mu.root'    
                                  'root:///eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/13_1_0_03_04_2024/SingleMu_ch0_OneOverPt_Run2029_13_1_0_03_04_2024/13_1_0_03_04_2024/240403_083618/0000/SingleMu_OneOverPt_1_100_m_443.root'
                                  #'file:/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch0_iPt1_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_150000/0000/DisplacedSingleMu_iPt_1_m_359.root'
                                   #'file:/scratch_cmsse/akalinow/CMS/Data/SingleMu/12_5_2_p1_15_02_2023/SingleMu_ch2_iPt0_12_5_2_p1_15_02_2023/12_5_2_p1_15_02_2023/230216_100239/0000/SingleMu_iPt_0_p_47.root',

),
skipEvents =  cms.untracked.uint32(0),       
)

#samplefor Ch0 - pTbin(GeV) 0-10 10-100 100-1000
prefixPath1 = '/eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/PrivateProductionForOMTFStudy/Displaced_cTau5m_XTo2LLTo4Mu_condPhase2_GP2024/13_1_0_23_03_2024_XTo2LLPTo4Mu/240323_145610/0000'
fileList1 = glob.glob(prefixPath1 + '/*.root')
#fileList2 = glob.glob(prefixPath2 + '/*.root')
#fileList = fileList1 + fileList2
random.shuffle(fileList1)
fileList_mix = ['file:' + aFile for aFile in fileList1]
process.source.fileNames = fileList_mix
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(200000))

####Event Setup Producer
"""
process.load('L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff')
process.esProd = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(
      cms.PSet(record = cms.string('L1TMuonOverlapParamsRcd'),
                 data = cms.vstring('L1TMuonOverlapParams'))
                   ),
   verbose = cms.untracked.bool(False)
)

"""      


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

import L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff
process.omtfParameter=L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff.omtfParams.clone()
process.omtfParameter.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0209.xml")






import L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_cfi
process.omtfEmulatorPhase2 = L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_cfi.simOmtfPhase2Digis.clone()


#####OMTF phaseII EMulator
#import L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_extrapol_cfi
#process.omtfEmulatorPhase2=L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_extrapol_cfi.simOmtfPhase2Digis.clone()

process.omtfEmulatorPhase2.srcDTPh = cms.InputTag('simDtTriggerPrimitiveDigis')
process.omtfEmulatorPhase2.srcDTTh = cms.InputTag('simDtTriggerPrimitiveDigis')
process.omtfEmulatorPhase2.srcCSC = cms.InputTag('simCscTriggerPrimitiveDigis')
process.omtfEmulatorPhase2.srcRPC = cms.InputTag('simMuonRPCDigis')
process.omtfEmulatorPhase2.dumpHitsToROOT = cms.bool(True)
process.omtfEmulatorPhase2.candidateSimMuonMatcher = cms.bool(True)
process.omtfEmulatorPhase2.simTracksTag = cms.InputTag('g4SimHits')
process.omtfEmulatorPhase2.simVertexesTag = cms.InputTag('g4SimHits')
process.omtfEmulatorPhase2.muonMatcherFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/muonMatcherHists_100files_smoothStdDev_withOvf.root")
process.omtfEmulatorPhase2.sorterType = cms.string("byLLH")
process.omtfEmulatorPhase2.ghostBusterType = cms.string("byRefLayer")
process.omtfEmulatorPhase2.patternXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2DTQualAndEtaFixedP_ValueP1Scale_t20_v1_SingleMu_iPt_and_OneOverPt_classProb17_recalib2_minDP0.xml")
process.omtfEmulatorPhase2.dtRefHitMinQuality =  cms.int32(4)
process.omtfEmulatorPhase2.usePhiBExtrapolationFromMB1 = cms.bool(True)
process.omtfEmulatorPhase2.usePhiBExtrapolationFromMB2 = cms.bool(True)
process.omtfEmulatorPhase2.rpcMaxClusterSize = cms.int32(3)
process.omtfEmulatorPhase2.rpcMaxClusterCnt = cms.int32(2)
process.omtfEmulatorPhase2.rpcDropAllClustersIfMoreThanMax = cms.bool(True)
process.omtfEmulatorPhase2.goldenPatternResultFinalizeFunction = cms.int32(10)
process.omtfEmulatorPhase2.noHitValueInPdf = cms.bool(True)
process.omtfEmulatorPhase2.minDtPhiQuality = cms.int32(2)
process.omtfEmulatorPhase2.minDtPhiBQuality = cms.int32(4)
process.omtfEmulatorPhase2.lctCentralBx = cms.int32(8)
process.omtfEmulatorPhase2.lctCentralBx = cms.int32(8);
process.omtfEmulatorPhase2.bxMin = cms.int32(-3)
process.omtfEmulatorPhase2.bxMax = cms.int32(4)
process.omtfEmulatorPhase2.srcDTPhPhase2 = cms.InputTag("dtTriggerPhase2PrimitiveDigis")
process.omtfEmulatorPhase2.srcDTThPhase2 = cms.InputTag("dtTriggerPhase2PrimitiveDigis")
process.omtfEmulatorPhase2.dropDTPrimitives = cms.bool(True)
process.omtfEmulatorPhase2.usePhase2DTPrimitives = cms.bool(True)

#=============================================================================================

process.TFileService = cms.Service("TFileService", 
        fileName = cms.string(
            #"file:///eos/user/a/almuhamm/OMTF_UW/newTFRecord/SingleMu_" + version + ".root")
            "file:///eos/cms/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/OMTFFlatNtuples/SingleMu_" + version + ".root") 
            #"file:///eos/user/a/almuhamm/OMTF_UW/AprilMay_2024_PIIExtraPolDTReprocessed_Ntuples_ForTFRecord/SingleMu_" + version + ".root") 
                                    )
      

#=============================================================================================
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")

process.dumpED = cms.EDAnalyzer("EventContentAnalyzer")
process.dumpES = cms.EDAnalyzer("PrintEventSetupContent")

process.L1TMuonSeq = cms.Sequence( #process.esProd          
                                   process.omtfEmulatorPhase2 
                                   #+ process.dumpED
                                   #+ process.dumpES
)
#process.DTPhase2DigisPath = cms.Path(process.L1TMuonSeq)
process.DTPhase2DigisPath = cms.Path(process.CalibratedDigis * process.dtTriggerPhase2PrimitiveDigis * process.L1TMuonSeq) 
process.schedule = cms.Schedule(process.DTPhase2DigisPath)


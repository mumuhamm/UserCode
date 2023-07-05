import FWCore.ParameterSet.Config as cms
import os
import sys
import subprocess

#from Configuration.StandardSequences.Eras import eras
#process = cms.Process('OmtfTree',eras.Run2_2016)

process = cms.Process('OmtfTree')

#
# For processing single files insert lines with 'file:/PATH/FILE.root'
# alernatively one can use 'root://xrootd.unl.edu//store/express/Run2015A.....root'
# or                       '/store/express/Run2015A/ExpressPhysics/FEVT/...root'
# (there is 255 file limit though). Can be empty for crab.
#

dataDir='/afs/cern.ch/work/k/konec/data/runs/'
#dataDir='/eos/cms/store/express/Run2022D/ExpressPhysics/FEVT/Express-v1/000/357/815/00000/'
#dataDir='/eos/cms/store/express/Run2022E/ExpressPhysics/FEVT/Express-v1/000/359/691/00000/'
#dataDir='/eos/cms/store/express/Run2022E/ExpressPhysics/FEVT/Express-v1/000/359/686/00000/'
#dataDir='/eos/cms/store/express/Run2022E/ExpressPhysics/FEVT/Express-v1/000/359/685/00000/'
#dataDir='/eos/cms/store/express/Run2022F/ExpressPhysics/FEVT/Express-v1/000/360/459/00000/'
#dataDir='/eos/cms/store/express/Run2022G/ExpressPhysics/FEVT/Express-v1/000/362/728/00000/'
#lsCommand='ls -1 '+dataDir+'|grep root'
lsCommand='ls -1 '+dataDir+'|grep JetMET | grep 362437 |grep root'
#lsCommand='ls -1 '+dataDir+'|grep run362728_Muon'

print ('command: ',lsCommand)
lsOutput= subprocess.Popen(lsCommand, stdout=subprocess.PIPE, shell=True, text=True).communicate()[0]
files=[]
for f in lsOutput.split():
  files.append('file:'+dataDir+f)
print ("Number of files in direcotry:",dataDir," ---> ", len(files))

process.source = cms.Source("PoolSource", 
fileNames = cms.untracked.vstring(
#'file:/afs/cern.ch/work/k/konec/data/runs/run279931-Express-2000_82DB28E0-7171-E611-A67B-FA163EE0E3A6.root',
#'root://cms-xrd-global.cern.ch//store/express/Run2017B/ExpressPhysics/FEVT/Express-v2/000/298/853/00000/08861D5E-C966-E711-9E99-02163E019DA2.root'
#'/store/data/Run2017F/SingleMuon/RAW-RECO/ZMu-17Nov2017-v1/70002/BEB00326-8EE0-E711-BCEE-FA163E8B70D3.root',
#'root://eoscms.cern.ch//eos/cms/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/321/887/00000/6C133D73-73AE-E811-8244-FA163E6C4BEA.root'
# 'file:/eos/cms/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/ff2a2110-2a06-4a7f-8e51-6977113e6e68.root',
# 'file:/eos/cms/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/417/00000/01946fa6-080a-42e1-af66-b40b0621e8e5.root',
# 'file:/eos/cms/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/417/00000/06079f98-e0ed-4810-9490-1f7d0d5a17bb.root',
# 'file:/eos/cms/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/417/00000/069157b0-dbaa-4546-bdac-072a85fee2ff.root',
#  'file:/eos/cms/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/417/00000/0773fa06-e0e6-4da3-a12f-7f02e809a2ef.root',
# 'file:/afs/cern.ch/work/k/konec/data/runs/run324201_SingleMuon_DE15789B-9E54-7F41-8C6B-E2442CB23F52.root',
#  'file:/afs/cern.ch/work/k/konec/data/runs/run321124_JetHT_9E9321CC-B19E-E811-BF42-FA163E4EAC94.root',
#  'file:/afs/cern.ch/work/k/konec/data/runs/run321140_JetHT_00CAF0AF-5B9F-E811-9E6B-FA163EEA3181.root',
#  'file:/afs/cern.ch/work/k/konec/data/runs/run322348_JetHT_A8C88C19-40B4-E811-9F14-02163E019EAF.root',
# 'file:/eos/cms/store/express/Run2022D/ExpressPhysics/FEVT/Express-v1/000/357/815/00000/ffe8b95d-25cb-45cd-9f45-b96d8e18ed4f.root',
#  '/store/data/Run2022G/Muon/RAW-RECO/ZMu-PromptReco-v1/000/362/728/00000/02c66efb-5541-4c9d-b2ac-952ce4ebdcd7.root',
#  'file:/afs/cern.ch/work/k/konec/data/runs/run362728_Muon_02c66efb-5541-4c9d-b2ac-952ce4ebdcd7.root',
#  '/store/data/Run2022G/JetMET/RAW-RECO/JetHTJetPlusHOFilter-PromptReco-v1/000/362/437/00000/7fa78eec-f7bf-47be-bbce-9264b8d5205e.root',
#  '/store/data/Run2022G/JetMET/RAW-RECO/JetHTJetPlusHOFilter-PromptReco-v1/000/362/437/00000/cc10cdfb-6a8c-455d-a441-960522112238.root',
#   '/store/data/Run2022G/Muon/MINIAOD/PromptReco-v1/000/362/760/00000/01cd8e14-f3a9-412e-8548-3f17ea13040b.root',
#  '/store/data/Run2022G/JetMET/MINIAOD/PromptReco-v1/000/362/760/00000/110404fa-abee-41ad-9ff3-25756fa54d58.root',
 '/store/data/Run2023D/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/369/870/00000/42f402f5-c1ce-433f-8d92-7af6cb2004d5.root',
 '/store/data/Run2023D/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/369/956/00000/50d95203-d831-4a5f-8e47-f9147cfc0e7f.root',
  ),
#skipEvents =  cms.untracked.uint32(764)
#skipEvents =  cms.untracked.uint32(19177)
#skipEvents =  cms.untracked.uint32(19177+1117)
#skipEvents =  cms.untracked.uint32(19177+1332)
)
#process.source.fileNames = files
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(101) )

#
# import of standard configurations
#
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
#process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

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

#
# set proper GlobalTag
#
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag.globaltag = '123X_dataRun3_Express_v5'
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')

#
# message logger
#
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.enableStatistics = False
process.MessageLogger.cout.enable =False 
#process.MessageLogger.cerr.threshold = "DEBUG"
#process.MessageLogger.debugModules.append('muonRPCDigis')
#process.MessageLogger.debugModules.append('omtfStage2Digis')
process.MessageLogger.suppressWarning  = cms.untracked.vstring('*')

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

#process.omtfStage2Raw = cms.EDProducer("OmtfPacker",
#  rpcInputLabel = cms.InputTag('omtfStage2Digis'),
#  cscInputLabel = cms.InputTag('omtfStage2Digis'),
#  dtPhInputLabel = cms.InputTag('omtfStage2Digis'),
#  dtThInputLabel = cms.InputTag('omtfStage2Digis'),
#)

#process.omtfStage2Digis2 = cms.EDProducer("OmtfUnpacker",
#  inputLabel = cms.InputTag('omtfStage2Raw'),
#  useRpcConnectionFile = cms.bool(True),
#  rpcConnectionFile = cms.string("CondTools/RPC/data/RPCOMTFLinkMapInput.txt"),
#  outputTag = cms.string("OmtfUnpacker2"),
#)

#
###OMTF emulator configuration
#
#OMTF ESProducer. Fills CondFormats from XML files.
#process.omtfParamsSource = cms.ESSource( "EmptyESSource",
#     recordName = cms.string('L1TMuonOverlapParamsRcd'),
#    iovIsRunNotTime = cms.bool(True),
#    firstValid = cms.vuint32(1)
#)
#process.omtfParams = cms.ESProducer( "L1TMuonOverlapParamsESProducer",
#     patternsXMLFiles = cms.VPSet( cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x0003.xml")),),
#     configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0004.xml"),
#)

#process.load('L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff')
#process.omtfParams.configXMLFile =  cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0008.xml")
#process.omtfParams.patternsXMLFiles = cms.VPSet( cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x00012_oldSample_3_30Files_grouped1_classProb17_recalib2.xml")))

import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi.simOmtfDigis.clone() 
#process.omtfEmulator.srcDTPh = cms.InputTag('simDtTriggerPrimitiveDigis'),
#process.omtfEmulator.srcDTTh = cms.InputTag('simDtTriggerPrimitiveDigis'),
#process.omtfEmulator.srcCSC = cms.InputTag('simCscTriggerPrimitiveDigis','MPCSORTED'),
#process.omtfEmulator.srcRPC = cms.InputTag('simMuonRPCDigis'),
process.omtfEmulator.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcCSC = cms.InputTag('omtfStage2Digis')
#process.omtfEmulator.srcCSC = cms.InputTag('emtfStage2Digis')
process.omtfEmulator.srcRPC = cms.InputTag('omtfStage2Digis')
#process.omtfEmulator.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x00012_oldSample_3_30Files_grouped1_classProb17_recalib2.xml")
#
process.omtfEmulator.dumpResultToXML = cms.bool(False)
#process.omtfEmulator.dumpResultToROOT = cms.bool(False)
#process.omtfEmulator.eventCaptureDebug = cms.bool(False)
#
#process.omtfEmulator.sorterType = cms.string("byLLH")
#process.omtfEmulator.ghostBusterType = cms.string("GhostBusterPreferRefDt")
process.omtfEmulator.minDtPhiQuality = cms.int32(2)
process.omtfEmulator.minDtPhiBQuality = cms.int32(4)
#process.omtfEmulator.rpcMaxClusterSize = cms.int32(3)
#process.omtfEmulator.rpcMaxClusterCnt = cms.int32(2)
#process.omtfEmulator.rpcDropAllClustersIfMoreThanMax = cms.bool(True)
#process.omtfEmulator.goldenPatternResultFinalizeFunction = cms.int32(9) # 2018: 0, 100g:9
#process.omtfEmulator.noHitValueInPdf = cms.bool(True) #2018: False, 100g: True
process.omtfEmulator.lctCentralBx = cms.int32(8);
process.omtfEmulator.bxMin = cms.int32(-3)
process.omtfEmulator.bxMax = cms.int32(4)


#
# reemulate GMT, with changed OMTF
#
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

process.schedule = cms.Schedule(process.raw2digi_step, process.omtf_step, process.endjob_step)

#
# OMTF tree 
#
process.omtfTree = cms.EDAnalyzer("OmtfTreeMaker",
  histoFileName = cms.string("omtfHelper.root"),
  treeFileName = cms.string("omtfTree.root"),

  menuInspector = cms.PSet( 
#    namesCheckHltMuMatch = cms.vstring(
#      "HLT_IsoMu22_v","HLT_IsoTkMu22_v","HLT_Mu50_v","HLT_TkMu50_v","HLT_Mu45_eta2p1_v",
#      "HLT_IsoMu22_eta2p1_v", "HLT_IsoMu24_v", "HLT_IsoMu27_v",
#      "HLT_IsoTkMu22_eta2p1_v", "HLT_IsoTkMu24_v", "HLT_IsoTkMu27_v",
#      "HLT_Mu55_v", "HLT_IsoMu24_eta2p1_v", "HLT_IsoTkMu24_eta2p1_v"
#    ),
    namesCheckHltMuMatch = cms.vstring(
       "HLT_IsoMu24_v","HLT_IsoMu24_eta2p1_v","HLT_Mu50_v"
     ),
  ),

   linkSynchroGrabber = cms.PSet(
     rawSynchroTag = cms.InputTag("muonRPCDigis"),
     writeHistograms = cms.untracked.bool(True),
     deltaR_MuonToDetUnit_cutoff = cms.double(0.3),
     checkInside = cms.bool(True),
     linkMonitorPSet = cms.PSet(
       useFirstHitOnly = cms.untracked.bool(True),
       dumpDelays = cms.untracked.bool(True) # set to True for LB delay plots
     ),
     synchroSelector = cms.PSet(
       checkRpcDetMatching_minPropagationQuality = cms.int32(0),
       checkRpcDetMatching_matchingScaleValue = cms.double(3),
       checkRpcDetMatching_matchingScaleAuto  = cms.bool(True),
       checkUniqueRecHitMatching_maxPull = cms.double(2.),
       checkUniqueRecHitMatching_maxDist = cms.double(5.)
     )
   ),
  
  l1ObjMaker = cms.PSet(
    omtfEmulSrc = cms.InputTag('omtfEmulator','OMTF'),
    omtfDataSrc = cms.InputTag('omtfStage2Digis'),
    emtfDataSrc = cms.InputTag('emtfStage2Digis'),
    bmtfDataSrc = cms.InputTag('bmtfDigis','BMTF'),
#   omtfDataSrc = cms.InputTag('gmtStage2Digis','OMTF'),
#   emtfDataSrc = cms.InputTag('gmtStage2Digis','EMTF'),
#   bmtfDataSrc = cms.InputTag('gmtStage2Digis','BMTF'),
    gmtDataSrc = cms.InputTag('gmtStage2Digis','Muon'),
    gmtEmulSrc = cms.InputTag('emulGmtStage2Digis',''),
  ),

  closestTrackFinder = cms.PSet(
    trackColl = cms.InputTag("generalTracks"),
    warnNoColl = cms.untracked.bool(True)
  ),

  onlyBestMuEvents = cms.bool(True),
  bestMuonFinder = cms.PSet(
    muonColl = cms.InputTag("muons"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    warnNoColl = cms.untracked.bool(True),
    requireInnerTrack = cms.bool(True),
    requireOuterTrack = cms.bool(False),
    requireGlobalTrack = cms.bool(False),
    requireLoose       = cms.bool(True),
    minPt = cms.double(3.),
    maxTIP = cms.double(0.2),
    maxAbsEta = cms.double(2.4),
    minNumberTrackerHits = cms.int32(6),
    minNumberRpcHits = cms.int32(0),
    minNumberDtCscHits = cms.int32(0),
    minNumberOfMatchedStations = cms.int32(0),
    cutTkIsoRel = cms.double(0.1),
    cutPFIsoRel = cms.double(0.15),
    deltaPhiUnique = cms.double(1.0),
    deltaEtaUnique = cms.double(0.5),
    minPtUnique = cms.double(3.0),
    looseUnique = cms.bool(True)
  ),

  synchroCheck = cms.PSet(
    srcDT  = cms.InputTag('omtfStage2Digis'),
    srcCSC = cms.InputTag('omtfStage2Digis'),
    srcRPC = cms.InputTag('omtfStage2Digis')
  ),
)

#
# refit Muon
#
process.load("TrackingTools.RecoGeometry.RecoGeometries_cff")
process.load("TrackingTools.TrackRefitter.TracksToTrajectories_cff")
process.load("TrackingTools.TrackRefitter.globalMuonTrajectories_cff")
#import TrackingTools.TrackRefitter.globalMuonTrajectories_cff
#process.refittedMuons = TrackingTools.TrackRefitter.globalMuonTrajectories_cff.globalMuons.clone()
#process.OmtfTree = cms.Path(process.refittedMuons*process.omtfTree)

process.OmtfTree = cms.Path(process.omtfTree)
process.schedule.append(process.OmtfTree)

#print process.dumpPython();
#print process.schedule

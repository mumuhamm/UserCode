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
                                'root://cms-xrd-global.cern.ch//store/data/Run2023B/Muon1/RAW-RECO/ZMu-PromptReco-v1/000/366/469/00000/70d9986d-9df0-46c8-b6be-9d96a8113ccc.root'
  

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
process.recomuon = cms.EDFilter("MuonRefSelector",
                                        src = cms.InputTag("muons"),
                                        cut = cms.string('pt > 0.5 && abs(eta) > 0.83 && abs(eta) < 1.23  && isGlobalMuon == 1' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1)
                                        )


####OMTF Emulator
import L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi
process.omtfEmulator=L1Trigger.L1TMuonOverlapPhase1.simOmtfDigis_cfi.simOmtfDigis.clone() 
process.omtfEmulator.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcCSC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.srcRPC = cms.InputTag('omtfStage2Digis')
process.omtfEmulator.lctCentralBx = cms.int32(8);
process.omtfEmulator.bxMin = cms.int32(-3)
process.omtfEmulator.bxMax = cms.int32(4)

#####OMTF phaseII EMulator
import L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_cfi
process.omtfEmulatorPhase2=L1Trigger.L1TMuonOverlapPhase2.simOmtfPhase2Digis_cfi.simOmtfPhase2Digis.clone()
process.omtfEmulatorPhase2.srcDTPh = cms.InputTag('omtfStage2Digis')
process.omtfEmulatorPhase2.srcDTTh = cms.InputTag('omtfStage2Digis')
process.omtfEmulatorPhase2.srcCSC = cms.InputTag('omtfStage2Digis')
process.omtfEmulatorPhase2.srcRPC = cms.InputTag('omtfStage2Digis')
process.omtfEmulatorPhase2.lctCentralBx = cms.int32(8);
process.omtfEmulatorPhase2.bxMin = cms.int32(-3)
process.omtfEmulatorPhase2.bxMax = cms.int32(4)




process.raw2digi_step = cms.Path(process.muonRPCDigis+process.muonCSCDigis+process.bmtfDigis+process.emtfStage2Digis+process.twinMuxStage2Digis+process.gmtStage2Digis+process.caloStage2Digis)
process.omtf_step = cms.Path(process.omtfStage2Digis+process.omtfEmulator+process.omtfEmulatorPhase2)

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
process.schedule = cms.Schedule(process.muAnalyzerPath, process.endjob_step)
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

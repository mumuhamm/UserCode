# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --conditions 123X_mcRun4_realistic_v3 -n 2 --era Phase2C9 --eventcontent FEVTDEBUGHLT --runUnscheduled file:/eos/cms/store/relval/CMSSW_11_0_0/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v2/10000/01054EE2-1B51-C449-91A2-5202A60D16A3.root -s RAW2DIGI,L1TrackTrigger,L1 --datatier FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,L1Trigger/Configuration/customisePhase2TTNoMC.customisePhase2TTNoMC,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT --geometry Extended2026D49 --fileout file:/tmp/step1_Reprocess_TrackTrigger_L1.root --no_exec --nThreads 8 --python step1_L1_ProdLike.py --processName=L1REPR
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('L1REPROCESS',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:/scratch/Magisterka/Test_data/PhaseIISpring22DRMiniAOD_DYToLL_M-10To50_noPU_40000_04216b41-07a8-4ec9-a1c3-a24cda929b74_2000Ev.root'),
                            #fileNames = cms.untracked.vstring('file:FEVTSIM.root'),
                            #fileNames = cms.untracked.vstring('file:/scratch_hdd/akalinow/CMS/OMTF/PhaseII/HSCP_Production/Tasks_Run2029/crab_HSCPstop_M_800_TuneCP5_13TeV_pythia8_Run2029_test_20_10_2022/results/RECOSIM_1.root',
                            #                                  'file:/scratch_hdd/akalinow/CMS/OMTF/PhaseII/HSCP_Production/Tasks_Run2029/crab_HSCPstop_M_800_TuneCP5_13TeV_pythia8_Run2029_test_20_10_2022/results/RECOSIM_2.root'),
                            secondaryFileNames = cms.untracked.vstring(),
                                      dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
          inputCommands=cms.untracked.vstring()  
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Output definition
process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('FEVTDEBUGHLT'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:TTTrigger_reprocess_L1.root'),
    outputCommands = cms.untracked.vstring(
        "drop *_*_*_*",
        "keep *_gmtMuons_*_*",
        "keep *_gmtStubs_*_*",
        "keep *_genParticles_*_*",
        "keep *_TTTracksFromTrackletEmulation_Level1TTTracks_*",
        "keep *_L1TkMuons_*_*"
    ),
    splitLevel = cms.untracked.int32(0)
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '123X_mcRun4_realistic_v3', '')

##
#Calibrate Digi
process.load("L1Trigger.DTTriggerPhase2.CalibratedDigis_cfi")
process.CalibratedDigis.dtDigiTag = "simMuonDTDigis" 
process.CalibratedDigis.scenario = 0

#DTTriggerPhase2
process.load("L1Trigger.DTTriggerPhase2.dtTriggerPhase2PrimitiveDigis_cfi")
process.dtTriggerPhase2PrimitiveDigis.debug = False
process.dtTriggerPhase2PrimitiveDigis.dump = False
process.dtTriggerPhase2PrimitiveDigis.scenario = 0

process.load("L1Trigger.Phase2L1GMT.gmt_cff")
process.gmtMuons.trackMatching.verbose=0
process.gmtMuons.verbose=0
process.gmtMuons.trackConverter.verbose=0
process.gmtMuons.isolation.IsodumpForHLS = 0

process.gmtMuons.trackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth")
process.gmtMuons.mcTruthTrackInputTag = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks")
process.gmtMuons.dumpToRoot = cms.bool(False)
process.gmtMuons.dumpToXml = cms.bool(False)

########### Analyzer from MK
####OMTF Analyzer
process.load('omtfTree_cfi')
############################
########### Analyzer from KB
analysisType = "efficiency" # or rate
verbose = True
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('muCorrelatorTTAnalysis.root'),
                                   closeFileFast = cms.untracked.bool(True)
)
process.muCorrelatorAnalyzer= cms.EDAnalyzer("MuCorrelatorAnalyzer", 
                                 outRootFile = cms.string("muCorrelatorTTAnalysis.root"),
                                 etaCutFrom = cms.double(0.), #OMTF eta range
                                 etaCutTo = cms.double(2.4),
                                          
                                MyProcess = cms.int32(1),
                                             DebugMode = cms.bool(verbose),      # printout lots of debug statements
                                             SaveAllTracks = cms.bool(True),   # save *all* L1 tracks, not just truth matched to primary particle
                                             SaveStubs = cms.bool(False),      # save some info for *all* stubs
                                             LooseMatch = cms.bool(True),     # turn on to use "loose" MC truth association
                                             L1Tk_minNStub = cms.int32(4),     # L1 tracks with >= 4 stubs
                                             TP_minNStub = cms.int32(4),       # require TP to have >= X number of stubs associated with it
                                             TP_minNStubLayer = cms.int32(4),  # require TP to have stubs in >= X layers/disks
                                             TP_minPt = cms.double(1.0),       # only save TPs with pt > X GeV
                                             TP_maxEta = cms.double(2.4),      # only save TPs with |eta| < X
                                             TP_maxZ0 = cms.double(30.0),      # only save TPs with |z0| < X cm
                                             TP_maxRho = cms.double(30.0),     # for efficiency analysis, to not inlude the muons from the far decays 
                                             L1TrackInputTag = cms.InputTag("TTTracksFromTrackletEmulation", "Level1TTTracks") ,               ## TTTrack input
                                             MCTruthTrackInputTag = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks"), ## MCTruth input 
                                             # other input collections
                                             L1StubInputTag = cms.InputTag("TTStubsFromPhase2TrackerDigis","StubAccepted"),
                                             MCTruthClusterInputTag = cms.InputTag("TTClusterAssociatorFromPixelDigis", "ClusterAccepted"),
                                             MCTruthStubInputTag = cms.InputTag("TTStubAssociatorFromPixelDigis", "StubAccepted"),
                                             TrackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                             TrackingVertexInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                             
                                       muCandQualityCut = cms.int32(12),
                                             analysisType = cms.string(analysisType)
                                        )
process.muCorrelatorAnalyzerPath = cms.Path(process.muCorrelatorAnalyzer + process.omtfTree)
############################

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1simulation_step = cms.Path(process.L1TrackTrigger*process.CalibratedDigis*process.dtTriggerPhase2PrimitiveDigis*process.phase2GMT)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1simulation_step,process.muCorrelatorAnalyzerPath,process.endjob_step,process.FEVTDEBUGHLToutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 1
process.options.numberOfStreams = 0
process.options.numberOfConcurrentLuminosityBlocks = 1
process.options.eventSetup.numberOfConcurrentIOVs = 1

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2TTNoMC
from L1Trigger.Configuration.customisePhase2TTNoMC import customisePhase2TTNoMC 

#call to customisation function customisePhase2TTNoMC imported from L1Trigger.Configuration.customisePhase2TTNoMC
process = customisePhase2TTNoMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT
from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT import customisePhase2FEVTDEBUGHLT 

#call to customisation function customisePhase2FEVTDEBUGHLT imported from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT
process = customisePhase2FEVTDEBUGHLT(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

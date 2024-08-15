from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'OMTF_CosmicsEV2AOD'
config.General.requestName = 'OMTF_CosmicsEV2AOD'
config.section_('JobType')
config.JobType.psetName = '/eos/user/a/almuhamm/01.MuonTech/WorkArea_ModifiedPhaseII/CMSSW_14_1_0_pre0/src/UserCode/OmtfAnalysis/test/makeTree_Cosmics_AOD.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['omtfTree.root']
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
#config.Data.inputDataset ='/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/Run3Winter23Reco-RnD_126X_mcRun3_2023_forPU65_v1-v2/GEN-SIM-RECO'
#config.Data.inputDataset ='/JetMET1/Run2023C-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Muon0/Run2024B-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Muon1/Run2024B-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Muon0/Run2024C-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Muon1/Run2024C-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Muon0/Run2024D-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset  ='/Muon1/Run2024D-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Cosmics/Run2024A-CosmicSP-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/Cosmics/Run2024E-CosmicSP-PromptReco-v1/RAW-RECO'
config.Data.inputDataset = '/Cosmics/Run2024E-PromptReco-v2/AOD'
config.Data.ignoreLocality = False
config.Data.unitsPerJob     = 5000
NJOBS = 100  
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits      = 700000
config.Data.splitting       ='EventAwareLumiBased'#'LumiBased'#'FileBased'#EventAwareLumiBased'
#config.Data.runRange        = '357538-357733'
config.JobType.maxMemoryMB = 5000

#config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/Cert_Collisions2022_eraC_355862_357482_Muon.json'
#config.Data.lumiMask = '/eos/user/a/almuhamm/OMTF_UW/json24/Cert_Collisions2024_378981_379866_Muon.json'
config.Data.outLFNDirBase = '/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/crabOut24'#'/store/user/almuhamm/OMTF_UW/crabOut24'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

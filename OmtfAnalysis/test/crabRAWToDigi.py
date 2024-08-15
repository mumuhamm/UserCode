from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True


config.section_("General")
config.General.requestName = 'RAW2DIGI'
config.General.workArea = 'tasks_RAW2DIGI'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'data_run3_2024.py'
config.JobType.allowUndistributedCMSSW = True


config.section_('Data')
#config.Data.inputDataset ='/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/Run3Winter23Reco-RnD_126X_mcRun3_2023_forPU65_v1-v2/GEN-SIM-RECO'
config.Data.inputDataset = '/Muon1/Run2024B-v1/RAW'
#config.Data.inputDataset = '/JetMET/Run2022G-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
config.Data.ignoreLocality = False
config.Data.unitsPerJob     = 5000
NJOBS = 100  
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits      = 700000
config.Data.splitting       ='EventAwareLumiBased'#'LumiBased'#'FileBased'#EventAwareLumiBased'
#config.Data.runRange        = '357538-357733'
config.JobType.maxMemoryMB = 5000
config.Data.publication = False
config.Data.outLFNDirBase = '/store/group/dpg_trigger/comm_trigger/L1Trigger/OMTF/'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'


from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = '/eos/user/a/almuhamm/ZMu_Test/crab_logs/OMTF_DrellYanMLL50MC'
config.General.requestName = 'DrellYanMLL50MC_OMTFL1T'
config.section_('JobType')
config.JobType.psetName = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/makeTree_SingleMuZMu_Displaced.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['omtfTree_mc.root']
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
config.Data.inputDataset = '/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/Run3Winter23Reco-KeepSi_RnD_126X_mcRun3_2023_forPU65_v1-v2/GEN-SIM-RECO'
#config.Data.inputDataset = '/ZToMuMu_M-200To400_TuneCP5_13p6TeV-powheg-pythia8/Run3Winter22DR-L1TPU0to99FEVT_122X_mcRun3_2021_realistic_v9-v2/GEN-SIM-RECO'
config.Data.ignoreLocality = False
config.Data.unitsPerJob     = 5000
NJOBS = 100  
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits      = 70000000
config.Data.splitting       ='EventAwareLumiBased'#'LumiBased'#'FileBased'#EventAwareLumiBased'
#config.Data.runRange        = '355862-356071'
config.JobType.maxMemoryMB = 5000
#config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/Cert_Collisions2022_eraC_355862_357482_Muon.json'
#config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/Cert_Collisions2022_eraG_362433_362760_Golden.json'
config.Data.outLFNDirBase = '/store/user/almuhamm/ZMu_Test'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'

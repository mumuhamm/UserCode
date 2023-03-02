from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Run2022G_from362755'
#config.General.workArea = 'v5_JetMET'
config.General.workArea = 'v6_Express'
#config.General.workArea = 'v7_EGamma'
#config.General.workArea = 'v8_MuonEG'
#config.General.workArea = 'v9_Muon'
config.General.transferLogs = True 
config.General.transferOutputs = True 

config.section_("Data")
#config.Data.inputDataset = '/Muon/Run2022D-ZMu-PromptReco-v2/RAW-RECO'
#config.Data.inputDataset = '/JetMET/Run2022G-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
config.Data.inputDataset = '/ExpressPhysics/Run2022G-Express-v1/FEVT'
#config.Data.inputDataset = '/EGamma/Run2022G-ZElectron-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset = '/MuonEG/Run2022G-TopMuEG-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset = '/Muon/Run2022G-ZMu-PromptReco-v1/RAW-RECO'

#config.Data.lumiMask='Cert_Collisions2022_eraG_from362755.json'
config.Data.lumiMask='Cert_Collisions2022_eraG_362433_362760_Golden.json'
#config.Data.lumiMask='Cert_Collisions2022_eraD_357538_357900_Golden.json'
#config.Data.lumiMask='Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.lumiMask='Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'

config.Data.runRange = '362719-362760'
#config.Data.runRange = '295606'

config.Data.useParent = False 
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 50 #number of files per jobs
config.Data.totalUnits =  -1 #number of event
config.Data.outLFNDirBase = '/store/user/konec/crabout/'
config.Data.publication = False 
config.Data.outputDatasetTag = 'CRAB_CMSSW_12_4_8_ana'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'makeTree.py'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['omtfTree.root', 'omtfHelper.root']

config.section_("Site")
#config.Site.whitelist = ['T3_CH_CERNCAF']
#config.Site.whitelist = ['T2_CH_CERN']
#config.Site.storageSite = 'T2_PL_Swierk'
config.Site.storageSite = 'T3_CH_CERNBOX'
#config.Site.blacklist = ['T2_KR_*','T2_CN_*','T2_BR_*','T2_US_Florida','T2_US_UCSD']

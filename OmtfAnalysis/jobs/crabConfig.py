from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Run2022D'
config.General.workArea = 'v4_Muon'
#config.General.workArea = 'v2_JetMET'
config.General.transferLogs = True 
config.General.transferOutputs = True 

config.section_("Data")
#config.Data.inputDataset = '/JetMET/Run2022D-JetHTJetPlusHOFilter-PromptReco-v2/RAW-RECO'
config.Data.inputDataset = '/Muon/Run2022D-ZMu-PromptReco-v2/RAW-RECO'


config.Data.lumiMask='Cert_Collisions2022_eraD_357538_357900_Golden.json'
#config.Data.lumiMask='Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.lumiMask='Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'

#config.Data.runRange = '282000-283000'
#config.Data.runRange = '295606'

config.Data.useParent = False 
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 300 #number of files per jobs
config.Data.totalUnits =  -1 #number of event
config.Data.outLFNDirBase = '/store/user/konec/test/'
config.Data.publication = False 
#config.Data.outputDatasetTag = 'CRAB3_tutorial_May2015_Data_analysis'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'makeTree.py'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['omtfTree.root', 'omtfHelper.root']

config.section_("Site")
#config.Site.whitelist = ['T3_CH_CERNCAF']
#config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_PL_Swierk'
#config.Site.blacklist = ['T2_KR_*','T2_CN_*','T2_BR_*','T2_US_Florida','T2_US_UCSD']

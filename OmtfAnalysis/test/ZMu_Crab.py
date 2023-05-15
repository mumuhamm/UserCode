from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'OMTF_JetMet'
config.General.requestName = 'SingMu_RecoMuon_JetMet_EraG_OMTFL1T'
config.section_('JobType')
config.JobType.psetName = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/makeTree_SingleMuZMu_Displaced.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['omtfTree.root']
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
config.Data.inputDataset = '/JetMET/Run2022G-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
config.Data.ignoreLocality = False
config.Data.unitsPerJob     = 5000
NJOBS = 100  
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits      = 700000
config.Data.splitting       ='EventAwareLumiBased'#'LumiBased'#'FileBased'#EventAwareLumiBased'
#config.Data.runRange        = '355862-356071'
config.JobType.maxMemoryMB = 5000
#config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/Cert_Collisions2022_eraC_355862_357482_Muon.json'
config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/Cert_Collisions2022_eraG_362433_362760_Golden.json'
config.Data.outLFNDirBase = '/store/user/almuhamm/ZMu_Test'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'

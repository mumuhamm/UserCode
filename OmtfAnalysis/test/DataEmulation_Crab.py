from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'OMTF_ZMuF24_muon0_v1_DataEmulation'
config.General.requestName = 'OMTF_ZMuF24_muon0_v1_DataEmulation'
config.section_('JobType')
config.JobType.psetName = '/eos/user/a/almuhamm/01.MuonTech/WorkArea_ModifiedPhaseII/CMSSW_14_1_0_pre0/src/UserCode/OmtfAnalysis/test/makeTree_DataEmulation.py'
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
config.Data.inputDataset  ='/Muon0/Run2024F-ZMu-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset ='/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Reco-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RECO'
#config.Data.inputBlocks = [
#    '00265b23-7298-42ea-9c26-4368c6c9ec9c',
#    '00278475-f3d4-40b0-a895-ba45b86502af',
#    '02461a4a-015b-41c1-b520-9268efc1e62f',
#    '028e39ce-6475-4fed-9fec-79b9a073e9ed',
#    '04ebf202-e4d0-4e53-9830-6b3e71598130',
#    '07aa14d0-9e92-4130-8a8f-3eac9b0b03c0',
#    '0a84bf8a-5708-4312-a15f-2bfd510f5345',
#    '0ac4f5e2-1d30-42f4-8fd6-30e6f3f81045',
#    '0e3a0656-e04f-46f5-8ec6-90d3ede0ee7f',
#    '0e7ad428-17a9-43e4-8899-b2e1b3f25f4c',
#    '112dd77c-c1b1-407f-9a6b-2ece15758102',
#    '1502b4f9-ebbe-43f8-b1ae-6fdb20c8c323',
#    '1540dc97-ab73-4e6f-a4a6-68401d804998'
#]
#config.Data.inputDataset = '/JetMET/Run2022G-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
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
config.Data.outLFNDirBase = '/store/user/almuhamm/OMTF_UW/crabOut24'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'

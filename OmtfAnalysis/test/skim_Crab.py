from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'MinBias_TuneCP5_14TeV-pythia8_Phase2Spring23DIGIRECOMiniAOD-PU140'
config.General.requestName = 'MinBias_TuneCP5_14TeV-pythia8_Phase2Spring23DIGIRECOMiniAOD-PU140'
config.section_('JobType')
config.JobType.psetName = '/eos/user/a/almuhamm/01.MuonTech/LXPLUS8_MaxWorkDoneArea/CMSSW_14_0_0_pre2/src/UserCode/OmtfAnalysis/test/skimMinBiasPileUpConfig.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['thinned_MB_PU140.root']
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')

#config.Data.inputDataset ='/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/Run3Winter23Reco-RnD_126X_mcRun3_2023_forPU65_v1-v2/GEN-SIM-RECO'
#config.Data.inputDataset = '/JetMET1/Run2023C-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset = '/JetMET/Run2022G-JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset = '/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU250_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v2/GEN-SIM-DIGI-RAW-MINIAOD'
#config.Data.inputDataset = '/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9_ext1-v2/GEN-SIM-DIGI-RAW-MINIAOD'
config.Data.inputDataset ='/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU140_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v2/GEN-SIM-DIGI-RAW-MINIAOD'
config.Data.ignoreLocality = False
config.Data.unitsPerJob     = 5000
NJOBS = 100  
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits      = 700000
config.Data.splitting       ='EventAwareLumiBased'#'LumiBased'#'FileBased'#EventAwareLumiBased'
#config.Data.runRange        = '357538-357733'
config.JobType.maxMemoryMB = 5000
#config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/CMSSW_12_6_3/src/UserCode/OmtfAnalysis/test/Cert_Collisions2022_eraC_355862_357482_Muon.json'
#config.Data.lumiMask = '/eos/user/a/almuhamm/01.MuonTech/TestDariosModule/CMSSW_13_1_0/src/UserCode/OmtfAnalysis/test/json/Cert_Collisions2023_eraC_367095_368224_Golden.json'
config.Data.outLFNDirBase = '/store/user/almuhamm/MuSampleSharedDirectory/'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'

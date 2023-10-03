from WMCore.Configuration import Configuration

setEra='Run2023C'
#setType='Muon'
setType='JetMET'
setId='1'
jobVer='3'
json='Cert_Collisions2023_eraC_367095_368823_Golden.json'
#json='Cert_Collisions2023_eraB_366403_367079_Golden.json'

if setType == 'Muon' :
  inputDataSet='ZMu-PromptReco-v1/RAW-RECO'
elif setType == 'JetMET' :
  inputDataSet='JetHTJetPlusHOFilter-PromptReco-v1/RAW-RECO'
else:
  inputDataSet='FIXME'

#---------------------------------
config = Configuration()
config.section_("General")
#config.General.requestName = setEra+setType 
#config.General.workArea = setType+setId+'_jobVer'+jobVer
config.General.workArea = setEra+'_'+setType
config.General.requestName = setType+setId+'_jobVer'+jobVer 
config.General.transferLogs = True 
config.General.transferOutputs = True 

config.section_("Data")
config.Data.inputDataset = '/'+setType+setId+'/'+setEra+'-'+inputDataSet
config.Data.lumiMask=json
#config.Data.lumiMask='Cert_Collisions2022_eraG_362433_362760_Golden.json'
#config.Data.lumiMask='Cert_Collisions2022_eraD_357538_357900_Golden.json'
#config.Data.lumiMask='Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.lumiMask='Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'

#config.Data.runRange = '362719-362760'
#config.Data.runRange = '295606'

config.Data.useParent = False 
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 100 #number of files per jobs
config.Data.totalUnits =  -1 #number of event
config.Data.outLFNDirBase = '/store/user/konec/crabout/'
config.Data.publication = False 
config.Data.outputDatasetTag = setEra+'_'+setType+'_jobVer'+jobVer

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

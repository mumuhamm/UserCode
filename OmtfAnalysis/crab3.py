import CRABClient
from CRABClient.UserUtilities import config 
config = config()

config.General.requestName = 'Nov_2022_test'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'analysis_GMT.py'


# Dziala program ale zla probka
config.Data.inputDataset = '/HSCPgmstau_M_432_TuneZ2star_13TeV_pythia6/jwiechni-Run2029_test_20_10_2022-5d05d887c523296d99604cfb8b1e7b08/USER'

# config.Data.inputDataset = 'file:/scratch/Magisterka/Test_data/PhaseIISpring22DRMiniAOD_DYToLL_M-10To50_noPU_40000_04216b41-07a8-4ec9-a1c3-a24cda929b74_2000Ev.root'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 10
# config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_Nov2022_test'

config.Site.storageSite = 'T2_PL_Swierk'
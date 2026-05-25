#!/usr/bin/env python3
from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand

config = config()

config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = 'OMTF_ZMuEra2026C'
config.section_('JobType')
config.JobType.psetName = '/eos/user/a/almuhamm/05.PrivateMC/DisplacedProduction_SLC8/CMSSW_16_1_0/src/UserCode/OmtfAnalysis/test/makeTree_ZMu.py'
#/eos/user/a/almuhamm/01.MuonTech/WorkArea_ModifiedPhaseII/CMSSW_15_1_0_pre2/src/UserCode/OmtfAnalysis/test/makeTree_ZMu.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['omtfTree.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 2900
config.section_('Data')
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 700000
config.Data.ignoreLocality = False
config.Data.outLFNDirBase = '/store/user/almuhamm/OMTF_UW/crabOut26'
config.Data.publication = False
config.section_('Site')
config.Site.storageSite = 'T3_CH_CERNBOX'

# List of datasets to process
datasets = [
    '/Muon0/Run2026C-ZMu-PromptReco-v1/RAW-RECO',
    '/Muon1/Run2026C-ZMu-PromptReco-v1/RAW-RECO',
    '/Muon2/Run2026C-ZMu-PromptReco-v1/RAW-RECO',
    '/Muon3/Run2026C-ZMu-PromptReco-v1/RAW-RECO'
]

for dataset in datasets:
    shortname = dataset.split('/')[1] + '_' + dataset.split('/')[2]  # e.g. Muon0_Run2025F-ZMu-PromptReco-v1
    config.General.requestName = 'OMTF_' + shortname
    config.Data.inputDataset = dataset
    try:
        crabCommand('submit', config=config)
    except Exception as e:
        print(f"Failed to submit {dataset}: {e}")


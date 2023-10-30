# Ntuple Production for the studies of  L1Trigger Efficiency 
## Contributors
- ```Marcin, Karol, Artur, Alibordi```
(with update with full names soon)
### Generic steps : Clone & Run : 
```bash
cmsrel CMSSW_13_1_0
cd CMSSW_13_1_0/src
cmsenv
git cms-init 
git cms-addpkg L1Trigger/L1TMuon
git cms-addpkg L1Trigger/L1TMuonOverlapPhase1
git cms-addpkg L1Trigger/L1TMuonOverlapPhase2
git cms-merge-topic -u kbunkow:from-CMSSW_13_1_0_KB_v1_displMu_LUTNN/L1Trigger
scram b -j 8
```

### Usercode :
```bash 
git clone -b devel_cmssw13_algosKB https://github.com/mumuhamm/UserCode.git  
cd  UserCode
scram b -j 8
```
### Description :

- ```OmtfAnalysis``` : The usual CMSSW EventAnalyzer runs on the given container provided by the data sample 
- ```OmtfDataFormats``` : Creates Tobjects ( vector of Float_t, Int_t 's etc.) for analysis 
- ```OmtfAnalysis/test/makeTree_SingleMuZMu_Displaced.py``` : PSet.py script for dry run   
- ```OmtfAnalysis/test/ZMu_Crab.py``` : Crab submission script , customise as per your requirements

This set up functional for 2022, 2023 - RAW-RECO samples 
### For Displaced algos : 
-Work in Progress

### Satements :  
Comming soon


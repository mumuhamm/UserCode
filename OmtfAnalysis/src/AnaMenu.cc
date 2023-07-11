#include "UserCode/OmtfAnalysis/interface/AnaMenu.h"
#include "TObjArray.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TGraphErrors.h"
#include "UserCode/OmtfDataFormats/interface/MuonObj.h"
#include "UserCode/OmtfDataFormats/interface/EventObj.h"
#include "UserCode/OmtfDataFormats/interface/TriggerMenuResultObj.h"
#include "UserCode/OmtfAnalysis/interface/Utilities.h"
#include <sstream>
#include <iostream>
#include <cmath>

namespace { } 

AnaMenu::AnaMenu(const edm::ParameterSet& cfg)
   : debug(false), theConfig(cfg),
     acceptL1_Names(cfg.exists("acceptL1_Names") ?  cfg.getParameter<std::vector<std::string> >("acceptL1_Names") : std::vector<std::string>()),
     acceptHLT_Names(cfg.exists("acceptHLT_Names") ?  theConfig.getParameter<std::vector<std::string> >("acceptHLT_Names") : std::vector<std::string>())
{ }

void  AnaMenu::updateMenu(const std::vector<std::string> & menuL1, const std::vector<std::string> & menuHLT)
{
  if (menuL1.size() != 0) theMenuL1 = menuL1;
  if (menuHLT.size() != 0) theMenuHLT = menuHLT;
}

bool AnaMenu::filter( const EventObj* ev, const MuonObj* muon,
                      const TriggerMenuResultObj *bitsL1,
                      const TriggerMenuResultObj *bitsHLT)

{
  const std::vector<unsigned int> & algosL1 = bitsL1->firedAlgos;
  const std::vector<unsigned int> & algosHLT = bitsHLT->firedAlgos;

  typedef std::vector<unsigned int>::const_iterator CIT;

  bool okL1 = false;
  
  debug = false;
  if (debug) std::cout << "================== L1 names: "<< std::endl;
  for (CIT it=algosL1.begin(); it != algosL1.end(); ++it) {
    bool aokL1 = false;
    std::string nameAlgo = theMenuL1[*it];
    if (theAlgosL1.find(nameAlgo) == theAlgosL1.end()) theAlgosL1[nameAlgo]=0;    
    for (std::vector<std::string>::const_iterator is=acceptL1_Names.begin(); is != acceptL1_Names.end(); ++is) { if (*is=="any" || nameAlgo==(*is)) aokL1 = true; }
    if (debug) {std::cout <<nameAlgo; if (aokL1) std::cout <<" <--"; std::cout << std::endl; }
    if (aokL1) okL1=true;
  }

  bool okHLT = false;
  if (debug) std::cout << "================= HLT names: "<< std::endl;
  for (CIT it=algosHLT.begin(); it != algosHLT.end(); ++it) {
    bool aokHLT = false;
    std::string nameAlgo = theMenuHLT[*it];
    if (theAlgosHLT.find(nameAlgo) == theAlgosHLT.end()) theAlgosHLT[nameAlgo]=0;    
    for (const auto & nameHLT : acceptHLT_Names) if(nameHLT=="any" || nameAlgo.find(nameHLT)!=std::string::npos ) aokHLT = true;
    if (debug) {std::cout <<nameAlgo; if (aokHLT) std::cout <<" <--"; std::cout << std::endl; }
    if (aokHLT) okHLT=true;
  }

  if (okL1 && okHLT) {
    for (CIT it=algosL1.begin();  it != algosL1.end();  ++it)  theAlgosL1[ theMenuL1[*it] ]++; 
    for (CIT it=algosHLT.begin(); it != algosHLT.end(); ++it) theAlgosHLT[ theMenuHLT[*it] ]++;
    return true; 
  } else return  false;

}

void AnaMenu::resume(TObjArray& histos)
{
  unsigned int sizeL1  = theAlgosL1.size();
  unsigned int sizeHLT = theAlgosHLT.size();
  TH1D *hMenuAlgosL1  = new TH1D( "hMenuAlgosL1", "hMenuAlgosL1", sizeL1, 1., 1.+sizeL1);  histos.Add(hMenuAlgosL1); 
  TH1D *hMenuAlgosHLT = new TH1D("hMenuAlgosHLT","hMenuAlgosHLT",sizeHLT, 1., 1.+sizeHLT); histos.Add(hMenuAlgosHLT); 
  unsigned int ibin = 0;
  typedef std::map< std::string, unsigned int>::const_iterator CIM;
  std::cout <<" SIZE OF L1 ALGOS: " << sizeL1 << std::endl;
  for (CIM it=theAlgosL1.begin(); it != theAlgosL1.end(); ++it) {
    ibin++;
    hMenuAlgosL1->GetXaxis()->SetBinLabel(ibin, (*it).first.c_str());
    hMenuAlgosL1->SetBinContent(ibin, (*it).second);
    std::cout <<" BIN "<<ibin<<" LABEL: "<<(*it).first.c_str()<<" ENTRIES:"<<(*it).second<<std::endl;
  }
  ibin = 0;
  std::cout <<" SIZE OF HLT ALGOS: " << sizeHLT << std::endl;
  for (CIM it=theAlgosHLT.begin(); it != theAlgosHLT.end(); ++it) {
    ibin++;
    hMenuAlgosHLT->GetXaxis()->SetBinLabel(ibin, (*it).first.c_str());
    hMenuAlgosHLT->SetBinContent(ibin, (*it).second);
//    std::cout <<" BIN "<<ibin<<" LABEL: "<<(*it).first.c_str()<<" ENTRIES:"<<(*it).second<<std::endl;
  }
}


void AnaMenu::init(TObjArray& histos)
{ }

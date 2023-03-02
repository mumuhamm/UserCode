#include "UserCode/OmtfAnalysis/interface/Utilities.h"

#include <sstream>
#include <cmath>

#include "UserCode/OmtfDataFormats/interface/L1Obj.h"

OmtfName omtfUtilities::makeName(const L1Obj & obj) 
{  
  return (obj.type==L1Obj::OMTF || obj.type==L1Obj::OMTF_emu) ? 
             OmtfName(obj.iProcessor, obj.position) : OmtfName(); 
}

double omtfUtilities::code2pt(int pt) { return std::fmin( double(pt-1)/2., 159); }

const int  omtfUtilities::etaBinVal[nEtaBins] = {73, 75, 78, 79, 85, 90, 92, 94, 95, 99, 103, 110, 115, 121};

int omtfUtilities::code2HistoBin (int code) {
    int sign = omtfUtilities::sgn(code);
    switch (abs(code)) {
      case  73 : return sign*1;
      case  75 : return sign*2;
      case  78 : return sign*3;
      case  79 : return sign*4;
      case  85 : return sign*5;
      case  90 : return sign*6;
      case  92 : return sign*7;
      case  94 : return sign*8;
      case  95 : return sign*9;
      case  99 : return sign*10;
      case 103 : return sign*11;
      case 110 : return sign*12;
      case 115 : return sign*13;
      case 121 : return sign*14;
      default:  return sign*0;
    }
}

std::vector<std::string> omtfUtilities::layerNames = { "MB1","MB1phi","MB2","MB2_phi","MB3","MB3_phi",
                                                       "ME1/3", "ME2/2", "ME3/2", "ME1/2",
                                                       "RB1in", "RB1out", "RB2in", "RB2out", "RB3",
                                                       "RE1/3",  "RE2/3",  "RE3/3"};


//  for each index return corresponding ipt code value.   
//  exception: 0 -> returns 0. instead of "no muon"
//             1 -> returns 0.1 instead of 0.
//             32 -> is outside of L1 ptscale. Returns 160.
double L1PtScale::ptBins[]={ 0., 0.1, 
                         1.5,  2., 2.5,  3., 3.5,  4.,   4.5,   5.,   6.,   8., 
                         10., 12., 14., 16., 18., 20.,   22.,  25.,  30.,  35., 
                         40., 45., 50., 55., 60., 65., 70., 80., 90., 100., 120., 140., 180., 250., 350., 500., 
                         1000. };
/*
double L1PtScale::ptBins[]={ 0., 0.1, 
                         1.5,  2., 2.5,  3., 3.5,  4.,   4.5,   5.,   6.,   8., 
                         10., 12., 14., 16., 18., 20.,   22.,  25.,  30.,  35., 
                         40., 50., 60., 70., 80., 100., 120., 150., 200., 500., 
                         1000. };
*/

/*
double L1PtScale::ptBins[]={0., 0.1, 
                         1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 6., 7., 8., 
                         10., 12., 14., 16., 18., 20., 25., 30., 35., 40., 45., 
                         50., 60., 70., 80., 90., 100., 120., 140., 
                         160. };
*/

double L1RpcEtaScale::etaBins[] = {
   -2.10, -1.97, -1.85, -1.73, -1.61, -1.48, -1.36, -1.24, -1.14,
   -1.04, -0.93, -0.83, -0.72, -0.58, -0.44, -0.27, -0.07,
    0.07, 0.27, 0.44, 0.58, 0.72, 0.83, 0.93, 1.04, 1.14,
    1.24, 1.36, 1.48, 1.61, 1.73, 1.85, 1.97, 2.10 };


float L1PtScale::ptValue(unsigned int ptCode)
{
  return (ptCode < nPtBins) ? ptBins[ptCode] : -1;
}

unsigned int L1PtScale::ptCode(float ptValue)
{
  unsigned int result = 0;
  for (unsigned int i = 0; i < nPtBins; i++) {
    if (std::fabs(ptValue) >= ptBins[i]) result = i; else break;
  }
  return result;
}

// for each index keep corresponding lower eta bound of a tower.
float L1RpcEtaScale::etaValue(int etaCode)
{
  if (etaCode > 16) return 2.4;
  else if (etaCode < -16) return -2.4;

  unsigned int etaBin = 16+etaCode;
  return (etaBins[etaBin]+etaBins[etaBin+1])/2.;
}

int L1RpcEtaScale::etaCode(float etaValue)
{
  int result = -17;
  for (unsigned int i = 0; i <= nEtaBins; i++) {
    if (etaValue >= etaBins[i]) result += 1; else break;
  }
  return result;
}


bool RunEffMap::hasRun(unsigned int run) const { return (theRunMap.find(run) != theRunMap.end()); }

std::pair<unsigned int, unsigned int> RunEffMap::stat(unsigned int run) const {
  if (hasRun(run) ) return  theRunMap.at(run); else return {0,0}; 
}

void RunEffMap::addEvent(unsigned int run, bool fired)
{
  if (!hasRun(run)) theRunMap[run] = std::make_pair(0,0);
  theRunMap[run].second++;
  if (fired) theRunMap[run].first++;
}
std::vector<unsigned int> RunEffMap::runs() const
{
  std::vector<unsigned int> result;
  for (auto & runEntry : theRunMap ) result.push_back(runEntry.first);
  return result;
}

RunEffMap::EffAndErr  RunEffMap::effAndErr() const
{
  unsigned int nFired = 0;
  unsigned int nEvent = 0;
  for (auto aRunStat : theRunMap) {
    nFired += aRunStat.second.first;
    nEvent += aRunStat.second.second;
  } 
  return effAndErr(nFired,nEvent);
}

RunEffMap::EffAndErr  RunEffMap::effAndErr(unsigned int run) const
{
  if (!hasRun(run)) return {0.,0.};
  unsigned int nFired = theRunMap.at(run).first;
  unsigned int nEvent = theRunMap.at(run).second;
  return effAndErr(nFired, nEvent);
}

RunEffMap::EffAndErr RunEffMap::effAndErr(unsigned int nFired, unsigned int nEvents) const
{
  double effErr = 0.;
  double eff    = 0.;
  if (nEvents > 0) {
    eff    = double(nFired)/double(nEvents);
    double effMod = (nFired != nEvents) ?  eff : double(nFired-1)/(double)nEvents;
    effErr = sqrt( (1-effMod)*std::max((double)nFired,1.)) /(double)nEvents;
  }
  return {eff,effErr};
}



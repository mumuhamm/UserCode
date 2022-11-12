#include "UserCode/OmtfDataFormats/interface/L1PhaseIIObj.h"
#include "UserCode/OmtfDataFormats/interface/L1PhaseIIObjColl.h"
#include <iostream>


ClassImp(L1PhaseIIObjColl)

L1PhaseIIObjColl L1PhaseIIObjColl::selectByType( TYPE t) const
{
  L1PhaseIIObjColl result;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if (theL1Obj[i].type == t) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]); 
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::selectByPt( double ptMin, double ptMax) const
{
  L1PhaseIIObjColl result;
  const double epsilon = 1.e-9;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if ( theL1Obj[i].pt > (ptMin-epsilon) && theL1Obj[i].pt < (ptMax+epsilon) ) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}
L1PhaseIIObjColl L1PhaseIIObjColl::selectByPtMin( double ptMin) const
{
  L1PhaseIIObjColl result;
  const double epsilon = 1.e-9;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if ( theL1Obj[i].pt > (ptMin-epsilon) ) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::selectByEta( double etaMin, double etaMax) const
{
  L1PhaseIIObjColl result;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if ( etaMin < theL1Obj[i].eta && theL1Obj[i].eta <= etaMax)  result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::selectByBx( int bxMin, int bxMax) const
{
  L1PhaseIIObjColl result;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if ( bxMin <=  theL1Obj[i].bx &&  theL1Obj[i].bx <= bxMax) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::selectByQuality( int qMin, int qMax) const
{
  L1PhaseIIObjColl result;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if ( qMin <=  theL1Obj[i].q &&  theL1Obj[i].q <= qMax) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::selectByMatched() const
{
  L1PhaseIIObjColl result;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if (theL1Matching[i]) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::selectByDeltaR( double deltaRMax) const
{
  L1PhaseIIObjColl result;
  for (unsigned int i=0; i<theL1Obj.size(); i++) if ( theDeltaR[i] <= deltaRMax) result.push_back( theL1Obj[i], theL1Matching[i], theDeltaR[i]);
  return result;
}

L1PhaseIIObjColl L1PhaseIIObjColl::operator+(const L1PhaseIIObjColl &o) const
{
  L1PhaseIIObjColl result = *this;
  for (unsigned int i=0; i<o.theL1Obj.size(); i++) result.push_back( o.theL1Obj[i], o.theL1Matching[i], o.theDeltaR[i]);
  return result;
}

void L1PhaseIIObjColl::push_back(const L1PhaseIIObj & obj, bool match, double deltaR)
{
  theL1Obj.push_back(obj);
  theL1Matching.push_back(match);
  theDeltaR.push_back(deltaR);
}





std::vector<L1PhaseIIObj> L1PhaseIIObjColl::typeSelector(const  std::vector<L1PhaseIIObj> & col,  
 TYPE t1, TYPE t2, TYPE t3, TYPE t4)
{
  std::vector<L1PhaseIIObj> result;
  for (std::vector<L1PhaseIIObj>::const_iterator it= col.begin(); it != col.end(); ++it) {
    if ( it->type == t1 || it->type == t2 || it->type == t3 ||it->type == t4 ) result.push_back(*it); 
  }
  return result; 
}
std::vector<L1PhaseIIObj> L1PhaseIIObjColl::getL1ObjsMatched(double ptMin) const 
{
  std::vector<L1PhaseIIObj> result;
  unsigned int nObj = theL1Obj.size();
  unsigned int nCom = theL1Matching.size();

  for (unsigned int i=0; i<nObj && i<nCom; ++i) 
      if (theL1Matching[i] && theL1Obj[i].pt >= ptMin) result.push_back(theL1Obj[i]);

  return result;
}

std::vector<L1PhaseIIObj> L1PhaseIIObjColl::getL1ObjsSelected(
    bool requireMatched, 
    bool requireNonMatched, 
    double ptMin, double ptMax,
    int bxMin, int bxMax,
    double etaMin, double etaMax, 
    double phiMin, double phiMax,
    int qMin, int qMax) const 
{
  std::vector<L1PhaseIIObj> result;
  unsigned int nMS = theL1Matching.size();
  for (unsigned int i=0; i<theL1Obj.size(); ++i) {
	  bool isMatched = ( (i<nMS) && theL1Matching[i] );
	  if (requireMatched && !isMatched ) continue;
	  if (requireNonMatched && isMatched) continue;
	  if (theL1Obj[i].pt < ptMin) continue;
	  if (theL1Obj[i].pt > ptMax) continue;
	  if (theL1Obj[i].bx < bxMin) continue;
	  if (theL1Obj[i].bx > bxMax) continue;
	  if (theL1Obj[i].eta < etaMin) continue;
	  if (theL1Obj[i].eta > etaMax) continue;
	  if (theL1Obj[i].phi < phiMin) continue;
	  if (theL1Obj[i].phi > phiMax) continue;
	  if (theL1Obj[i].q < qMin) continue;
	  if (theL1Obj[i].q > qMax) continue;
	  result.push_back(theL1Obj[i]);
  }
  return result;
}


std::ostream & operator<< (std::ostream &out, const L1PhaseIIObjColl &col)
 {
  for (unsigned int i=0; i< col.theL1Obj.size(); ++i) {
    out <<"("<<i<<")"<<col.theL1Obj[i];
//    out <<" matched: "<< col.theL1Matching[i]<<" deltaR: "<< col.theDeltaR[i];
    if (i !=  col.theL1Obj.size()-1) out <<std::endl;
  }
   return out;
 }



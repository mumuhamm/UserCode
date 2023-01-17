#include "UserCode/OmtfDataFormats/interface/GenObj.h"
#include <bitset>
#include <iomanip>


std::ostream & operator<< (std::ostream &out, const GenObj &o)
{
  out<<"GenObj: ";
  out<<" PDG id: "<<o.pdgId();
  out<<" charge: "<<o.charge();
  out<<"pt: "<<o.pt()<<" eta: "<<o.eta()<<" phi: "<<o.phi();
  out<<" status: "<<o.status()<<" motherId: "<<o.motherId();
  out<<" x coordinate of vertex position: "<<o.vx();
  out<<" y coordinate of vertex position: "<<o.vy();
  out<<" z coordinate of vertex position: "<<o.vz();



  out<<std::endl;

  return out;
}


ClassImp(GenObj)

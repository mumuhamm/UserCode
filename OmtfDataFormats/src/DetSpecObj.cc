#include "UserCode/OmtfDataFormats/interface/DetSpecObj.h"
#include <iomanip>

DetSpecObj::DET DetSpecObj::name2type(const std::string name) 
{
  if      (name=="RPCb") return DetSpecObj::DET::RPCb;
  else if (name=="RPCe") return DetSpecObj::DET::RPCe;  
  else if (name=="DT")   return DetSpecObj::DET::DT;  
  else if (name=="CSC")  return DetSpecObj::DET::CSC;  
  else                   return DetSpecObj::DET::NONE;
}

std::ostream& operator<<(std::ostream& os, const DetSpecObj& det) 
{
  std::string wd;
  std::string sr;
  std::string sc;
  switch (det.type()) {
    case DetSpecObj::DET::RPCb : os << "RPCb"; wd="wheel"; sr="stat"; sc="sect"; break; 
    case DetSpecObj::DET::DT   : os << "  DT"; wd="wheel"; sr="stat"; sc="sect"; break; 
    case DetSpecObj::DET::RPCe : os << "RPCe"; wd=" disk", sr="ring"; sc="cham"; break; 
    case DetSpecObj::DET::CSC  : os << " CSC"; wd=" disk", sr="ring"; sc="cham"; break; 
    default                    : os << "none"; break; 
  }
  os <<" "<<wd<<":"<<std::setw(2)<<det.whellORdisk()
     <<" "<<sr<<":"<<std::setw(2)<<det.statORring()
     <<" "<<sc<<":"<<std::setw(3)<<det.sectorORchamber();

  return os;
}
ClassImp(DetSpecObj)


#include "UserCode/OmtfDataFormats/interface/BxStatObj.h"

#include <cmath>
#include <iomanip>


const int BxStatObj::offset;
const unsigned int BxStatObj::dim;

namespace {
template <class T> T sqr( T t) {return t*t;}
}

unsigned int  BxStatObj::mom0() const
{ 
  unsigned int result = 0; 
  for (unsigned int i=0; i<dim; ++i) result += theCounts[i]; 
  return result; 
}

double  BxStatObj::mom1() const
{ 
  double result = 0.; 
  for (unsigned int i=0; i<dim; ++i) {
     result += (static_cast<int>(i)-offset)*static_cast<int>(theCounts[i]); 
  }
  return result; 
}

double  BxStatObj::mean() const
{ 
  unsigned int sum = mom0(); 
  return sum==0 ? 0. : mom1()/sum; 
}

double  BxStatObj::rms() const
{
  double result = 0.;
  int      sum = mom0();
  if (sum==0) return 0.;
  double mean = this->mean();
  for (unsigned int i=0; i<dim; ++i) result += theCounts[i]*sqr(mean-(static_cast<int>(i)-offset));
  result /= sum;
  return sqrt(result);
}


std::ostream& operator<<(std::ostream& os, const BxStatObj& stat) {
  os <<" mean: "<<std::setw(5)<<std::setprecision(2) <<stat.mean();
  os <<" rms: "<<std::setw(4)<<std::fixed<<std::setprecision(2)<<stat.rms();
  os <<" counts: ";
  for (unsigned int i=0; i< stat.dim; i++) {
   unsigned int n= ( (int)i-stat.offset==0) ? 5 : 4;
   os <<std::setw(n)<< stat.theCounts[i];
  }
  return os;
}
ClassImp(BxStatObj)


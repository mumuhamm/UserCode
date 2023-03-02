#include "UserCode/OmtfAnalysis/interface/SynchroCounts.h"

#include <cmath>
#include <iomanip>


unsigned int SynchroCounts::firstHit() const
{
  for (unsigned int i=0; i <8 ; ++i) if(theCounts[i]) return i;
  return 8;
}

void  SynchroCounts::set(unsigned int bxDiff)
{
  if (bxDiff < 8) theCounts[bxDiff]=1;
}

void  SynchroCounts::increment(unsigned int bxDiff)
{
  if (bxDiff < 8) theCounts[bxDiff]++;
}

SynchroCounts & SynchroCounts::operator+=(const SynchroCounts &rhs)
{
  for (unsigned int i=0; i<8; ++i) theCounts[i]+=rhs.theCounts[i];
  return *this;
}

unsigned int  SynchroCounts::mom0() const
{ unsigned int result = 0; for (unsigned int i=0; i<8; ++i) result += theCounts[i]; return result; }

double  SynchroCounts::mom1() const
{ double result = 0.; for (unsigned int i=0; i<8; ++i) result += i*theCounts[i]; return result; }

double  SynchroCounts::mean() const
{ unsigned int sum = mom0(); return sum==0 ? 0. : mom1()/sum; }

double  SynchroCounts::rms() const
{
  double result = 0.;
  int      sum = mom0();
  if (sum==0) return 0.;
  double mean = mom1()/sum;
  for (int i=0; i<8; ++i) result += theCounts[i]*(mean-i)*(mean-i);
  result /= sum;
  return sqrt(result);
}

std::string  SynchroCounts::print() const
{
  std::ostringstream str;
  str<<" mean: "<<std::setw(6)<<std::setprecision(5)<<mean();
  str<<" rms: "<<std::setw(6)<<std::fixed<<std::setprecision(4)<<rms();
  str<<" counts:"; for (int i=0; i<8; ++i) str<<" "<<std::setw(4)<<theCounts[i];
  return str.str();
}

bool SynchroCounts::operator==(const SynchroCounts &o) const
{
  for (unsigned int idx=0; idx <8; ++idx) if (theCounts[idx] != o.theCounts[idx]) return false;
  return true;
}



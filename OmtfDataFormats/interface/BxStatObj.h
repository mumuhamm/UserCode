#ifndef BxStatObj_H
#define BxStatObj_H

#include "TObject.h"
#include <iostream>
#include <cassert>


class BxStatObj : public TObject {
public:
  BxStatObj() : theCounts(dim,0) {}
  BxStatObj( const std::vector<unsigned int> & d) { assert((d.size()==dim)); theCounts=d; }
  virtual ~BxStatObj() {}
  void incrementBx(int bx, unsigned int incr=1) {
    int idx = bx+offset; 
    if (idx < (int)dim && idx >=0) theCounts[idx]+=incr; 
  }
  BxStatObj & operator+=(const BxStatObj & o) {
    for (unsigned int idx=0; idx < dim; ++idx) theCounts[idx]+=o.theCounts[idx];
    return *this;
  }
  unsigned int getBx(int bx) const {
    int idx = bx+offset; 
    if (idx < (int)dim && idx >=0) return theCounts[static_cast<unsigned int>(idx)];
    return 0;
  }
  unsigned int operator()(int bx) const { return getBx(bx); } 

  const std::vector<unsigned int> & raw() const { return theCounts; }
  void print() { std::cout << *this << std::endl; } 

  double rms() const;
  double mean() const;
  unsigned int sum() const { return mom0(); }

private:
  unsigned int  mom0() const;
  double mom1() const;

  static const int offset = 3;
  static const unsigned int dim = 8;

  std::vector<unsigned int> theCounts;

  friend class DetBxStatObj;
  friend std::ostream& operator<<(std::ostream& os, const BxStatObj& stat);

ClassDef(BxStatObj,1)
};
#endif

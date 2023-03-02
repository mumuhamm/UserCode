#ifndef DetBxStatObj_H
#define DetBxStatObj_H

#include "TObject.h"
#include "DetSpecObj.h"
#include "BxStatObj.h"
#include <map>
#include <vector>
#include <algorithm>
#include <string>

class DetBxStatObj : public TObject {

public: 
  DetBxStatObj(std::string aname = "DetBxStat") : name(aname) {}

  virtual ~DetBxStatObj() {}

  virtual const char * GetName() const { return name.c_str(); }

  virtual DetBxStatObj & operator+= (const DetBxStatObj& o);

  std::vector<DetSpecObj> dets() const;

  BxStatObj getBxStat(const DetSpecObj & det) const;
  
  BxStatObj & bxStat(const DetSpecObj & det);

  void print() const;

private:

  std::string name;
  std::vector< std::pair<uint32_t, BxStatObj> > data;

ClassDef(DetBxStatObj,1)
};

#endif

#ifndef DetSpecObj_H
#define DetSpecObj_H

#include "TObject.h"
#include <iostream>

class DetSpecObj : public TObject {
public:
  enum DET { NONE=0, RPCb=1, RPCe=2, DT=3, CSC=4 };
  DetSpecObj(DET type, int wd, int sr, int sc) {
    data =   (static_cast<unsigned int>(type) << 16)
           | (((static_cast<unsigned int>(wd+8))&0xF)<<12) 
           | ((sr&0xF)<<8) 
           | (sc&0xFF); 
  }
  DetSpecObj(uint32_t raw) : data(raw) {}
  virtual ~DetSpecObj(){}
  DET type() const { return static_cast<DET>((data>>16)&0xF); }
  int          whellORdisk()    const { return static_cast<int>((data>>12)&0xF) - 8;}
  unsigned int statORring()     const { return ((data>>8)&0xF);}
  unsigned int sectorORchamber() const { return (data & 0xFF);}
  void print() { std::cout << *this << std::endl; }
  uint32_t raw() const { return data; }

  static DET  name2type(const std::string name);
  
private:
  uint32_t data;
  friend class DetBxStatObj;  
  friend std::ostream& operator<<(std::ostream& os, const DetSpecObj& det);
ClassDef(DetSpecObj,1)
};
#endif

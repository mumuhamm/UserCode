#ifndef L1Obj_H
#define L1Obj_H
#include "TObject.h"
#include <iostream>
#include <math.h>

class L1Obj : public TObject {

public:
  
  enum TYPE { NONE, RPCb, RPCf, DT, CSC, GMT, RPCb_emu, RPCf_emu, GMT_emu, OMTF, OMTF_emu, BMTF, EMTF, uGMT, uGMT_emu, uGMTPhase2_emu};

  double pt, eta, phi;
  double z0, d0;
  int disc;
  int   bx, q, hits, charge, refLayer;
  TYPE  type;
  int   iProcessor, position;

  L1Obj();

  bool isValid() const { return type!=NONE && pt>0;}

  double ptValue() const; 
  double etaValue() const; 
  double phiValue() const; 
  int chargeValue() const; 

  ClassDef(L1Obj,5)
};


std::ostream & operator<< (std::ostream &out, const L1Obj &o);

#endif

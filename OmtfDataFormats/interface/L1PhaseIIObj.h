#ifndef L1PhaseIIObj_H
#define L1PhaseIIObj_H
#include "TObject.h"
#include <iostream>
#include <math.h>


class L1PhaseIIObj : public TObject {

public:
  
  enum TYPE { NONE, RPCb, RPCf, DT, CSC, GMT, RPCb_emu, RPCf_emu, GMT_emu, OMTF, OMTF_emu, BMTF, EMTF, uGMT, uGMT_emu };

  int pt, eta, phi;
  int disc;
  int   bx, q, hits, charge, refLayer;
  TYPE  type;
  int   iProcessor, position;

  L1PhaseIIObj();

  double modulo2PI (double phi) const{ 
    while (phi > 2*M_PI) phi -= 2*M_PI;
    while (phi < 0.) phi += 2*M_PI;
    return phi;
  }

  bool isValid() const { return type!=NONE && pt>0;}

  double ptValue() const { return (pt-1.)/2.; }
  double etaValue() const { return eta/240.*2.61; }
  double phiValue() const {
    if (type==OMTF || type==OMTF_emu || type==EMTF) 
    return modulo2PI( ( (15.+iProcessor*60.)/360. + phi/576. ) *2*M_PI) ;  
    else if (type==BMTF) return modulo2PI( ( (-15.+iProcessor*30.)/360. + phi/576. ) *2*M_PI);
    else if (type==uGMT || type==uGMT_emu) return modulo2PI((phi/576.)*2*M_PI);
    else return 9999.;
  }
  int chargeValue() const { return pow(-1,charge); }

  ClassDef(L1PhaseIIObj,1)
};


std::ostream & operator<< (std::ostream &out, const L1PhaseIIObj &o);

#endif

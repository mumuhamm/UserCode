#ifndef GenObj_H
#define GenObj_H
#include <ostream>

#include "TObject.h"
class GenObj : public TObject {
public:
 GenObj(float pt=0., float eta=0., float phi=0.,float mass=0., 
	int charge=0, int pdgid=0, int st=0, int mother=0, double vx=0):
  _pt(pt),_eta(eta),_phi(phi),_mass(mass),_charge(charge),_id(pdgid),_status(st),_mid(mother),_vx(vx) {}
  virtual ~GenObj() {}
public:
  float pt() const { return _pt;}
  float eta() const { return _eta;}
  float phi() const { return _phi;}
  float mass() const { return _mass;}
  int pdgId() const { return _id;}
  int status() const { return _status;}
  int motherId() const { return _mid;}
  int charge() const { return _charge;}
  double vx() const { return _vx;}


private:  
  float _pt,_eta,_phi,_mass; 
  int _charge,_id,_status,_mid; 
  double _vx;

public:
  ClassDef(GenObj,2);
};

std::ostream & operator<< (std::ostream &out, const GenObj &o);

#endif

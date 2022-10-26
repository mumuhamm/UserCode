#include "UserCode/OmtfDataFormats/interface/DetBxStatObj.h"
#include <functional>

namespace {
struct LessData { 
  bool operator() (const std::pair<uint32_t, BxStatObj> &o1,
                   const std::pair<uint32_t, BxStatObj> &o2) { 
    return o1.first < o2.first; 
  } 
};
}

DetBxStatObj & DetBxStatObj::operator+= (const DetBxStatObj& o) 
{
  for (const auto & oel : o.data) bxStat(oel.first)+=oel.second;
  return *this;
}

BxStatObj & DetBxStatObj::bxStat(const DetSpecObj & det) 
{
  auto test = std::make_pair(det.raw(), BxStatObj());
  auto pos = std::lower_bound(data.begin(), data.end(), test, LessData());
  if (pos == data.end() || pos->first != test.first) pos = data.insert(pos,test);
  return pos->second;
}

std::vector<DetSpecObj> DetBxStatObj::dets() const 
{
    std::vector<DetSpecObj> result;
    for (auto d : data) result.push_back(DetSpecObj(d.first));
    return result;
}

BxStatObj DetBxStatObj::getBxStat(const DetSpecObj & det) const
{
  auto test = std::make_pair(det.raw(), BxStatObj());
  auto pos = std::lower_bound(data.begin(), data.end(), test, LessData());
  return (pos == data.end() || pos->first != test.first) ? BxStatObj() : pos->second;  
}


void DetBxStatObj::print() const 
{
  for (auto d : data) std::cout << DetSpecObj(d.first)<<" BxStat:" << d.second << std::endl;
}

ClassImp(DetBxStatObj)

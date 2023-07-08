#include "UserCode/OmtfAnalysis/interface/RPCDetIdUtil.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/RPCGeometry/interface/RPCGeometry.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

void RPCDetIdUtil::print(const edm::EventSetup &es)
{
 // edm::ESHandle<RPCGeometry> rpcGeometry;
 // es.get<MuonGeometryRecord>().get(rpcGeometry);


 // idToDet() 

    edm::ESGetToken<RPCGeometry, MuonGeometryRecord> rpcGeometry;
    
 // rpcGeometry(iC.esConsumes<RPCGeometry, MuonGeometryRecord>());
 // GlobalPoint position = rpcGeometry->idToDet(theRpcDet)->position();
 /////////En este estaba   GlobalPoint position =  &es.getData(rpcGeometry).idToDet(theRpcDet)->position();
//  GlobalPoint position = (*rpcGeometry).idToDet(theRpcDet)->position();

  const auto* positionPtr = &es.getData(rpcGeometry).idToDet(theRpcDet)->position();
  GlobalPoint position = *positionPtr;
  
  std::cout << (*this) <<" R= "<<position.perp()
                       <<" Z= "<<position.z()
                       <<" eta="<<position.eta()
                       <<" consecutiveLayer: "<<layer(position.eta())
                       << std::endl;
}

std::ostream & operator<< (std::ostream &out, const RPCDetIdUtil &o) {
  out <<"DetId: "<<o.theRpcDet.rawId()
              <<" region: "<<o.theRpcDet.region()
              <<" layer:  "<<o.layer()
              <<" ring/wheel: "<<o.theRpcDet.ring();
  return out;
}


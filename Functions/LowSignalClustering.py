from CloseNeighboursList import *
from ms2_feat_modules import *
from SignalsModulesStats import *
def LowSignalClustering(SignalVec0,minSignal=0):
    ZeroFil=SignalVec0>0
    SignalVec=SignalVec0[ZeroFil]    
    NeighboursList,SignalsSet=CloseNeighboursList(SignalVec,minSignal=minSignal)
    Modules=ms2_feat_modules(AdjacencyList=NeighboursList,ms2_ids=SignalsSet)
    ModulesStats=SignalsModulesStats(Modules,SignalVec)
    NoiseTres=ModulesStats[0,2]
    return NoiseTres

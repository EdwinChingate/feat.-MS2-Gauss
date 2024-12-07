import numpy as np
from LowSignalClustering import *
from ResolvingChromatogram import *
def Feat_RT_edges(Chromatogram,minSpec=10):
    NoiseTres=LowSignalClustering(SignalVec0=Chromatogram[:,2])
    IntVec=Chromatogram[:,2]
    ValidSignalsLoc=np.where(IntVec>NoiseTres)[0]
    ValidSignalsLoc_Future=ValidSignalsLoc[1:]
    ValidSignalsLoc_Past=ValidSignalsLoc[:-1]
    LocDisVec=ValidSignalsLoc_Future-ValidSignalsLoc_Past
    ValidSignalsTresLoc=np.where(LocDisVec>1)[0]
    N_Clusters=len(ValidSignalsTresLoc)+1
    ClustersMat=np.zeros((N_Clusters,3))
    ClustersMat[1:,0]=ValidSignalsLoc_Future[ValidSignalsTresLoc]
    ClustersMat[:-1,1]=ValidSignalsLoc_Past[ValidSignalsTresLoc]+1
    ClustersMat[0,0]=np.min(ValidSignalsLoc)
    ClustersMat[-1,1]=np.max(ValidSignalsLoc)
    ClustersMat[:,2]=ClustersMat[:,1]-ClustersMat[:,0]
    MinSpecFil=ClustersMat[:,2]>minSpec
    NoNoiseClusters=ClustersMat[MinSpecFil,:]
    FirstChPeak=True
    for no_noise in NoNoiseClusters:
        EarlyLoc=int(no_noise[0])
        LateLoc=int(no_noise[1])
        ChrMat=ResolvingChromatogram(EarlyLoc=EarlyLoc,LateLoc=LateLoc,Chromatogram=Chromatogram,minSpec=minSpec)
        if FirstChPeak:
            ChrPeakMat=ChrMat
            FirstChPeak=False
        else:
            ChrPeakMat=np.append(ChrPeakMat,ChrMat,axis=0)    
    return ChrPeakMat


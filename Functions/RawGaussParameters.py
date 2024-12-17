import numpy as np
from UmbrellasStats import *
def RawGaussParameters(smooth_peak,peaksMin,ExtraPeaks=3,RTCorFrac=10):
    NPeaks=len(peaksMin)
    NSignals=int(len(smooth_peak[:,0]))
    PeaksUmbrellaMat=np.zeros((NPeaks,8))
    ExtraPeaks=min([ExtraPeaks,NPeaks])
    ExtraPeaksUmbrellaMat=np.zeros((ExtraPeaks,4))
    PeaksUmbrellaMat[:,0]=peaksMin
    PeakValley=np.array((peaksMin[1:]+peaksMin[:-1])/2,dtype='int')
    PeaksUmbrellaMat[1:,1]=PeakValley
    PeaksUmbrellaMat[:-1,2]=PeakValley
    PeaksUmbrellaMat[-1,2]=NSignals
    PeaksUmbrellaMat=UmbrellasStats(smooth_peak=smooth_peak,PeaksUmbrellaMat=PeaksUmbrellaMat,NPeaks=NPeaks)
    PeaksUmbrellaMat=PeaksUmbrellaMat[PeaksUmbrellaMat[:,6].argsort(),:]
    ParametersList=list(PeaksUmbrellaMat[:,4:])
    
    minRT=smooth_peak[0,0]
    maxRT=smooth_peak[-1,0]
    RT_interval=maxRT-minRT
    minIntegral_2=PeaksUmbrellaMat[0,6]/2
    RT_std=PeaksUmbrellaMat[-1,5]
    Ref_RT=PeaksUmbrellaMat[-ExtraPeaks:,4]
    rng = np.random.default_rng()
    RandomVec=rng.random(size=ExtraPeaks)
    ExtraRT=RTCorFrac*RandomVec*RT_interval/100+Ref_RT
    
    ExtraPeaksUmbrellaMat[:,1]=RT_std
    ExtraPeaksUmbrellaMat[:,2]=minIntegral_2
    ExtraPeaksUmbrellaMat[:,0]=ExtraRT
    ExtraParametersList=list(ExtraPeaksUmbrellaMat)
    return ParametersList+ExtraParametersList

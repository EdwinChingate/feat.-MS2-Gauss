import numpy as np
from UmbrellasStats import *
def RawGaussParameters(smooth_peak,peaksMin):
    NPeaks=len(peaksMin)
    NSignals=int(len(smooth_peak[:,0]))
    PeaksUmbrellaMat=np.zeros((NPeaks,8))
    PeaksUmbrellaMat[:,0]=peaksMin
    PeakValley=np.array((peaksMin[1:]+peaksMin[:-1])/2,dtype='int')
    PeaksUmbrellaMat[1:,1]=PeakValley
    PeaksUmbrellaMat[:-1,2]=PeakValley
    PeaksUmbrellaMat[-1,2]=NSignals
    PeaksUmbrellaMat=UmbrellasStats(smooth_peak=smooth_peak,PeaksUmbrellaMat=PeaksUmbrellaMat,NPeaks=NPeaks)
    PeaksUmbrellaMat=PeaksUmbrellaMat[PeaksUmbrellaMat[:,6].argsort(),:]
    ParametersList=list(PeaksUmbrellaMat[:,4:])
    return ParametersList

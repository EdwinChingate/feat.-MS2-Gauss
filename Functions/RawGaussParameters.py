import numpy as np
from UmbrellasStats import *
def RawGaussParameters(smooth_peaks,peaksMax):
    NPeaks=len(peaksMax)
    NSignals=int(len(smooth_peaks[:,0]))
    PeaksUmbrellaMat=np.zeros((NPeaks,7))
    PeaksUmbrellaMat[:,0]=peaksMax
    PeakValley=np.array((peaksMax[1:]+peaksMax[:-1])/2,dtype='int')
    PeaksUmbrellaMat[1:,1]=PeakValley
    PeaksUmbrellaMat[:-1,2]=PeakValley
    PeaksUmbrellaMat[-1,2]=NSignals
    PeaksUmbrellaMat=UmbrellasStats(smooth_peaks=smooth_peaks,PeaksUmbrellaMat=PeaksUmbrellaMat,NPeaks=NPeaks)
    PeaksUmbrellaMat=PeaksUmbrellaMat[PeaksUmbrellaMat[:,6].argsort(),:]
    ParametersMat=PeaksUmbrellaMat[:,4:]
    return ParametersMat

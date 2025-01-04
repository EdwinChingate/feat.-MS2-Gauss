import numpy as np
from UmbrellasStats import *
def RawGaussSeed(smooth_peaks,peaksMax):
    NPeaks=len(peaksMax)
    NSignals=int(len(smooth_peaks[:,0]))
    PeaksUmbrellaMat=np.zeros((NPeaks,6))
    PeaksUmbrellaMat[:,0]=peaksMax
    PeakValley=np.array((peaksMax[1:]+peaksMax[:-1])/2,dtype='int')
    PeaksUmbrellaMat[1:,1]=PeakValley
    PeaksUmbrellaMat[:-1,2]=PeakValley
    PeaksUmbrellaMat[-1,2]=NSignals
    PeaksUmbrellaMat=UmbrellasStats(smooth_peaks=smooth_peaks,PeaksUmbrellaMat=PeaksUmbrellaMat,NPeaks=NPeaks)
    ParametersMat=PeaksUmbrellaMat[:,3:]    
    ExtraPeak=(np.mean(ParametersMat,axis=0)).reshape(1,-1)
    ParametersMat=np.append(ParametersMat,ExtraPeak,axis=0)
    ExtraPeak=(np.mean(ParametersMat,axis=0)).reshape(1,-1)
    ParametersMat=np.append(ParametersMat,ExtraPeak,axis=0)
    ParametersMat=ParametersMat[ParametersMat[:,0].argsort(),:]    
    return ParametersMat

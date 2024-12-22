import numpy as np
from UmbrellasStats import *
def RawGaussParameters(smooth_peaks,peaksMax):
    NPeaks=len(peaksMax)
    NSignals=int(len(smooth_peaks[:,0]))
    PeaksUmbrellaMat=np.zeros((NPeaks,7))
    ExtraPeaksMat=np.zeros((2,3))
    PeaksUmbrellaMat[:,0]=peaksMax
    PeakValley=np.array((peaksMax[1:]+peaksMax[:-1])/2,dtype='int')
    PeaksUmbrellaMat[1:,1]=PeakValley
    PeaksUmbrellaMat[:-1,2]=PeakValley
    PeaksUmbrellaMat[-1,2]=NSignals
    PeaksUmbrellaMat=UmbrellasStats(smooth_peaks=smooth_peaks,PeaksUmbrellaMat=PeaksUmbrellaMat,NPeaks=NPeaks)
    PeaksUmbrellaMat=PeaksUmbrellaMat[PeaksUmbrellaMat[:,6].argsort(),:]
    ParametersMat=PeaksUmbrellaMat[:,4:]
    ExtraPeaksMat[0,:]=ParametersMat[-1,:].copy()
    ExtraPeaksMat[-1,:]=ParametersMat[0,:]
    ExtraPeaksMat[:,2]=ParametersMat[0,2]/100    
    ParametersMat=np.append(ParametersMat,ExtraPeaksMat,axis=0)
    return ParametersMat

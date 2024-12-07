from scipy.signal import find_peaks
from scipy.signal import savgol_filter
import numpy as np
def ResolvingChromatogram(EarlyLoc,LateLoc,Chromatogram,minSpec):
    PeakChr=Chromatogram[EarlyLoc:LateLoc,:]
    NSpec=len(PeakChr[:,0])
    SoftInt = savgol_filter(PeakChr[:,2], 11, 3)#those could become more general parameters
    peaksMin = find_peaks(-SoftInt,prominence=1,distance=minSpec)[0]
    if len(peaksMin)<1:
        return np.array([EarlyLoc,LateLoc]).reshape(-1,1).T
    N_min=len(peaksMin)+1
    ChrMat=np.zeros((N_min,2))
    ChrMat[1:,0]=peaksMin
    ChrMat[:-1,1]=peaksMin
    ChrMat[-1,1]=NSpec
    ChrMat=ChrMat+EarlyLoc
    NSpecVec=ChrMat[:,1]-ChrMat[:,0]
    MinSpecFil=NSpecVec>minSpec
    ChrMat=ChrMat[MinSpecFil,:]
    return ChrMat

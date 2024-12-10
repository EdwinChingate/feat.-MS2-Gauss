from scipy.signal import find_peaks
from scipy.signal import savgol_filter
import numpy as np
def ResolvingChromatogram(Chromatogram,minSpec,int_col=5,EarlyLoc=0,LateLoc=0,minWindow=11,minPoly=5):
    if EarlyLoc==0 and LateLoc==0:
        LateLoc=len(Chromatogram[:,0])
    PeakChr=Chromatogram[EarlyLoc:LateLoc,:]    
    NSpec=len(PeakChr[:,0])
    NSpec_2=int(NSpec/2)
    toRegLoc=np.linspace(0,NSpec-1,NSpec_2,dtype='int')
    wl=min([int(NSpec_2/4)*2+1,minWindow])
    poly=min([int(wl/2),minPoly])
    SoftInt = savgol_filter(PeakChr[toRegLoc,int_col], wl, poly)
    peaksMin = find_peaks(-SoftInt,prominence=1,distance=minSpec)[0]
    if len(peaksMin)<1:
        return np.array([EarlyLoc,LateLoc]).reshape(-1,1).T
    N_min=len(peaksMin)+1
    ChrMat=np.zeros((N_min,2))
    ChrMat[1:,0]=toRegLoc[peaksMin]
    ChrMat[:-1,1]=toRegLoc[peaksMin]
    ChrMat[-1,1]=NSpec
    ChrMat=ChrMat+EarlyLoc
    NSpecVec=ChrMat[:,1]-ChrMat[:,0]
    MinSpecFil=NSpecVec>minSpec
    ChrMat=ChrMat[MinSpecFil,:]
    return ChrMat

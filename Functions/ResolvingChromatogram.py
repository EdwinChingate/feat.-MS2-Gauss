from scipy.signal import find_peaks
from scipy.signal import savgol_filter
import numpy as np
#returning tresholds as RT
def ResolvingChromatogram(Chromatogram,minSpec,minPoints=10,int_col=5,EarlyLoc=0,LateLoc=0,minWindow=11,minPoly=5):
    if EarlyLoc==0 and LateLoc==0:
        LateLoc=len(Chromatogram[:,0])
    PeakChr=Chromatogram[EarlyLoc:LateLoc,:].copy()
    NSpec=len(PeakChr[:,0])
    smooth_peak=SmoothPeak(PeakChr=PeakChr,stdDistance=1,SavgolWindowTimes=2,minPoly=5,int_col=1,RT_col=2)
    peaksMin=find_peaks(smooth_peak[:,1],prominence=1,distance=minPoints)[0]
    plt.plot(PeakChr[:,2],PeakChr[:,1],'.')
    plt.plot(smooth_peak[:,0],smooth_peak[:,1],'-')
    plt.plot(smooth_peak[peaksMin,0],smooth_peak[peaksMin,1],'o')
    plt.show()    
    if len(peaksMin)<1:
        ChrMat=np.array([PeakChr[0,0],PeakChr[-1,0]]).reshape(-1,1).T
        return ChrMat
    N_min=len(peaksMin)+1
    ChrMat=np.zeros((N_min,2))
    ChrMat[1:,0]=smooth_peak[peaksMin,0]
    ChrMat[:-1,1]=smooth_peak[peaksMin,0]
    ChrMat[-1,1]=NSpec
    ChrMat=ChrMat+EarlyLoc
   # NSpecVec=ChrMat[:,1]-ChrMat[:,0]
   # MinSpecFil=NSpecVec>minSpec
    #ChrMat=ChrMat[MinSpecFil,:]
    return ChrMat

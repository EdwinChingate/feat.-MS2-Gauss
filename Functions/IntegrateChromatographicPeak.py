from scipy import integrate
from scipy.signal import savgol_filter
from BaseLine import *
def IntegrateChromatographicPeak(EarlyLoc,LateLoc,Chromatogram,minIntFrac=1,RT_col=2,int_col=5,BaseLinePoints_2=3,minWindow=11,minPoly=5):
    PeakChr=Chromatogram[EarlyLoc:LateLoc,:]    
    NSpec=len(PeakChr[:,0])
    wl=min([int(NSpec/4)*2+1,minWindow])
    poly=min([int(wl/2),minPoly])    
    SoftInt=savgol_filter(PeakChr[:,int_col], wl, poly)
    BL=BaseLine(EarlyLoc=EarlyLoc,LateLoc=LateLoc,Chromatogram=Chromatogram,RT_col=RT_col,int_col=int_col,BaseLinePoints_2=BaseLinePoints_2)
    No_NoiseSignal=SoftInt-BL    
    #plt.plot(PeakChr[:,2],PeakChr[:,1],'.')
    #plt.plot(PeakChr[:,2],SoftInt,'-')
    #plt.plot(PeakChr[:,2],BL,'-')
    #plt.show()
    maxInt=np.max(No_NoiseSignal)
    minInt=minIntFrac*maxInt/100
    PosLoc=np.where(No_NoiseSignal>minInt)[0]
    if len(PosLoc)<4:
        return 0
    No_NoiseSignal=No_NoiseSignal[PosLoc]
    X=PeakChr[PosLoc,RT_col]
    Y=No_NoiseSignal
    #plt.plot(X,Y,'-')
    #plt.show()
    I=integrate.simpson(y=Y,x=X)   
    return I

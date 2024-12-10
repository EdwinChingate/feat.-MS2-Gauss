from scipy import integrate
from scipy.signal import savgol_filter
from BaseLine import *
def IntegrateChromatographicPeak(EarlyLoc,LateLoc,Chromatogram,RT_col=2,int_col=5,BaseLinePoints_2=3):
    SoftInt=savgol_filter(Chromatogram[EarlyLoc:LateLoc,int_col], 11, 3)
    BL=BaseLine(EarlyLoc=EarlyLoc,LateLoc=LateLoc,Chromatogram=Chromatogram,RT_col=RT_col,int_col=int_col,BaseLinePoints_2=BaseLinePoints_2)
    No_NoiseSignal=SoftInt-BL
    NegLoc=No_NoiseSignal<0
    No_NoiseSignal[NegLoc]=0
    X=Chromatogram[EarlyLoc:LateLoc,RT_col]
    Y=No_NoiseSignal
    I=integrate.simpson(y=Y,x=X)    
    return I

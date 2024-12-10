import numpy as np
from IntegrateChromatographicPeak import *
def Summarize_ms1_ChPeak(EarlyLoc,LateLoc,Chromatogram,int_col,RT_col,BaseLinePoints_2=3):
    ChPeak=Chromatogram[EarlyLoc:LateLoc,:].copy()   
    Integral=IntegrateChromatographicPeak(EarlyLoc=EarlyLoc,LateLoc=LateLoc,Chromatogram=Chromatogram,int_col=int_col,RT_col=RT_col,BaseLinePoints_2=BaseLinePoints_2)
    ChPeak=ChPeak[(-ChPeak[:,int_col]).argsort(),:]
    min_RT=np.min(ChPeak[:,RT_col])
    max_RT=np.max(ChPeak[:,RT_col])
    mz=ChPeak[0,0]
    RT=ChPeak[0,RT_col]
    SummaryChPeak=[RT]+[min_RT]+[max_RT]+[Integral]
    return SummaryChPeak

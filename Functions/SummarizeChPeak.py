from IntegrateChromatographicPeak import *
def SummarizeChPeak(EarlyLoc,LateLoc,Chromatogram,BaseLinePoints_2=3):
    ChPeak=Chromatogram[EarlyLoc:LateLoc,:].copy()   
    Integral=IntegrateChromatographicPeak(EarlyLoc,LateLoc,Chromatogram,BaseLinePoints_2=BaseLinePoints_2)
    ChPeak=ChPeak[(-ChPeak[:,5]).argsort(),:]
    min_RT=np.min(ChPeak[:,2])
    max_RT=np.max(ChPeak[:,2])
    ChPeak[0,5]=Integral
    ChPeak[0,12]=min_RT
    ChPeak[0,13]=max_RT
    SummaryChPeak=ChPeak[0,:]
    return SummaryChPeak

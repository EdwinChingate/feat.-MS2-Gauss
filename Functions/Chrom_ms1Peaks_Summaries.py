from MaxIntChromatogram import *
from ResolvingChromatogram import *
from Summarize_ms1_ChPeak import *
from Feat_RT_edges import *
def Chrom_ms1Peaks_Summaries(mz,mz_std,DataSet,DataSetName,MS1IDVec,AllPeaks,minIntFrac=1,int_col=1,RT_col=2,BaseLinePoints_2=3,LogFileName='LogFile_ms1.csv',stdDistance=1,minSignals=5,MaxCount=3,minInt=1e3,Points_for_regression=4,alpha=0.01,minSpec=10):
    Chromatogram=MaxIntChromatogram(mz=mz,mz_std=mz_std,AllPeaks=AllPeaks,stdDistance=stdDistance)    
    Chromatogram=Chromatogram[Chromatogram[:,RT_col].argsort(),:].copy()
    #ChrMat=ResolvingChromatogram(Chromatogram=Chromatogram,minSpec=minSpec,int_col=int_col)
    ChrMat=Feat_RT_edges(Chromatogram=Chromatogram,minSpec=minSpec,int_col=int_col,stdDistance=3,NoiseCluster=False)
    #ShowDF(ChrMat)
    if len(ChrMat)==0:
        return []
    min_mz=mz-mz_std*stdDistance
    max_mz=mz+mz_std*stdDistance
    SummarizeChFeat=[]
    for sig in ChrMat:
        EarlyLoc=int(sig[0])
        LateLoc=int(sig[1])
        SummaryChPeak=Summarize_ms1_ChPeak(EarlyLoc=EarlyLoc,LateLoc=LateLoc,minIntFrac=minIntFrac,Chromatogram=Chromatogram,int_col=int_col,RT_col=RT_col,BaseLinePoints_2=BaseLinePoints_2)
        SummaryPeak=[mz]+[mz_std]+[min_mz]+[max_mz]+SummaryChPeak
        SummarizeChFeat.append(SummaryPeak)
    return SummarizeChFeat

import numpy as np
from RetrieveChromatogram import *
from Feat_RT_edges import *
from SummarizeChPeak import *
def ModuleChromSummaries(mz,mz_std,DataSet,DataSetName,MS1IDVec,BaseLinePoints_2=3,LogFileName='LogFile_ms1.csv',stdDistance=3,minSignals=5,MaxCount=3,minInt=1e3,Points_for_regression=4,alpha=0.01,minSpec=10):
    Chromatogram=RetrieveChromatogram(mz=mz,mz_std=mz_std,DataSet=DataSet,DataSetName=DataSetName,MS1IDVec=MS1IDVec,LogFileName=LogFileName,stdDistance=stdDistance,minSignals=minSignals,MaxCount=MaxCount,minInt=minInt,Points_for_regression=Points_for_regression,alpha=alpha)
    ChrPeakMat=Feat_RT_edges(Chromatogram=Chromatogram,minSpec=minSpec)
    SummarizeChFeat=[]
    for sig in ChrPeakMat:
        EarlyLoc=int(sig[0])
        LateLoc=int(sig[1])
        SummaryChPeak=SummarizeChPeak(EarlyLoc=EarlyLoc,LateLoc=LateLoc,Chromatogram=Chromatogram,BaseLinePoints_2=BaseLinePoints_2)
        SummarizeChFeat.append(SummaryChPeak)
    SummarizeChFeat=np.array(SummarizeChFeat)
    return SummarizeChFeat

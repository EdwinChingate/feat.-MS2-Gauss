import numpy as np
from ResolveChromPeaks import *
from ExtractAllRawPeaks import *
def Match_Feature_O2O_Chrom(AlignedSamplesDF,MS1IDVec,DataSet,ms2_feature_id,RT_tol=5,mz_Tol=1,RT_window=30):
    mz=AlignedSamplesDF['AverageMZ_1'][ms2_feature_id]
    mz_std=AlignedSamplesDF['StdMZ_1'][ms2_feature_id]
    RT=AlignedSamplesDF["AverageRT_1"][ms2_feature_id]*60
    min_mz=mz-mz_Tol
    max_mz=mz+mz_Tol
    min_RT=RT-RT_window 
    max_RT=RT+RT_window
    AllRawPeaks=ExtractAllRawPeaks(MS1IDVec=MS1IDVec,DataSet=DataSet,height=1e2,distance=2,min_RT=min_RT,max_RT=max_RT,min_mz=min_mz,max_mz=max_mz)
    AllChromPeaksMat=ResolveChromPeaks(mz=mz,mz_std=mz_std,AllRawPeaks=AllRawPeaks,stdDistance=3,RT_tol=5,minSignals=5,mz_name='mz',ChromPoints=100,prominence=5,distance=5)
    if len(AllChromPeaksMat)==0:
        return [0,0]
    PeaksLoc=(AllChromPeaksMat[:,1]<RT)&(AllChromPeaksMat[:,2]>RT)
    if len(AllChromPeaksMat[PeaksLoc,:])==0:
        return [0,0]
    elif len (AllChromPeaksMat[PeaksLoc,:])==1:
        Closest_RTPeak=AllChromPeaksMat[PeaksLoc,0][0]
        ChosenPeakInt=AllChromPeaksMat[PeaksLoc,3][0]
    else:
        RT_vec=np.abs(AllChromPeaksMat[PeaksLoc,0]-RT)
        Closest_RT=np.min(RT_vec)
        Closest_RT_Loc=np.where(RT_vec==Closest_RT)[0][0]
        ChosenPeakInt=AllChromPeaksMat[PeaksLoc,:][Closest_RT_Loc,3]
        Closest_RTPeak=AllChromPeaksMat[PeaksLoc,:][Closest_RT_Loc,0]
    return [Closest_RTPeak,ChosenPeakInt]

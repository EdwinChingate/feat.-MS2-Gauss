import numpy as np
from ResolveChromPeaks import *
def Match_ms2Feature_Chrom(CarbonSourceFeatures_RT,AllRawPeaks,sample_id,ms2_feature_id,RT_tol):
    mz=CarbonSourceFeatures_RT['mz_(Da)'][ms2_feature_id]
    mz_std=CarbonSourceFeatures_RT['mz_std_(Da)'][ms2_feature_id]
    RT=CarbonSourceFeatures_RT[sample_id][ms2_feature_id]
    AllChromPeaksMat=ResolveChromPeaks(mz=mz,mz_std=mz_std,AllRawPeaks=AllRawPeaks,stdDistance=3,RT_tol=5,minSignals=5,mz_name='mz',ChromPoints=100,prominence=5,distance=5)
    if len (AllChromPeaksMat)==0:
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

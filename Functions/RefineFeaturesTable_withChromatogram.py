import numpy as np
from ExtractAllRawPeaks import *
from ChargeDataSet_in_AnotherFolder import *
from MS_L_IDs import *
from Match_ms2Feature_Chrom import *
from RT_Predictor import *
def RefineFeaturesTable_withChromatogram(CarbonSourceFeatures,CarbonSourceFeatures_RT,ToAdd='.mzML',DataFolder='/home/edwin/Documents/16.02/data',mz_tol=5,RT_tol=5):
    CarbonSourceFeatures_RT=RT_Predictor(CarbonSourceFeatures_RT)
    CarbonSourceFeatures=CarbonSourceFeatures.sort_values(by=['RT_(s)'])
    SamplesIds=CarbonSourceFeatures_RT.columns[7:]
    min_RT=np.min(CarbonSourceFeatures['min_RT_(s)'])-RT_tol
    max_RT=np.max(CarbonSourceFeatures['max_RT_(s)'])+RT_tol
    min_mz=np.min(CarbonSourceFeatures['mz_(Da)'])-mz_tol
    max_mz=np.max(CarbonSourceFeatures['mz_(Da)'])+mz_tol
    for sample_id in SamplesIds:    
        sampleName=sample_id+ToAdd    
        DataSet=ChargeDataSet_in_AnotherFolder(DataSetName=sampleName,DataFolder=DataFolder)
        MS1IDVec=MS_L_IDs(DataSet=DataSet,Level=1,min_RT=min_RT,max_RT=max_RT)
        AllRawPeaks=ExtractAllRawPeaks(MS1IDVec=MS1IDVec,DataSet=DataSet,height=1e2,distance=2,min_RT=min_RT,max_RT=max_RT,min_mz=min_mz,max_mz=max_mz)
        ms2FeaturesList=list(CarbonSourceFeatures.index)
        for ms2_feature_id in ms2FeaturesList:        
            Closest_RT,ChosenPeakInt=Match_ms2Feature_Chrom(CarbonSourceFeatures_RT=CarbonSourceFeatures_RT.copy(),AllRawPeaks=AllRawPeaks.copy(),sample_id=sample_id,ms2_feature_id=ms2_feature_id,RT_tol=RT_tol)
            CarbonSourceFeatures_RT[sample_id][ms2_feature_id]=Closest_RT
            CarbonSourceFeatures[sample_id][ms2_feature_id]=ChosenPeakInt
    return [CarbonSourceFeatures,CarbonSourceFeatures_RT]

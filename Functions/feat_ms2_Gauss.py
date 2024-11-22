import numpy as np
from ms2_features_stats import *
from Cluster_ms2_Features import *
def feat_ms2_Gauss(DataSet,SummMS2,MS1IDVec,mz_std=2e-3,MS2_to_MS1_ratio=10,stdDistance=3,MaxCount=3,Points_for_regression=5,minSignals=7):
    MS2_features=[]
    N_MS2_features=len(SummMS2[:,0])
    for MS2_id in np.arange(N_MS2_features,dtype='int'):         
        while True:
            try:
                features_stats=ms2_features_stats(DataSet=DataSet,MS2_id=MS2_id,SummMS2=SummMS2,MS1IDVec=MS1IDVec,mz_std=mz_std,MS2_to_MS1_ratio=MS2_to_MS1_ratio,stdDistance=stdDistance,MaxCount=MaxCount,Points_for_regression=Points_for_regression,minSignals=minSignals)
                if len(features_stats)>0:
                    MS2_features.append(features_stats)                
                break
            except:
                print('error',MS2_id)
                break
    MS2_features=np.array(MS2_features)
    MS2_features=MS2_features[MS2_features[:,3].argsort(),:]
    ms2_featuresDF=Cluster_ms2_Features(MS2_features)
    return ms2_featuresDF

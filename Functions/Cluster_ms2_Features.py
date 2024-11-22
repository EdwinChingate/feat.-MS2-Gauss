import numpy as np
import pandas as pd
def Cluster_ms2_Features(MS2_features):
    N_feat=len(MS2_features[:,0])
    ConfidenceInterval_OverlapVec=np.where(MS2_features[:-1,3]+MS2_features[:-1,4]<MS2_features[1:,3]-MS2_features[:-1,4])[0]+1
    ConfidenceInterval_OverlapVec=np.append(ConfidenceInterval_OverlapVec,N_feat)
    Lower_feat_id=0
    All_IDsList=[]
    FirstFeat=True
    for Higher_feat_id in ConfidenceInterval_OverlapVec:
        MS2_feature=MS2_features[Lower_feat_id:Higher_feat_id,:].copy()
        MS2_feature=MS2_feature[(-MS2_feature[:,5]).argsort(),:]
        MS2_vec=list(MS2_feature[:,0])
        MS1_vec=list(MS2_feature[:,1])
        N_spec=len(MS1_vec)
        min_RT=np.min(MS2_feature[:,2])
        max_RT=np.max(MS2_feature[:,2])    
        All_IDsList.append([min_RT,max_RT,N_spec,MS2_vec,MS1_vec])    
        Lower_feat_id=Higher_feat_id
        if FirstFeat:
            ms2_featuresTable=MS2_feature[[0,0],:]
            FirstFeat=False
        else:
            ms2_featuresTable=np.insert(ms2_featuresTable,-1,MS2_feature[0,:],axis=0)
    FeaturesColumns=["ms2_id",
                    "ms1_id",
                    "RT_(s)",
                    "mz_(Da)",
                    "mz_std_(Da)",
                    "I_tol_1spec",
                    "Gauss_r2",
                    "N_points_1spec",
                    "ConfidenceInterval_(Da)",
                    "ConfidenceInterval_(ppm)",
                    "min_mz_(Da)",
                    "max_mz_(Da)"]
    IDsColumns=["min_RT_(s)",
               "max_RT_(s)",
               "N_spec",
               "ms2_ids",
               "ms1_ids"]
    ms2_featuresDF=pd.DataFrame(ms2_featuresTable[:-1,:],columns=FeaturesColumns)    
    ms2_featuresDF[IDsColumns]=pd.DataFrame(All_IDsList,dtype='object')
    return ms2_featuresDF

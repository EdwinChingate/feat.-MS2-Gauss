import numpy as np
def AdjacencyList_mz(MS2_features,mz_col=3,mz_CI_col=8,mz_Tol=0,stdDistance=3):
    N_possible_feat=len(MS2_features[:,0])
    if mz_Tol==0:
        mz_CI_Vec=MS2_features[:,mz_CI_col]
    else:
        mz_CI_Vec=np.ones(N_possible_feat)*mz_Tol
    mzVec=MS2_features[:,mz_col]
    mzMaxVec=mzVec+mz_CI_Vec*stdDistance
    mzMinVec=mzVec-mz_CI_Vec*stdDistance
    AdjacencyList=[]
    feat_ids=[]
    for feat_id in np.arange(N_possible_feat):
        min_mz=mzMinVec[feat_id]
        max_mz=mzMaxVec[feat_id]       
        NearFilter=(mzMaxVec>=min_mz)&(mzMinVec<=max_mz)
        Neigbours=np.where(NearFilter)[0]    
        AdjacencyList.append(Neigbours)
        if len(Neigbours)>0:
            feat_ids.append(feat_id)
    feat_ids=set(feat_ids)
    return [AdjacencyList,feat_ids]

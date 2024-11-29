import numpy as np
def AdjacencyListFeatures(MS2_features,RT_tol=0):
    N_possible_feat=len(MS2_features[:,0])
    mzMaxVec=MS2_features[:,3]+MS2_features[:,8]
    mzMinVec=MS2_features[:,3]-MS2_features[:,8]
    if RT_tol==0:
        RTMaxVec=MS2_features[:,13]
        RTMinVec=MS2_features[:,12]
    else:
        RTMaxVec=MS2_features[:,2]+RT_tol
        RTMinVec=MS2_features[:,2]-RT_tol
    AdjacencyList=[]
    feat_ids=[]
    for feat_id in np.arange(N_possible_feat):
        mz=MS2_features[feat_id,3]
        mz_CI=MS2_features[feat_id,8]
        min_mz=mz-mz_CI
        max_mz=mz+mz_CI
        min_RT=RTMinVec[feat_id]
        max_RT=RTMaxVec[feat_id]
        if RT_tol==0:
            min_RT=MS2_features[feat_id,12]
            max_RT=MS2_features[feat_id,13]
        else:
            min_RT=MS2_features[feat_id,2]-RT_tol
            max_RT=MS2_features[feat_id,2]+RT_tol            
        NearFilter=(mzMaxVec>min_mz)&(mzMinVec<max_mz)&(RTMaxVec>min_RT)&(RTMinVec<max_RT)
        Neigbours=np.where(NearFilter)[0]    
        AdjacencyList.append(Neigbours)
        if len(Neigbours)>0:
            feat_ids.append(feat_id)
    feat_ids=set(feat_ids)
    return [AdjacencyList,feat_ids]

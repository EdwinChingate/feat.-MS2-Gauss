import numpy as np
def AdjacencyList_ms2Fragments(All_ms2):
    N_fragments=len(All_ms2[:,0])
    mzMaxVec=All_ms2[:,0]+All_ms2[:,5]
    mzMinVec=All_ms2[:,0]-All_ms2[:,5]
    AdjacencyList=[]
    frag_ids=[]
    for feat_id in np.arange(N_fragments):
        mz=All_ms2[feat_id,0]
        mz_CI=All_ms2[feat_id,5]
        min_mz=mz-mz_CI
        max_mz=mz+mz_CI        
        NearFilter=(mzMaxVec>min_mz)&(mzMinVec<max_mz)
        Neigbours=np.where(NearFilter)[0]    
        AdjacencyList.append(Neigbours)
        if len(Neigbours)>0:
            frag_ids.append(feat_id)
    frag_ids=set(frag_ids)
    return [AdjacencyList,frag_ids]

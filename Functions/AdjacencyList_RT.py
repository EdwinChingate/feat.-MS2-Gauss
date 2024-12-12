import numpy as np
def AdjacencyList_RT(ChromPeaks,RT_col=3,RT_CI_col=8,RT_Tol=0,stdDistance=3):
    N_signals=len(ChromPeaks[:,0])
    if RT_Tol==0:
        RT_CI_Vec=ChromPeaks[:,RT_CI_col]
    else:
        RT_CI_Vec=np.ones(N_signals)*RT_Tol
    RTVec=ChromPeaks[:,RT_col]
    RTMaxVec=RTVec+RT_CI_Vec*stdDistance
    RTMinVec=RTVec-RT_CI_Vec*stdDistance
    AdjacencyList=[]
    peak_ids=[]
    for peak_id in np.arange(N_signals):
        min_RT=RTMinVec[peak_id]
        max_RT=RTMaxVec[peak_id]       
        NearFilter=(RTMaxVec>=min_RT)&(RTMinVec<=max_RT)
        Neigbours=np.where(NearFilter)[0]    
        AdjacencyList.append(Neigbours)
        if len(Neigbours)>0:
            peak_ids.append(peak_id)
    peak_ids=set(peak_ids)
    return [AdjacencyList,peak_ids]

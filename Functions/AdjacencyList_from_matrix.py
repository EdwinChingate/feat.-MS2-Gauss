import numpy as np
def AdjacencyList_from_matrix(AdjacencyMatrix,N_ms2_spectra):
    AdjacencyList=[]
    ms2_ids=[]
    for ms2_candidate_id in np.arange(N_ms2_spectra,dtype='int'):
        Neigbours=np.where(AdjacencyMatrix[ms2_candidate_id,:]>0)[0]
        if len(Neigbours)>0:
            ms2_ids.append(ms2_candidate_id)
        AdjacencyList.append(Neigbours)
    ms2_ids=set(ms2_ids) 
    return [AdjacencyList,ms2_ids]

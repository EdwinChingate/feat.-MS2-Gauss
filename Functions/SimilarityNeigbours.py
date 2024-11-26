import numpy as np
from CheckNeigbours import *
def SimilarityNeigbours(SpectraList,AdjacencyMatrix,SummMS2,ms2_candidate_id1,RT_tol=30,cos_tol=0.95,Tanimoto_tol=0.6,mz_maxDif=1e-2,min_Int_Frac=5):
    mz=SummMS2[ms2_candidate_id1,0]
    RT=SummMS2[ms2_candidate_id1,1]
    min_RT=RT-RT_tol
    max_RT=RT+RT_tol    
    max_mz_peak=mz+mz_maxDif
    min_mz_peak=mz-mz_maxDif
    mz_NearFilter=(SummMS2[:,0]<max_mz_peak)&(SummMS2[:,0]>mz)&(SummMS2[:,1]>min_RT)&(SummMS2[:,1]<max_RT)
    Neigbours=np.where(mz_NearFilter)[0]
    Spectrum_1=SpectraList[ms2_candidate_id1] 
    if len(Spectrum_1)==0:
        AdjacencyMatrix[ms2_candidate_id1,ms2_candidate_id1]=0
    AdjacencyMatrix=CheckNeigbours(ms2_candidate_id1=ms2_candidate_id1,AdjacencyMatrix=AdjacencyMatrix,Spectrum_1=Spectrum_1,SpectraList=SpectraList,Neigbours=Neigbours,min_Int_Frac=min_Int_Frac,Tanimoto_tol=Tanimoto_tol,cos_tol=cos_tol)
    return AdjacencyMatrix

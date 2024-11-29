import numpy as np
from Similarity_AdjacencyMatrix import *
from AdjacencyList_from_matrix import *
from ms2_feat_modules import *
def ms2_SpectralRendundancy(SpectraList,SummMS2,RT_tol=30,cos_tol=0.95,Tanimoto_tol=0.6,mz_maxDif=1e-2,min_Int_Frac=5):
    AdjacencyMatrix=Similarity_AdjacencyMatrix(SpectraList=SpectraList,SummMS2=SummMS2,RT_tol=RT_tol,cos_tol=cos_tol,Tanimoto_tol=Tanimoto_tol,mz_maxDif=mz_maxDif,min_Int_Frac=min_Int_Frac)
    N_ms2_spectra=len(SummMS2[:,0])
    AdjacencyList,ms2_ids=AdjacencyList_from_matrix(AdjacencyMatrix,N_ms2_spectra)
    Modules=ms2_feat_modules(AdjacencyList=AdjacencyList,ms2_ids=ms2_ids)
    N_modules=len(Modules)
    NonRedundant_SummMS2=[]
    for mod_p in np.arange(N_modules,dtype='int'):
        mod=Modules[mod_p]
        mod_loc=0
        SummMS2_mod=SummMS2[mod,:].copy()
        min_RT=np.min(SummMS2_mod[:,1])
        max_RT=np.max(SummMS2_mod[:,1])
        N_spec=len(mod)
        if N_spec>1:
            mostInt_ms2Frag=np.max(SummMS2_mod[:,3])
            mostInt_ms2Frag_Filter=SummMS2_mod[:,3]==mostInt_ms2Frag
            mod_loc=int(np.where(mostInt_ms2Frag_Filter)[0])            
        SummMS2_mod=list(SummMS2_mod[mod_loc,:])
        ms2_spec_id=mod[mod_loc]
        SummMS2_mod=SummMS2_mod+[min_RT]+[max_RT]+[N_spec]+[ms2_spec_id]
        NonRedundant_SummMS2.append(SummMS2_mod)
    NonRedundant_SummMS2=np.array(NonRedundant_SummMS2)
    return NonRedundant_SummMS2

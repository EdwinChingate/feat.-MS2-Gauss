from GoodNeigbour import *
def CheckNeigbours(ms2_candidate_id1,AdjacencyMatrix,Spectrum_1,SpectraList,Neigbours,Tanimoto_tol,cos_tol,min_Int_Frac=5):
    for ms2_candidate_id2 in Neigbours:        
        Spectrum_2=SpectraList[ms2_candidate_id2]
        if (len(Spectrum_1)>0)and((len(Spectrum_2)>0)):        
            AdjacencyMatrix=GoodNeigbour(ms2_candidate_id1=ms2_candidate_id1,ms2_candidate_id2=ms2_candidate_id2,AdjacencyMatrix=AdjacencyMatrix,Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2,min_Int_Frac=min_Int_Frac,Tanimoto_tol=Tanimoto_tol,cos_tol=cos_tol)
    return AdjacencyMatrix

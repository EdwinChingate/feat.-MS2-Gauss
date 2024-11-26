from Similarity_2Spectra import *
def GoodNeigbour(ms2_candidate_id1,ms2_candidate_id2,AdjacencyMatrix,Spectrum_1,Spectrum_2,min_Int_Frac,Tanimoto_tol,cos_tol):
    Cosine,TanimotoSim=Similarity_2Spectra(Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2,min_Int_Frac=min_Int_Frac)
    if Cosine>cos_tol and TanimotoSim>Tanimoto_tol:
        AdjacencyMatrix[ms2_candidate_id1,ms2_candidate_id2]=1
        AdjacencyMatrix[ms2_candidate_id2,ms2_candidate_id1]=1
    return AdjacencyMatrix

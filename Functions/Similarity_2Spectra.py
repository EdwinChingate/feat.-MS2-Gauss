from SpectralOrder import *
from AlignSpectra import *
from Cosine_2VecSpec import *
def Similarity_2Spectra(Spectrum_1,Spectrum_2,min_Int_Frac=2):
    Spectrum_1,Spectrum_2,L_spec1,L_spec2=SpectralOrder(Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2,min_Int_Frac=min_Int_Frac)    
    if len(Spectrum_1)==0 or len(Spectrum_2)==0:
        return [0,0]
    AlignedSpecMat,TanimotoSim,AlignedSpec_Inf=AlignSpectra(Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2,L_spec1=L_spec1,L_spec2=L_spec2)
    Cosine=Cosine_2VecSpec(AlignedSpecMat=AlignedSpecMat)
    return [Cosine,TanimotoSim]

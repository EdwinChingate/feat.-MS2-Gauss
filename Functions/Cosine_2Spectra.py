from SpectralOrder import *
from AlignSpectra import *
from Cosine_2VecSpec import *
def Cosine_2Spectra(Spectrum_1,Spectrum_2):
    Spectrum_1,Spectrum_2,L_spec1,L_spec2=SpectralOrder(Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2)    
    AlignedSpecMat=AlignSpectra(Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2,L_spec1=L_spec1,L_spec2=L_spec2)
    Cosine=Cosine_2VecSpec(AlignedSpecMat=AlignedSpecMat)
    return Cosine

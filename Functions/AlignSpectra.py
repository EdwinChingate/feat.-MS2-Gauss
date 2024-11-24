import numpy as np
from OverlpaingPeaks import *
def AlignSpectra(Spectrum_1,Spectrum_2,L_spec1,L_spec2):
    UniquePeaks_1=np.arange(L_spec1)
    UniquePeaks_2=np.arange(L_spec2)
    SharedPeaks_1,SharedPeaks_2,UniquePeaks_2=OverlpaingPeaks(Spectrum_1=Spectrum_1,Spectrum_2=Spectrum_2,UniquePeaks_2=UniquePeaks_2)    
    N_sharedpeaks=len(SharedPeaks_2)
    N_UniquePeaks_2=L_spec2-N_sharedpeaks
    N_AllPeaks=L_spec1+N_UniquePeaks_2    
    AlignedSpecMat=np.zeros((N_AllPeaks,3))  
    AlignedSpecMat[UniquePeaks_1,:2]=Spectrum_1[:,[0,2]]
    AlignedSpecMat[SharedPeaks_1,2]=Spectrum_2[SharedPeaks_2,2]
    AlignedSpecMat[-N_UniquePeaks_2:,0]=Spectrum_2[UniquePeaks_2,0]
    AlignedSpecMat[-N_UniquePeaks_2:,2]=Spectrum_2[UniquePeaks_2,2]
    return AlignedSpecMat

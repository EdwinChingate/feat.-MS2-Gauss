import numpy as np
from GaussianPeak import *
def r2_Gauss(PeakData,GaussianParameters):
    mz=GaussianParameters[0]
    mz_std=GaussianParameters[1]
    I_total=GaussianParameters[2]    
    Gaussian_Int=GaussianPeak(PeakData[:,0],mz,mz_std,I_total)
    I_mean=np.mean(PeakData[:,1])
    SS_tot=np.sum((PeakData[:,1]-I_mean)**2)
    SS_res=np.sum((Gaussian_Int-PeakData[:,1])**2)
    r2=1-SS_res/SS_tot
    return [r2]

import numpy as np
def GaussianPeak(mz_vec,mz,mz_std,I_total):
    LogVec=-((mz_vec-mz)/mz_std)**2/2
    f1_sqrt2pi=0.3989422804014327 #1/np.sqrt(np.pi*2) 
    Gaussian_Int=np.exp(LogVec)*f1_sqrt2pi*I_total/mz_std
    return Gaussian_Int

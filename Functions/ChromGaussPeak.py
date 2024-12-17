import numpy as np
#I need to remove the background parameter
def ChromGaussPeak(RT_vec,RT,RT_std,Integral,BG):
    LogVec=-((RT_vec-RT)/RT_std)**2/2
    f1_sqrt2pi=0.3989422804014327 #1/np.sqrt(np.pi*2) 
    Gaussian_Int=BG+np.exp(LogVec)*f1_sqrt2pi*Integral/RT_std
    return Gaussian_Int    

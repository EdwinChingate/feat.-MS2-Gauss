import numpy as np
from ChromGaussPeak import *
def OverlappingGaussPeaks(RT_vec,ParametersList):
    NPeaks=int(len(ParametersList))
    NPoints=len(RT_vec)
    ChromatogramMatrix=np.zeros((NPoints,NPeaks))
    for peak_id in np.arange(NPeaks):      
        RT,RT_std,Integral=ParametersList[peak_id]
        ChromatogramMatrix[:,peak_id]=ChromGaussPeak(RT_vec,RT,RT_std,Integral)
    OverlapGaussInt=sum(ChromatogramMatrix.T)
    return ChromatogramMatrix

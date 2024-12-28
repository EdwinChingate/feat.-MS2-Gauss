import numpy as np
from WeightGauss import *
def ParametersFitGaussPeaks(RT_vec,ChromatogramMatrix,boundsMat,ParametersMat,stdDistance=3):
    NPeaks=int(len(ParametersMat[:,0]))
    Integral=boundsMat[2,1]
    ParametersMat_peak=ParametersMat.copy()
    for peak_id in np.arange(NPeaks):            
        Int_vec=ChromatogramMatrix[:,peak_id] 
        GaussianParameters=WeightGauss(RT_vec=RT_vec,Int_vec=Int_vec)
        ParametersMat_peak[peak_id,:]=np.array(GaussianParameters)
    ParametersMat_peak=ParametersMat_peak[ParametersMat_peak[:,0].argsort(),:]
    GaussianIntegral=np.sum(ParametersMat_peak[:,2])
    ParametersMat_peak[:,2]=ParametersMat_peak[:,2]*Integral/GaussianIntegral
    return ParametersMat_peak

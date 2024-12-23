import numpy as np
from PeakChromGauss import *
def ParametersFitGaussPeaks(RT_vec,ChromatogramMatrix,ParametersList):
    NPeaks=int(len(ParametersList))
    RT_max=np.max(RT_vec)
    RT_min=np.min(RT_vec)
    RT_maxDif=RT_max-RT_min    
    GaussianParList=[]
    for peak_id in np.arange(NPeaks):    
        Int_vec=ChromatogramMatrix[:,peak_id]
        RT,RT_std,Integral=ParametersList[peak_id]        
        bounds=([RT_min, 0, 0],[RT_max,RT_maxDif,np.inf])
        GaussianParameters=PeakChromGauss(RT_vec=RT_vec,Int_vec=Int_vec,RT=RT,RT_std=RT_std)
        if len(GaussianParameters)==0:            
            GaussianParameters=ParametersList[peak_id]
        GaussianParList.append(GaussianParameters)
    GaussianParMat=np.array(GaussianParList)
    GaussianParMat=GaussianParMat[GaussianParMat[:,0].argsort(),:]
    return GaussianParMat

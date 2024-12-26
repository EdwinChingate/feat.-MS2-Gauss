import numpy as np
from scipy.optimize import curve_fit
from ChromGaussPeak import *
def ParametersFitGaussPeaks(RT_vec,ChromatogramMatrix,boundsMat,ParametersMat,stdDistance=3):
    NPeaks=int(len(ParametersMat[:,0]))
    RT_min=boundsMat[0,0]
    RT_max=boundsMat[0,1]    
    RT_maxDif=boundsMat[1,1]
    Integral=boundsMat[2,1]
    GaussianParList=[]
    for peak_id in np.arange(NPeaks):    
        Int_vec=ChromatogramMatrix[:,peak_id] 
        RT,RT_std,Integralp=ParametersMat[peak_id,:]        
        bounds=([RT_min+stdDistance*RT_std, 0, 0],[RT_max-stdDistance*RT_std, RT_maxDif,Integral])
        while True:
            try:
                GaussianParameters=list(curve_fit(ChromGaussPeak, xdata=RT_vec, ydata=Int_vec,p0=ParametersMat[peak_id,:],bounds=bounds)[0])
                break
            except:
                GaussianParameters=ParametersMat[peak_id,:]
                break
        GaussianParList.append(GaussianParameters)
    GaussianParMat=np.array(GaussianParList)
    GaussianParMat=GaussianParMat[GaussianParMat[:,0].argsort(),:]
    GaussianIntegral=np.sum(GaussianParMat[:,2])
    GaussianParMat[:,2]=GaussianParMat[:,2]*Integral/GaussianIntegral
    return GaussianParMat

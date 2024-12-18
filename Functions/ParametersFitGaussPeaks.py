import numpy as np
from scipy.optimize import curve_fit
from ChromGaussPeak import *
# I can get the Gaussian Parameters in a way easier way
def ParametersFitGaussPeaks(RT_vec,ChromatogramMatrix,ParametersList,IntegralFrac=0.1,ExtraPeaks=1,Keep_N_Peaks=0):
    NPeaks=int(len(ParametersList))
    RT_max=np.max(RT_vec)
    RT_min=np.min(RT_vec)
    RT_maxDif=RT_max-RT_min    
    GaussianParList=[]
    for peak_id in np.arange(NPeaks):    
        Int_vec=ChromatogramMatrix[:,peak_id]
        RT,RT_std,Integral=ParametersList[peak_id]        
        bounds=([RT_min, 0, 0], [RT_max, RT_maxDif, np.inf])
        while True:
            try:
                GaussianParameters=list(curve_fit(ChromGaussPeak, xdata=RT_vec, ydata=Int_vec,p0=ParametersList[peak_id],bounds=bounds)[0])
                break
            except:
                GaussianParameters=ParametersList[peak_id]
                break
        GaussianParList.append(GaussianParameters)
    GaussianParMat=np.array(GaussianParList)
    GaussianParMat=GaussianParMat[GaussianParMat[:,2].argsort(),:]
    maxIntegral=GaussianParMat[-1,2]
    minIntegral=maxIntegral*IntegralFrac/100
    minIntegralFilter=GaussianParMat[:,2]>minIntegral
    minIntegralLoc=np.where(minIntegralFilter)[0][0]-ExtraPeaks
    if minIntegralLoc<0:
        minIntegralLoc=0
    elif (NPeaks-minIntegralLoc)<Keep_N_Peaks:
        minIntegralLoc=NPeaks-Keep_N_Peaks
    GaussianParList=list(GaussianParMat[minIntegralLoc:,:])
    return GaussianParList

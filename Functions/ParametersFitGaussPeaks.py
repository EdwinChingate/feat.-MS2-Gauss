import numpy as np
from scipy.optimize import curve_fit
from ChromGaussPeak import *
def ParametersFitGaussPeaks(Chromatogram,ParametersList,RT_col=2,int_col=1):
    NPeaks=int(len(ParametersList))
    RT_vec=Chromatogram[:,RT_col]
    RT_max=np.max(RT_vec)
    RT_min=np.min(RT_vec)
    RT_maxDif=RT_max-RT_min
    Int_vec=Chromatogram[:,int_col].copy()
    GaussianParList=[]
    for peak_id in np.arange(NPeaks):      
        RT,RT_std,Integral=ParametersList[peak_id]        
        bounds=([RT_min, 0, 0], [RT_max, RT_maxDif, np.inf])
        GaussianParameters=list(curve_fit(ChromGaussPeak, xdata=RT_vec, ydata=Int_vec,p0=ParametersList[peak_id],bounds=bounds)[0])
        RT,RT_std,Integral=GaussianParameters        
        Gaussian_Int=ChromGaussPeak(RT_vec,RT,RT_std,Integral)
        Int_vec=Int_vec-Gaussian_Int
        GaussianParList.append(GaussianParameters)
    return GaussianParList

from scipy.optimize import curve_fit
from GaussianChromatogram import *
from ToolsGaussianChrom import *
def ResolvingGaussianChromatogram(Chromatogram,RT_col=2,int_col=1,MaxSignals=100,distance=2):
    SChrom,ParametersList,bounds=ToolsGaussianChrom(Chromatogram=Chromatogram,RT_col=RT_col,int_col=int_col,MaxSignals=MaxSignals,distance=distance)
    if len(SChrom)==0:
        return []
    RT_vec=SChrom[:,0]
    Int_vec=SChrom[:,1]
    GaussianParametersList=list(curve_fit(GaussianChromatogram, xdata=RT_vec, ydata=Int_vec,p0=ParametersList,bounds=bounds)[0])
    NPeaks=int(len(GaussianParametersList)/3)
    GaussianParameters=np.array(GaussianParametersList).reshape(NPeaks, 3)
    return GaussianParameters

from scipy.optimize import curve_fit
from GaussianPeak import *
from r2_Gauss import *
def Normal_Fit(PeakData_and_Stats):
    PeakData=PeakData_and_Stats[0]
    GaussStats=PeakData_and_Stats[1]    
    mz=GaussStats[0]
    mz_std=GaussStats[1]
    I_total=GaussStats[4]
    GaussianParameters=list(curve_fit(GaussianPeak, xdata=PeakData[:,0], ydata=PeakData[:,1],p0=[mz,mz_std,I_total])[0])
    r2=r2_Gauss(PeakData,GaussianParameters)
    NormalParameters=GaussianParameters+r2
    return NormalParameters

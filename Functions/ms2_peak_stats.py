from scipy import stats
from ms2Peak import *
from Normal_Fit import *
def ms2_peak_stats(RawSpectrum,mz,mz_std=2e-3,stdDistance=3,minSignals=5,MaxCount=3,minInt=1e3,Points_for_regression=4,alpha=0.01):
    PeakData_and_Stats=ms2Peak(RawSpectrum=RawSpectrum,mz=mz,mz_std=mz_std,stdDistance=stdDistance,minSignals=minSignals,MaxCount=MaxCount,minInt=minInt,Points_for_regression=Points_for_regression)
    if len(PeakData_and_Stats)==0:
        return []
    NormalParameters=Normal_Fit(PeakData_and_Stats=PeakData_and_Stats)
    Nsignals=len(PeakData_and_Stats[0][:,0])
    PeakData=PeakData_and_Stats[0]
    mz=NormalParameters[0]
    mz_std=NormalParameters[1]
    min_mz=[np.min(PeakData[:,0])]
    max_mz=[np.max(PeakData[:,0])]
    tref=stats.t.interval(1-alpha, Nsignals-1)[1]    
    ConfidenceIntervalDa=[tref*mz_std/np.sqrt(Nsignals)]
    ConfidenceInterval=[tref*mz_std/np.sqrt(Nsignals)/mz*1e6]
    peak_stats=NormalParameters+[Nsignals]+ConfidenceIntervalDa+ConfidenceInterval+min_mz+max_mz    
    return peak_stats

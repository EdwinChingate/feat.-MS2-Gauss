import numpy as np
def Find_ms2Peak(RawSpectrum,mz,mz_std=2e-3,stdDistance=3,minSignals=4,count=0,MaxCount=3,minInt=1e3,RelativeContribution=False):
    if count==MaxCount:
        return []
    min_mz_peak=mz-mz_std*stdDistance
    max_mz_peak=mz+mz_std*stdDistance
    peakFilter=(RawSpectrum[:,0]>min_mz_peak)&(RawSpectrum[:,0]<max_mz_peak)&(RawSpectrum[:,1]>0)
    PeakData=RawSpectrum[peakFilter,:]            
    if RelativeContribution:
        PeakInt=sum(PeakData[:,1])
        TotalInt=sum(RawSpectrum[:,1])
        relative_contribution=[int(PeakInt/TotalInt*100)]
    if (len(PeakData[:,0])<minSignals) and (count<MaxCount):
        PeakData=Find_ms2Peak(RawSpectrum=RawSpectrum,mz=mz,mz_std=mz_std,stdDistance=stdDistance+1,count=count+1,minInt=minInt,minSignals=minSignals)        
    return PeakData

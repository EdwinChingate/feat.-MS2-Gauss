import numpy as np
from ms2_peakStats_safe import *
def ms2_spectrum(RawSpectrum,DataSetName,ms_id,LogFileName,mz_std=2e-3,stdDistance=3,minQuality=40,minInt=1e3,minSignals=5,MaxCount=3,Points_for_regression=4,minPeaks=3): 
    RawSpectrum=RawSpectrum[RawSpectrum[:,1]>0,:]
    TotalInt=sum(RawSpectrum[:,1])
    if len(RawSpectrum[:,0])<minSignals:
        return []    
    Spectrum=[]
    while True:
        maxInt=np.max(RawSpectrum[:,1])    
        if maxInt<minInt:
            break
        maxIntLoc=RawSpectrum[:,1]==maxInt
        mz_maxInt=RawSpectrum[maxIntLoc,0][0]
        peak_stats=ms2_peakStats_safe(RawSpectrum=RawSpectrum,DataSetName=DataSetName,ms_id=ms_id,mz=mz_maxInt,LogFileName=LogFileName,TotalInt=TotalInt,mz_std=mz_std,stdDistance=stdDistance,minSignals=minSignals,MaxCount=MaxCount,minInt=minInt,Points_for_regression=Points_for_regression)
        if len(peak_stats)>0:        
            min_mz_peak=peak_stats[7]
            max_mz_peak=peak_stats[8]
            Spectrum.append(peak_stats)      
        else:
            min_mz_peak=mz_maxInt-mz_std*stdDistance
            max_mz_peak=mz_maxInt+mz_std*stdDistance
        Latest_peakFilter=(RawSpectrum[:,0]<min_mz_peak)|(RawSpectrum[:,0]>max_mz_peak)       
        RawSpectrum=RawSpectrum[Latest_peakFilter,:]                  
        if len(RawSpectrum[:,0])<minSignals:
            break    
    if len(Spectrum)<minPeaks:
        return []
    Spectrum=np.array(Spectrum)    
    QualityFilter=Spectrum[:,6]<minQuality
    Spectrum=Spectrum[QualityFilter,:]
    Spectrum=Spectrum[Spectrum[:,0].argsort(),:]
    return Spectrum

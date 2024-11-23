from ms2_peak_stats import *
from WriteLog import *
def ms2_peakStats_safe(RawSpectrum,DataSetName,ms_id,mz,TotalInt,LogFileName,mz_std=2e-3,stdDistance=3,minSignals=5,MaxCount=3,minInt=1e3,Points_for_regression=4,alpha=0.01):
    while True:
        try:   
            peak_stats=ms2_peak_stats(RawSpectrum=RawSpectrum,mz=mz,mz_std=mz_std,stdDistance=stdDistance,minSignals=minSignals,MaxCount=MaxCount,minInt=minInt,Points_for_regression=Points_for_regression)
            return peak_stats
        except:         
            Parameters=[DataSetName,ms_id,mz,mz_std,stdDistance,minSignals,MaxCount,minInt,Points_for_regression,alpha]
            WriteLog(RawSpectrum=RawSpectrum,Parameters=Parameters,TotalInt=TotalInt,LogFileName=LogFileName)
            return []        

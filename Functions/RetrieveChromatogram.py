import numpy as np
from ms2_peakStats_safe import *
def RetrieveChromatogram(mz,mz_std,DataSet,MS1IDVec,LogFileName='LogFile_ms1.csv',stdDistance=3,minSignals=5,MaxCount=3,minInt=1e3,Points_for_regression=4,alpha=0.01):
    Chromatogram=[]
    N_ms1=len(MS1IDVec[:,0])
    for ms1_id in np.arange(N_ms1,dtype='int'):
        spectrum_id=MS1IDVec[ms1_id,0]
        RT=MS1IDVec[ms1_id,1]
        SpectralSignals=DataSet[int(spectrum_id)]
        RawSpectrum=np.array(SpectralSignals.get_peaks()).T
        TotalInt=np.sum(RawSpectrum[:,1])
        peak_stats=ms2_peakStats_safe(RawSpectrum=RawSpectrum,DataSetName=DataSetName,ms_id=spectrum_id,TotalInt=TotalInt,LogFileName=LogFileName,mz=mz,mz_std=mz_std,stdDistance=stdDistance,minSignals=minSignals,MaxCount=MaxCount,minInt=minInt,Points_for_regression=Points_for_regression,alpha=alpha)
        if len(peak_stats)>0:
            peak_stats=peak_stats+[RT]
            Chromatogram.append(peak_stats)
    Chromatogram=np.array(Chromatogram)
    return Chromatogram

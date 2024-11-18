import numpy as np
def Find_mzPeak(DataSet,spectrum_id,mz,mz_std=2e-3,stdDistance=3,minSignals=7,count=0,MaxCount=3,minInt=1e3):
    SpectralSignals=DataSet[int(spectrum_id)]
    spectrum=np.array(SpectralSignals.get_peaks()).T
    min_mz_peak=mz-mz_std*stdDistance
    max_mz_peak=mz+mz_std*stdDistance
    peakFilter=(spectrum[:,0]>min_mz_peak)&(spectrum[:,0]<max_mz_peak)&(spectrum[:,1]>minInt)
    PeakData=spectrum[peakFilter,:]
    if len(PeakData[:,0])<minSignals and count<MaxCount:
        PeakData=Find_mzPeak(DataSet=DataSet,spectrum_id=spectrum_id,mz=mz,mz_std=mz_std,stdDistance=stdDistance+1,count=count+1,minInt=minInt)
    return PeakData

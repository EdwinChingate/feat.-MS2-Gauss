from scipy.signal import find_peaks
import numpy as np
def ExtractAllPeaks(MS1IDVec,DataSet,height=1e5,distance=10,min_RT=0,max_RT=1200,min_mz=0,max_mz=1000):
    RT_Filter=(MS1IDVec[:,1]>min_RT)&(MS1IDVec[:,1]<max_RT)
    MS1IDVec=MS1IDVec[RT_Filter,:].copy()
    N_ms1=len(MS1IDVec[:,0])
    FirstSpec=True
    for ms1_id in np.arange(N_ms1,dtype='int'):
        spectrum_id=MS1IDVec[ms1_id,0]
        SpectralSignals=DataSet[int(spectrum_id)]
        RawSpectrum0=np.array(SpectralSignals.get_peaks()).T        
        mzFil=(RawSpectrum0[:,0]>=min_mz)&(RawSpectrum0[:,0]<=max_mz)
        RawSpectrum=RawSpectrum0[mzFil,:]
        peaksMax=find_peaks(RawSpectrum[:,1],height=height,distance=distance)[0]
        NPeaks=len(peaksMax)
        RT=MS1IDVec[ms1_id,1]    
        RTVec=np.ones(NPeaks)*RT
        Peaks_and_RT=np.c_[RawSpectrum[peaksMax,:],RTVec]
        if FirstSpec:
            AllPeaks=Peaks_and_RT
            FirstSpec=False
        else:
            AllPeaks=np.append(AllPeaks,Peaks_and_RT,axis=0)
    AllPeaks=AllPeaks[AllPeaks[:,0].argsort(),:]
    return AllPeaks

def ms2Peak_contribution(RawSpectrum,mz,TotalInt,mz_std=2e-3,stdDistance=3):
    min_mz_peak=mz-mz_std*stdDistance
    max_mz_peak=mz+mz_std*stdDistance
    peakFilter=(RawSpectrum[:,0]>min_mz_peak)&(RawSpectrum[:,0]<max_mz_peak)
    PeakData=RawSpectrum[peakFilter,:]            
    PeakInt=sum(PeakData[:,1])    
    relative_contribution=[int(PeakInt/TotalInt*100)]
    return relative_contribution

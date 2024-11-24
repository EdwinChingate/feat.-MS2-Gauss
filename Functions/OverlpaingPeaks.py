import numpy as np
def OverlpaingPeaks(Spectrum_1,Spectrum_2,UniquePeaks_2):
    SharedPeaks_2=[]
    SharedPeaks_1=[]    
    for peak_id in UniquePeaks_2:
        min_mz_peak=Spectrum_2[peak_id,7]
        max_mz_peak=Spectrum_2[peak_id,8]
        OverlapFilter=(Spectrum_1[:,7]>max_mz_peak)|(Spectrum_1[:,8]<min_mz_peak)
        OverlapLoc=np.where(~OverlapFilter)[0]
        if len(Spectrum_1[OverlapLoc,:])==1:
            SharedPeaks_1.append(int(OverlapLoc))
            SharedPeaks_2.append(peak_id)
        elif len(Spectrum_1[OverlapLoc,:])>1:
            OverlapLoc=OverlapLoc[0]
            SharedPeaks_1.append(int(OverlapLoc))
            SharedPeaks_2.append(peak_id)
    UniquePeaks_2=np.delete(UniquePeaks_2,SharedPeaks_2)
    return [SharedPeaks_1,SharedPeaks_2,UniquePeaks_2]    

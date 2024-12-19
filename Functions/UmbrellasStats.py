from RT_Gauss_std import *
def UmbrellasStats(smooth_peaks,PeaksUmbrellaMat,NPeaks,RT_col=0,int_col=1,Points_for_regression=4):
    for pseudo_peak_id in np.arange(NPeaks,dtype='int'):
        EarlyLoc=int(PeaksUmbrellaMat[pseudo_peak_id,1])
        LateLoc=int(PeaksUmbrellaMat[pseudo_peak_id,2])
        MaxRTLoc=int(PeaksUmbrellaMat[pseudo_peak_id,0])
        Stats=RT_Gauss_std(PeakData=smooth_peaks,MaxRTLoc=MaxRTLoc,EarlyLoc=EarlyLoc,LateLoc=LateLoc,RT_col=RT_col,int_col=int_col,Points_for_regression=Points_for_regression)
        PeaksUmbrellaMat[pseudo_peak_id,3:7]=Stats[:4]    
    RegFilter=PeaksUmbrellaMat[:,5]>0
    PeaksUmbrellaMat=PeaksUmbrellaMat[RegFilter,:]
    return PeaksUmbrellaMat

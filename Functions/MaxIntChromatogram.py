import numpy as np
def MaxIntChromatogram(mz,mz_std,AllPeaks,stdDistance=3):
    min_mz=mz-mz_std*stdDistance
    max_mz=mz+mz_std*stdDistance
    mzLoc=np.where((AllPeaks[:,0]>min_mz)&(AllPeaks[:,0]<max_mz))[0]
    Chromatogram=AllPeaks[mzLoc,:]
    return Chromatogram

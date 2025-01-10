import numpy as np
def MaxIntChromatogram(mz,mz_std,AllRawPeaks,stdDistance=3):
    min_mz=mz-mz_std*stdDistance
    max_mz=mz+mz_std*stdDistance
    mzLoc=np.where((AllRawPeaks[:,0]>min_mz)&(AllRawPeaks[:,0]<max_mz))[0]
    Chromatogram=AllRawPeaks[mzLoc,:]
    Chromatogram=Chromatogram[Chromatogram[:,2].argsort(),:]
    return Chromatogram

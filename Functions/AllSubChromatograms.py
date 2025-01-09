from MaxIntChromatogram import *
from SplitChromatogram import *
def AllSubChromatograms(mz,mz_std,AllPeaks,stdDistance=3,RT_tol=5,minSignals=5):
    ChromatogramList=[]
    Chromatogram0=MaxIntChromatogram(mz=mz,mz_std=mz_std,AllPeaks=AllPeaks,stdDistance=stdDistance)
    ChromatogramList=SplitChromatogram(Chromatogram0=Chromatogram0,RT_tol=5,minSignals=5,minInt=1)
    return ChromatogramList

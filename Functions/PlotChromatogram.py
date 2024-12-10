from MaxIntChromatogram import *
import matplotlib.pyplot as plt
def PlotChromatogram(mz,mz_std,AllPeaks,stdDistance=3):
    Chromatogram=MaxIntChromatogram(mz=mz,mz_std=mz_std,AllPeaks=AllPeaks,stdDistance=stdDistance)  
    plt.plot(Chromatogram[:,2],Chromatogram[:,1],'.')
    plt.show()

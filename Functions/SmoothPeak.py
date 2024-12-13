from SmoothFourier import *
from SmoothSavgol import *
def SmoothPeak(PeakChr,stdDistance=1,SavgolWindowTimes=2,minPoly=5,int_col=1,RT_col=2):
    smooth_fourier,SavgolWindow_odd=SmoothFourier(PeakChr=PeakChr,stdDistance=stdDistance,SuggestSavgolWindow=True,RT_col=RT_col,int_col=int_col,SavgolWindowTimes=SavgolWindowTimes)
    smooth_savgol=SmoothSavgol(PeakChr=smooth_fourier,int_col=1,minWindow=SavgolWindow_odd,minPoly=minPoly)
    return smooth_savgol

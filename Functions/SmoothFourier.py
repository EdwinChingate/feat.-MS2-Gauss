import numpy as np
from LowSignalClustering import *
from RedistributeSampling import *
def SmoothFourier(PeakChr,stdDistance=1,RT_col=2,int_col=1,SuggestSavgolWindow=False,SavgolWindowTimes=2):
    RedisPeak=RedistributeSampling(PeakChr=PeakChr,RT_col=RT_col,int_col=int_col)
    time=RedisPeak[:,0]
    signal=RedisPeak[:,1]
    NSig=len(signal)
    min_RT=np.min(time)
    max_RT=np.max(time)
    RT_total=max_RT-min_RT
    SamplingRate=NSig/RT_total
    fft_signal=np.fft.fft(signal)
    frequencies = np.fft.fftfreq(NSig,d=(time[1] - time[0]))    
    NoiseTresVec=LowSignalClustering(SignalVec0=np.abs(fft_signal))[0]
    NoiseTres=NoiseTresVec[2]
    fft_filtered=fft_signal.copy()
    No_NoiseLoc=fft_signal<NoiseTres
    NoiseFreq=frequencies[No_NoiseLoc]
    Freq_mean=np.mean(abs(NoiseFreq))
    Freq_std=np.std(abs(NoiseFreq))
    FreqTres=Freq_mean-Freq_std*stdDistance
    fft_filtered[np.abs(frequencies)>FreqTres] = 0
    filtered_signal = np.fft.ifft(fft_filtered).real
    smooth_fourier=RedisPeak.copy()
    smooth_fourier[:,1]=np.abs(filtered_signal)    
    if SuggestSavgolWindow:
        SavgolWindow=SamplingRate/FreqTres*SavgolWindowTimes
        SavgolWindow_odd=int(SavgolWindow/2)*2+1
        return [smooth_fourier,SavgolWindow_odd]
    return smooth_fourier

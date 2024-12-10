import numpy as np
def DistanceDistribution(SignalVec0):
    SignalVec=SignalVec0[SignalVec0.argsort()].copy()
    Low_Signal=SignalVec[:-1]
    High_Signal=SignalVec[1:]
    Dif_Signal=High_Signal-Low_Signal
    Dif_Int_mean=np.mean(Dif_Signal)
    Dif_Int_std=np.mean(Dif_Signal)
    Signal_min=SignalVec[0]
    LowerSignalDist=[Signal_min,Dif_Int_std]
    return LowerSignalDist

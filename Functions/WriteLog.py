from ms2Peak_contribution import *
from Parameters_to_string import *
def WriteLog(RawSpectrum,Parameters,TotalInt,LogFileName='LogMS2_peaks.csv'):
    mz=Parameters[2]
    mz_std=Parameters[3]
    stdDistance=Parameters[4]    
    relative_contribution=ms2Peak_contribution(RawSpectrum=RawSpectrum,TotalInt=TotalInt,mz=mz,mz_std=mz_std,stdDistance=stdDistance)
    Parameters=relative_contribution+Parameters
    toWrite=Parameters_to_string(Parameters)
    LogFile=open(LogFileName,'a')
    LogFile.write(toWrite)
    LogFile.close()

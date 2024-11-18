from Find_mzPeak import *
from mz_Gauss_std import *
def mzPeak(DataSet,spectrum_id,mz,mz_std=2e-3,stdDistance=3,count=0,MaxCount=3,Points_for_regression=5,minSignals=7,minInt=1e3):
    PeakData=Find_mzPeak(DataSet=DataSet,spectrum_id=spectrum_id,mz=mz,mz_std=mz_std,stdDistance=stdDistance,MaxCount=MaxCount,minInt=minInt)
    GaussStats=mz_Gauss_std(PeakData,Points_for_regression=Points_for_regression)
    New_mz_std=GaussStats[1]
    if New_mz_std>mz_std and count<MaxCount:
        PeakData=mzPeak(DataSet=DataSet,spectrum_id=spectrum_id,mz=mz,mz_std=New_mz_std,count=count+1,minInt=minInt)
    return PeakData       
#This one should also return the results from the GaussStats

from scipy import stats
import numpy as np
def mz_Gauss_std(PeakData,Points_for_regression=5):
    maxInt=np.max(PeakData[:,1])
    maxInt_Loc=np.where(PeakData[:,1]==maxInt)[0][0]
    mz_maxInt=PeakData[maxInt_Loc,0]
    mz_DifVec=np.abs(PeakData[:,0]-mz_maxInt)
    PeakData=PeakData[mz_DifVec.argsort(),:].copy()
    Closest_PeakData=PeakData[:Points_for_regression,:]
    log_Int_Vec=np.log(Closest_PeakData[:,1]/maxInt)
    Variance_mz_vec=(Closest_PeakData[:,0]-mz_maxInt)**2
    X=log_Int_Vec
    Y=Variance_mz_vec
    reg=stats.linregress(X,Y)
    m=reg[0]
    b=reg[1]
    r2=reg[2]**2
    mz_std=np.sqrt(-m/2)
    sqrt2pi=2.5066282746310002 #np.sqrt(np.pi*2) 
    I_total=maxInt*mz_std*sqrt2pi
    GaussStats=[mz_maxInt,mz_std,b,r2,I_total]      
    return GaussStats    

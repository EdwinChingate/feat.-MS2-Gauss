from scipy import stats
import numpy as np
def PeakChromGauss(RT_vec,Int_vec,RT,RT_std,minSignasl=5,stdDistance=4):
    minInt=np.min(Int_vec)
    if minInt<0:
        Int_vec=Int_vec.copy()-minInt
    Int_total=sum(Int_vec)
    maxInt=np.max(Int_vec)
    RT=sum(RT_vec*Int_vec)/Int_total
    RT_DifVec=RT_vec-RT
    Variance_RT_vec=RT_DifVec**2
    log_Int_Vec=np.log(Int_vec/maxInt)
    X=log_Int_Vec
    Y=Variance_RT_vec
    reg=stats.linregress(x=X,y=Y)
    m=reg[0]
    b=reg[1]
    if m>0:
        return []
    r2=reg[2]**2
    RT_std=np.sqrt(-m/2)
    sqrt2pi=2.5066282746310002 #np.sqrt(np.pi*2) 
    I_total=maxInt*RT_std*sqrt2pi
    GaussStats=[RT,RT_std,I_total]  
    return GaussStats    

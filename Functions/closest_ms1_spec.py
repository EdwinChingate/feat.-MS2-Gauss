import numpy as np
def closest_ms1_spec(mz,RT,MS2_id,SummMS2,MS1IDVec,MS2_to_MS1_ratio=10):    
    MS2_Fullsignal_id=SummMS2[MS2_id,2]
    ID_filter=(MS1IDVec[:,0]<MS2_Fullsignal_id)&(MS1IDVec[:,0]>(MS2_Fullsignal_id-MS2_to_MS1_ratio)) #The MS2 is generated with the ions from the MS1, so the MS2 RT and id, would be higher
    Earlier_MS1IDVec=MS1IDVec[ID_filter,:]
    RT_DifVec=RT-Earlier_MS1IDVec[:,1]
    Min_RT_Dif=np.min(RT_DifVec)
    Closest_MS1_Loc=np.where(RT_DifVec==Min_RT_Dif)[0]
    spectrum_idVec=Earlier_MS1IDVec[RT_DifVec.argsort(),0]
    return spectrum_idVec

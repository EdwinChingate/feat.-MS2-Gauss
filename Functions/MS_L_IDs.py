import numpy as np
def MS_L_IDs(DataSet,min_RT=0,max_RT=1e5,RT_tol=10,Level=1):
    IDvec=[]
    spectrum_id=0
    min_RT=min_RT-RT_tol
    max_RT=max_RT+RT_tol
    for SpectralSignals in DataSet:
        MSLevel=SpectralSignals.getMSLevel()
        RT=SpectralSignals.getRT()
        if MSLevel==Level and RT>min_RT:            
            IDvec.append([int(spectrum_id),RT])
        if RT>max_RT:
            break
        spectrum_id+=1
    IDvec=np.array(IDvec)
    return IDvec

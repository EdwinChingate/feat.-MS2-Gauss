import numpy as np
def AllMS2Data(DataSet):
    SummMS2=[]
    FirstSpec=True
    spectrum_id=0
    for SpectralSignals in DataSet:
        MSLevel=SpectralSignals.getMSLevel()
        if MSLevel==2:
            Precursor=SpectralSignals.getPrecursors()[0]
            MZ=Precursor.getMZ()
            RT=SpectralSignals.getRT()     
            Spectrum=np.array(SpectralSignals.get_peaks()).T
            maxInt=np.max(Spectrum[:,1])
            SummSpec=np.array([MZ,RT,spectrum_id,maxInt])
            SummMS2.append(SummSpec)
        spectrum_id+=1
    SummMS2=np.array(SummMS2)      
    return SummMS2

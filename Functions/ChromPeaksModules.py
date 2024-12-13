import numpy as np
def ChromPeaksModules(SummaryChromPeaks,Modules,minSpec=10):
    ChromPeaks=[]
    for mod in Modules:
        ChromPeak=SummaryChromPeaks[mod,:]
        early_RT=int(np.min(ChromPeak[:,4]))
        late_RT=int(np.max(ChromPeak[:,5]))
        ChromPeaks.append([early_RT,late_RT])
    ChromPeaks=np.array(ChromPeaks)
    LocMinSpec=ChromPeaks[:,1]-ChromPeaks[:,0]
    ChromPeaks=ChromPeaks[LocMinSpec>minSpec,:]
    return ChromPeaks

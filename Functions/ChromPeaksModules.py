import numpy as np
def ChromPeaksModules(SummaryChromPeaks,Modules):
    ChromPeaks=[]
    for mod in Modules:
        ChromPeak=SummaryChromPeaks[mod,:]
        early_RT=int(np.min(ChromPeak[:,4]))
        late_RT=int(np.max(ChromPeak[:,5]))
        ChromPeaks.append([early_RT,late_RT])
    return ChromPeaks

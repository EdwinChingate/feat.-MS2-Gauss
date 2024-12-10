import numpy as np
def Summary_ms1_featModules(Modules,SummaryPeaks):
    mz_feat=[]
    for mod in Modules:
        summary_peak=SummaryPeaks[mod,:]
        summary_peak=summary_peak[summary_peak[:,1].argsort(),:]
        mz_feat.append(summary_peak[-1,:])
    mz_feat=np.array(mz_feat)
    return mz_feat

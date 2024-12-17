from PeakFeatStats import *
from AdjacencyList_mz import *
from Summary_ms1_featModules import *
from AdjacencyList_mz import *
from ms2_feat_modules import *
def mz_mz_std_ms1(edgesVecList,SomePeaks,stdDistance=3):
    SummaryPeaks=np.array(list(map(lambda edgesVec: PeakFeatStats(edgesVec,Peaks=SomePeaks), edgesVecList)))    
    AdjacencyList,feat_ids=AdjacencyList_mz(MS2_features=SummaryPeaks,mz_col=0,mz_CI_col=1,mz_Tol=0,stdDistance=3)
    Modules=ms2_feat_modules(AdjacencyList=AdjacencyList,ms2_ids=feat_ids)
    mz_feat=Summary_ms1_featModules(Modules=Modules,SummaryPeaks=SummaryPeaks)
    zeroT=mz_feat[:,1]>0
    mz_feat=mz_feat[zeroT,:]
    return mz_feat

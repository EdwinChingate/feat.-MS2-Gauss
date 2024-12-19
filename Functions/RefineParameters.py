from OverlappingGaussPeaks import *
from AdjustingPeaksContributions import *
from UpdatingChromMat import *
from RefineChromMat import *
from ParametersFitGaussPeaks import *
def RefineParameters(ParametersList,smooth_peaks):
    RT_vec=smooth_peaks[:,0]
    ChromatogramMatrix=OverlappingGaussPeaks(RT_vec=RT_vec,ParametersList=ParametersList)
    ContributionsVec=AdjustingPeaksContributions(smooth_peaks=smooth_peaks,ChromatogramMatrix=ChromatogramMatrix)
    Updated_ChromatogramMatrix=UpdatingChromMat(ChromatogramMatrix=ChromatogramMatrix,ContributionsVec=ContributionsVec)
    Refined_ChromatogramMatrix=RefineChromMat(ChromatogramMatrix=Updated_ChromatogramMatrix,Chromatogram=smooth_peaks,int_col=1)
    GaussianParMat=ParametersFitGaussPeaks(RT_vec=RT_vec,ChromatogramMatrix=Refined_ChromatogramMatrix,ParametersList=ParametersList)
    return GaussianParMat

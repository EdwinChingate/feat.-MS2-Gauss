from OverlappingGaussPeaks import *
from RefineChromMat import *
from ParametersFitGaussPeaks import *
from AdjustingPeaksContributions import *
from UpdatingChromMat import *
def RefineParameters(ParametersMat,smooth_peaks,boundsMat,ConstrainPeaks=True,keepRTCentroid=True):
    RT_vec=smooth_peaks[:,0]
    ChromatogramMatrix=OverlappingGaussPeaks(RT_vec=RT_vec,ParametersList=ParametersMat,stdDistance=3)
    ContributionsVec=AdjustingPeaksContributions(smooth_peaks=smooth_peaks,ChromatogramMatrix=ChromatogramMatrix)
    ChromatogramMatrix=UpdatingChromMat(ChromatogramMatrix=ChromatogramMatrix,ContributionsVec=ContributionsVec)
    ChromatogramMatrix=RefineChromMat(ChromatogramMatrix=ChromatogramMatrix,Chromatogram=smooth_peaks,int_col=1,ParametersMat=ParametersMat,ConstrainPeaks=ConstrainPeaks)
    GaussianParMat=ParametersFitGaussPeaks(RT_vec=RT_vec,ChromatogramMatrix=ChromatogramMatrix,boundsMat=boundsMat,ParametersMat=ParametersMat,keepRTCentroid=keepRTCentroid)
    return GaussianParMat

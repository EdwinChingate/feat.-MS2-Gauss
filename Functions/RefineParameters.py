from OverlappingGaussPeaks import *
from AdjustingPeaksContributions import *
from UpdatingChromMat import *
from RefineChromMat import *
from ParametersFitGaussPeaks import *
def RefineParameters(ParametersMat,smooth_peaks,boundsMat,minContribution=0,ReturnFilter=False):
    RT_vec=smooth_peaks[:,0]
    ChromatogramMatrix=OverlappingGaussPeaks(RT_vec=RT_vec,ParametersList=ParametersMat)
    ContributionsVec=AdjustingPeaksContributions(smooth_peaks=smooth_peaks,ChromatogramMatrix=ChromatogramMatrix)
    Updated_ChromatogramMatrix=UpdatingChromMat(ChromatogramMatrix=ChromatogramMatrix,ContributionsVec=ContributionsVec)
    Refined_ChromatogramMatrix=RefineChromMat(ChromatogramMatrix=Updated_ChromatogramMatrix,Chromatogram=smooth_peaks,int_col=1)
    GaussianParMat=ParametersFitGaussPeaks(RT_vec=RT_vec,ChromatogramMatrix=Refined_ChromatogramMatrix,boundsMat=boundsMat,ParametersMat=ParametersMat)
    Integral=boundsMat[2,1]
    minIntegralContribution=Integral*minContribution/100
    if minContribution>0:
        ContributionFilter=GaussianParMat[:,2]>minIntegralContribution
        GaussianParMat=GaussianParMat[ContributionFilter,:]
        if ReturnFilter:
            return [GaussianParMat,ContributionFilter]
    return GaussianParMat

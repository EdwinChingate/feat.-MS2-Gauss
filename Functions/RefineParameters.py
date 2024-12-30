from OverlappingGaussPeaks import *
from RefineChromMat import *
from ParametersFitGaussPeaks import *
def RefineParameters(ParametersMat,smooth_peaks,boundsMat,minContribution=0,ReturnFilter=False,ConstrainPeaks=True):
    RT_vec=smooth_peaks[:,0]
    ChromatogramMatrix=OverlappingGaussPeaks(RT_vec=RT_vec,ParametersList=ParametersMat,stdDistance=3)
    ChromatogramMatrix=RefineChromMat(ChromatogramMatrix=ChromatogramMatrix,Chromatogram=smooth_peaks,int_col=1,ParametersMat=ParametersMat,ConstrainPeaks=ConstrainPeaks)
    GaussianParMat=ParametersFitGaussPeaks(RT_vec=RT_vec,ChromatogramMatrix=ChromatogramMatrix,boundsMat=boundsMat,ParametersMat=ParametersMat)
    Integral=boundsMat[2,1]
    minIntegralContribution=Integral*minContribution/100
    if minContribution>0:
        ContributionFilter=GaussianParMat[:,2]>minIntegralContribution
        GaussianParMat=GaussianParMat[ContributionFilter,:]
        if ReturnFilter:
            return [GaussianParMat,ContributionFilter]
    return GaussianParMat

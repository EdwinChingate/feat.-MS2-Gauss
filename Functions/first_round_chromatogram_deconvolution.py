from SmoothData_and_FindPeaks import *
from RawGaussParameters import *
from OverlappingGaussPeaks import *
from AdjustingPeaksContributions import *
from UpdatingChromMat import *
from ParametersFitGaussPeaks import *
def first_round_chromatogram_deconvolution(Chromatogram,IntegralFrac=0.1):    
    smooth_peak,peaksMin=SmoothData_and_FindPeaks(Chromatogram=Chromatogram)
    ParametersList=RawGaussParameters(smooth_peak=smooth_peak,peaksMin=peaksMin)
    RT_vec=smooth_peak[:,0]
    ChromatogramMatrix=OverlappingGaussPeaks(RT_vec=RT_vec,ParametersList=ParametersList)
    ContributionsVec=AdjustingPeaksContributions(smooth_peak=smooth_peak,ChromatogramMatrix=ChromatogramMatrix)
    Updated_ChromatogramMatrix=UpdatingChromMat(ChromatogramMatrix,ContributionsVec)
    GaussianParList=ParametersFitGaussPeaks(RT_vec=RT_vec,ChromatogramMatrix=Updated_ChromatogramMatrix,ParametersList=ParametersList,minIntegral=minIntegral)
    return GaussianParList

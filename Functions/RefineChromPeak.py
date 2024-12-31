from OverlappingGaussPeaks import *
from RefineChromMat import *
from AdjustingPeaksContributions import *
from UpdatingChromMat import *
from ParametersFitGaussParallelPeaks import *
def RefineChromPeak(ParametersMat,smooth_peaks,boundsMat):
    RT_vec=smooth_peaks[:,0]
    ChromatogramMatrix=OverlappingGaussPeaks(RT_vec=RT_vec,ParametersList=ParametersMat)  
    ChromatogramMatrix=RefineChromMat(ChromatogramMatrix=ChromatogramMatrix,Chromatogram=smooth_peaks,ParametersMat=ParametersMat,int_col=1)
    GaussianPopulation=ParametersFitGaussParallelPeaks(RT_vec=RT_vec,ChromatogramMatrix=ChromatogramMatrix,boundsMat=boundsMat,ParametersMat=ParametersMat)    
    return GaussianPopulation

from RefineParameters import *
def RefineParametersPopulation(smooth_peaks,Population,boundsMat):
    Population0=Population.copy()
    for ParametersMat in Population0:
        GaussianParMat=RefineParameters(smooth_peaks=smooth_peaks,ParametersMat=ParametersMat,boundsMat=boundsMat,keepRTCentroid=True)
        Population.append(GaussianParMat)
        GaussianParMat=RefineParameters(smooth_peaks=smooth_peaks,ParametersMat=ParametersMat,boundsMat=boundsMat,keepRTCentroid=False)
        Population.append(GaussianParMat)
    return Population

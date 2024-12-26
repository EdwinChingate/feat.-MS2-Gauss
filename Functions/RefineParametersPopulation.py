from RefineParameters import *
def RefineParametersPopulation(smooth_peaks,Population,boundsMat):
    Population0=Population.copy()
    for ParametersMat in Population0:
        GaussianParMat=RefineParameters(smooth_peaks=smooth_peaks,ParametersMat=ParametersMat,boundsMat=boundsMat)
        Population.append(GaussianParMat)
    return Population

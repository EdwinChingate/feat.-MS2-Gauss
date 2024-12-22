from RefineParameters import *
def RefineParametersPopulation(smooth_peaks,Population):
    Population0=Population.copy()
    for ParametersMat in Population0:
        ParametersList=list(ParametersMat)
        GaussianParMat=RefineParameters(smooth_peaks=smooth_peaks,ParametersList=ParametersList)
        Population.append(GaussianParMat)
    return Population

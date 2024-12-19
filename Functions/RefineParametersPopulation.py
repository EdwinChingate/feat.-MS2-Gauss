from RefineParameters import *
def RefineParametersPopulation(smooth_peaks,Population):
    RefinedParametersList=[]
    for ParametersMat in Population:
        ParametersList=list(ParametersMat)
        GaussianParMat=RefineParameters(smooth_peaks=smooth_peaks,ParametersList=ParametersList)
        RefinedParametersList.append(GaussianParMat)
    return RefinedParametersList                

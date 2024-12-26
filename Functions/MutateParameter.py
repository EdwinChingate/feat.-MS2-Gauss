import scipy.stats as stats
def MutateParameter(parameter,boundsVec,parameter_std,Mutants):
    parameter_min=boundsVec[0]
    parameter_max=boundsVec[1]       
    Mutants=stats.truncnorm.rvs((parameter_min-parameter)/parameter_std,(parameter_max-parameter)/parameter_std,loc=parameter,scale=parameter_std,size=Mutants)
    return Mutants

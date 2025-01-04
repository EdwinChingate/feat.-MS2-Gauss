from GaussianChromatogram import *
def GaussianLambda(RT_vec):
    GaussianLam=lambda loc,*ParametersList: GaussianChromatogram(loc,RT_vec,*ParametersList)
    return GaussianLam

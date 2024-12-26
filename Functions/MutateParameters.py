import numpy as np
from MutateParameterLambda import *
def MutateParameters(ParametersVec,boundsVec,parameter_std,Mutants):
    ParametersMutator=MutateParameterLambda(boundsVec=boundsVec,parameter_std=parameter_std,Mutants=Mutants)
    Mutants=list(map(ParametersMutator,ParametersVec))
    Mutants=np.array(Mutants).T
    return Mutants

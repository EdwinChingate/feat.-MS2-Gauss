from MutateParameter import *
def MutateParameterLambda(boundsVec,parameter_std,Mutants):
    MutanteLambda=lambda parameter: MutateParameter(parameter,boundsVec=boundsVec,parameter_std=parameter_std,Mutants=Mutants)
    return MutanteLambda

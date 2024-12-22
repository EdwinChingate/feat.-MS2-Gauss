import numpy as np
from MutantOffspring import *
def MutationTimes(Population,mut_stdVec=[10,1,1e6],Mutants=4):
    OriginalPopulation=Population.copy()
    NIndividuals=len(OriginalPopulation)
    for individual in np.arange(NIndividuals,dtype='int'):
        ParametersMat_RawIndividual=OriginalPopulation[individual].copy()
        MutantPopulation=MutantOffspring(ParametersMat=ParametersMat_RawIndividual,Mutants=Mutants,mut_stdVec=mut_stdVec)        
        Population=MutantPopulation+Population
    return Population

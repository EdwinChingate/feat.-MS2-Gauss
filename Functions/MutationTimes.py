import numpy as np
from MutantOffspring import *
def MutationTimes(Population,boundsMat,mut_stdVec=[0.6,0.7,0.8],Mutants=4,stdDistance=3):
    OriginalPopulation=Population.copy()
    NIndividuals=len(OriginalPopulation)
    for individual in np.arange(NIndividuals,dtype='int'):
        ParametersMat_RawIndividual=OriginalPopulation[individual].copy()
        MutantPopulation=MutantOffspring(ParametersMat=ParametersMat_RawIndividual,boundsMat=boundsMat,Mutants=Mutants,mut_stdVec=mut_stdVec,stdDistance=stdDistance)        
        Population=MutantPopulation+Population
    return Population

import numpy as np
from Mutate import *
def MutationTimes(Population,MutationRateVec,boundsMat,Times=2):
    OriginalPopulation=Population.copy()
    NIndividuals=len(OriginalPopulation)
    NNewIndividuals=NIndividuals*(Times-1) 
    for individual in np.arange(NNewIndividuals,dtype='int'):
        ParametersMat_RawIndividual=OriginalPopulation[individual%NIndividuals].copy()
        ParametersMat=Mutate(ParametersMat=ParametersMat_RawIndividual,MutationRateVec=MutationRateVec,boundsMat=boundsMat)
        Population.append(ParametersMat)    
    return Population

import numpy as np
def EvaluatePopulationIntensity(Population):
    NIndividuals=len(Population)
    BiggestPeakVec=np.zeros(NIndividuals)
    for individual_id in np.arange(NIndividuals, dtype='int'):
        Individual=Population[individual_id]
        MostIntensePeakInt=np.max(Individual[:,2]/Individual[:,1])
        BiggestPeakVec[individual_id]=MostIntensePeakInt    
    return BiggestPeakVec

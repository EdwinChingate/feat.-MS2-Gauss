import numpy as np
def Mate_squareColumns_GaussParPop(SeedPopulation):
    NSeedIndividuals=len(SeedPopulation)
    NPeaks=len(SeedPopulation[0])
    Population=[]
    for individual_1 in np.arange(NSeedIndividuals,dtype='int'):
        ParametersMat_i1=SeedPopulation[individual_1]        
        for individual_2 in np.arange(individual_1,NSeedIndividuals,dtype='int'):
            ParametersMat_i2=SeedPopulation[individual_2]
            ParametersMat=ParametersMat_i1.copy()
            ParametersMat[:,2]=ParametersMat_i2[:,2]
            Population.append(ParametersMat)
    return Population

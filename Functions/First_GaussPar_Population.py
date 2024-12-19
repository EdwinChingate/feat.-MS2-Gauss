import numpy as np
def First_GaussPar_Population(ParametersMat):
    NParameters=len(ParametersMat[:,0])
    Population=[]
    for individual in np.arange(NParameters,dtype='int'):
        ParametersMat_i=ParametersMat.copy()
        ParametersMat_i[:,2]=0
        ParametersMat_i[individual,2]=ParametersMat[individual,2]
        Population.append(ParametersMat_i)
    return Population

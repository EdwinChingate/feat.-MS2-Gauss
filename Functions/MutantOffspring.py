import numpy as np
from MutantansExtractor import *
def MutantOffspring(ParametersMat,Mutants=4,mut_stdVec=[10,1,1e6]):
    NPeaks=len(ParametersMat[:,0])
    NParameters=len(ParametersMat[0,:])
    MutationTensor=np.stack([ParametersMat]*Mutants,axis=0)
    for parameter_id in np.arange(NParameters):
        mut_std=mut_stdVec[parameter_id]
        Perturbation=np.random.normal(0,mut_std,(Mutants,NPeaks))
        MutationTensor[:,:,parameter_id]=np.abs(MutationTensor[:,:,parameter_id]+Perturbation)
    MutantPopulation=MutantansExtractor(MutationTensor=MutationTensor,Mutants=Mutants)
    return MutantPopulation

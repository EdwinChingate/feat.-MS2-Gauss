import numpy as np
from MutateParameters import *
from MutantansExtractor import *
def MutantOffspring(ParametersMat,boundsMat,stdDistance,Mutants=4,mut_stdVec=[0.6,0.7,0.8]):
    NPeaks=len(ParametersMat[:,0])
    NParameters=len(ParametersMat[0,:])
    MutationTensor=np.stack([ParametersMat]*Mutants,axis=0)
    boundsMatRef=boundsMat.copy()
    boundsMatRef[0,0]=boundsMat[0,0]+ParametersMat[0,1]*stdDistance
    boundsMatRef[0,1]=boundsMat[0,1]-ParametersMat[0,1]*stdDistance    
    for parameter_id in np.arange(NParameters):
        boundsVec=boundsMatRef[parameter_id,:]
        parameter_interval=boundsMat[parameter_id,2]
        mut_std=mut_stdVec[parameter_id]
        ParametersVec=ParametersMat[:,parameter_id]
        MutationTensor[:,:,parameter_id]=MutateParameters(ParametersVec=ParametersVec,boundsVec=boundsVec,parameter_std=mut_std,Mutants=Mutants)
    MutantPopulation=MutantansExtractor(MutationTensor=MutationTensor,Mutants=Mutants)
    return MutantPopulation

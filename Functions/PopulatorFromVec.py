import numpy as np
def PopulatorFromVec(ParametersMat,SelectorVectorList):
    Population=[]
    for SelectorVector in SelectorVectorList:
        KeepVec=np.where(SelectorVector)[0]
        Individual=ParametersMat[KeepVec,:]
        Population.append(Individual)
    return Population

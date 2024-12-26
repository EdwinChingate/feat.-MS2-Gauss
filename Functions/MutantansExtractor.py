import numpy as np
def MutantansExtractor(MutationTensor,Mutants):
    MutantPopulation=[]
    for mutant in np.arange(Mutants):
        ParametersMat_mutant=MutationTensor[mutant,:,:]
        ParametersMat_mutant=ParametersMat_mutant[ParametersMat_mutant[:,0].argsort(),:]        
        MutantPopulation.append(ParametersMat_mutant)
    return MutantPopulation

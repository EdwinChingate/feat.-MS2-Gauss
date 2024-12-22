def MutantansExtractor(MutationTensor,Mutants):
    MutantPopulation=[]
    for mutant in np.arange(Mutants):
        ParametersMat_mutant=MutationTensor[mutant,:,:]
        MutantPopulation.append(ParametersMat_mutant)
    return MutantPopulation

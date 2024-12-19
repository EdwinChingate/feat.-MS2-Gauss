from RandomVecGen import *
def Mutate(ParametersMat,MutationRateVec,boundsMat):
    NParameters=len(MutationRateVec)
    NPeaks=len(ParametersMat[:,0])
    for parameter_column in np.arange(NParameters,dtype='int'):
        MutationRate=MutationRateVec[parameter_column]
        bounds=boundsMat[parameter_column,:]
        min_val=bounds[0]
        max_val=bounds[1]
        interval=max_val-min_val
        parameterVec=RandomVecGen(NPeaks)*interval+min_val
        ChoiseVec=RandomVecGen(NPeaks)
        SelectorChoiseVec=ChoiseVec<MutationRate
        #ParametersMat[SelectorChoiseVec,parameter_column]=parameterVec[SelectorChoiseVec]
        ParametersMat[:,parameter_column]=parameterVec
    return ParametersMat

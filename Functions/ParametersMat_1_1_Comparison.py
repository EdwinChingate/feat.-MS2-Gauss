import numpy as np
def ParametersMat_1_1_Comparison(ParametersMat1,ParametersMat2,RelDifsAc=10):
    ParametersMatDif=sum(np.abs(ParametersMat1-ParametersMat2))
    ParametersMatSum=sum(ParametersMat1+ParametersMat2)
    RelativeComparison=ParametersMatDif/ParametersMatSum*100
    #print(RelativeComparison)
    RelativeComparisonTest=RelativeComparison<RelDifsAc
    RelativeComparisonTestLoc=np.where(RelativeComparisonTest)[0]
    if len(RelativeComparisonTestLoc)<2:
        Pass=True
    else:
        Pass=False
    return Pass

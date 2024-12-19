from ParametersMat_1_1_Comparison import *
def ExcludeFit(FittestIndividual,FitPopulation):
    for ParametersMat in FitPopulation:
        ParametersMat2=ParametersMat
        Pass=ParametersMat_1_1_Comparison(ParametersMat1=FittestIndividual,ParametersMat2=ParametersMat2,RelDifsAc=10)
        if not Pass:
            return False
    return True

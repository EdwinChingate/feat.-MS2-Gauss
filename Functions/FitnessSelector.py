from ExcludeFit import *
def FitnessSelector(r2Vec,Population,NSelect=0):
    if NSelect==0:
        NSelect=len(Population)
    FitPopulation=[]
    Sortr2Vec=(-r2Vec).argsort()    
    r2ListFit=[]
    for FittestIndividual_id in Sortr2Vec:
        FittestIndividual=Population[FittestIndividual_id]
        Pass=ExcludeFit(FittestIndividual=FittestIndividual,FitPopulation=FitPopulation)
        if Pass:
            FitPopulation.append(Population[FittestIndividual_id])
            r2ListFit.append(r2Vec[FittestIndividual_id])
        if len(FitPopulation)==NSelect:
            break
    return [FitPopulation,r2ListFit]

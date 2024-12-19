from ExcludeFit import *
def FitnessSelector(r2Vec,Population,NSelect,FitPopulation=[]):
    Sortr2Vec=(-r2Vec).argsort()
    FittestIndividual_id=Sortr2Vec[0]
    FittestIndividual=Population.pop(FittestIndividual_id)
    Pass=ExcludeFit(FittestIndividual=FittestIndividual,FitPopulation=FitPopulation)
    if Pass:
        FitPopulation.append(FittestIndividual)
    if len(FitPopulation)<NSelect:
        FitPopulation=FitnessSelector(r2Vec=Sortr2Vec[1:],Population=Population,NSelect=NSelect,FitPopulation=FitPopulation)
    return FitPopulation

from Mate_square_GaussParPop import *
from EvaluatePopulation import *
from FitnessSelector import *
def Mate_WildGenerations(Population,smooth_peaks,boundsMat,Generations=5,NSelect=10,NOffspring=10):    
    for generation in np.arange(Generations):
        Population=Mate_square_WildPop(SeedPopulation=Population,boundsMat=boundsMat,NOffspring=NOffspring) 
        r2Vec=EvaluatePopulation(Population=Population,smooth_peaks=smooth_peaks)        
        Population,r2ListFit=FitnessSelector(r2Vec=r2Vec,Population=Population,NSelect=NSelect) 
    return [Population,r2ListFit]

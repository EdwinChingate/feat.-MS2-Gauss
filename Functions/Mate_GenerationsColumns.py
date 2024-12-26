from Mate_squareColumns_GaussParPop import *
from EvaluatePopulation import *
from FitnessSelector import *
def Mate_GenerationsColumns(Population,smooth_peaks,Generations=5,NSelect=10):    
    for generation in np.arange(Generations):        
        Population=Mate_squareColumns_GaussParPop(SeedPopulation=Population) 
        r2Vec=EvaluatePopulation(Population=Population,smooth_peaks=smooth_peaks)
        Population,r2ListFit=FitnessSelector(r2Vec=r2Vec,Population=Population,NSelect=NSelect)
    return [Population,r2ListFit]

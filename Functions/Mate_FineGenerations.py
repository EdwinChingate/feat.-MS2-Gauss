from RefineParametersPopulation import *
from EvaluatePopulation import *
from FitnessSelector import *
from Mate_square_GaussParPop import *
def Mate_FineGenerations(Population,smooth_peaks,boundsMat,Generations=5,NSelect=4):    
    for generation in np.arange(Generations):
        Population=Mate_square_GaussParPop(SeedPopulation=Population)
        Population=RefineParametersPopulation(smooth_peaks=smooth_peaks,Population=Population,boundsMat=boundsMat)
        r2Vec=EvaluatePopulation(Population=Population,smooth_peaks=smooth_peaks)
        Population,r2ListFit=FitnessSelector(r2Vec=r2Vec,Population=Population,NSelect=NSelect)      
    return [Population,r2ListFit]

from Mate_square_GaussParPop import *
from EvaluatePopulation import *
from FitnessSelector import *
from MutationTimes import *
def Mate_MutantGenerations(Population,smooth_peaks,Generations=5,NSelect=5,mut_stdVec=[20,10,1e7],Mutants=5):    
    for generation in np.arange(Generations):
        Population=Mate_square_GaussParPop(SeedPopulation=Population) 
        Population=Mate_square_GaussParPop(SeedPopulation=Population) 
        Population=MutationTimes(Population=Population,mut_stdVec=mut_stdVec,Mutants=Mutants)
        r2Vec=EvaluatePopulation(Population=Population,smooth_peaks=smooth_peaks)
        Population,r2ListFit=FitnessSelector(r2Vec=r2Vec,Population=Population,NSelect=NSelect)      
    return Population

from Mate_square_GaussParPop import *
from EvaluatePopulation import *
#from FitnessSelector import *
from FitnessPeakSelector import *
def Mate_Generations(Population,smooth_peaks,Generations=5,NSelect=10):    
    for generation in np.arange(Generations):
        Population=Mate_square_GaussParPop(SeedPopulation=Population) 
        Population=Mate_square_GaussParPop(SeedPopulation=Population)         
        r2Vec=EvaluatePopulation(Population=Population,smooth_peaks=smooth_peaks)
        #Population,r2ListFit=FitnessSelector(r2Vec=r2Vec,Population=Population,NSelect=NSelect)  
        Population,bp_r2ListFit=FitnessPeakSelector(r2Vec=r2Vec,Population=Population,NSelect=NSelect) 
    r2ListFit=r2Vec[bp_r2ListFit]
    return [Population,r2ListFit]

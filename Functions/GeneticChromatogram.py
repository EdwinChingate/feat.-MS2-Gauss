from Mate_GenerationsColumns import *
from Mate_Generations import *
from Mate_MutantGenerations import *
from Mate_FineGenerations import *
from MutationTimes import *
from EvaluatePopulation import *
from FitnessSelector import *
from RefineParametersPopulation import *
from GaussBoundaries import *
from RefineParameters import *
from RefineParametersPopulation import *
def GeneticChromatogram(Population0,smooth_peaks):
    boundsMat=GaussBoundaries(smooth_peaks=smooth_peaks)
    Mutants=50
    mut_stdVec=boundsMat[:,2].copy()
    Population=MutationTimes(Population=Population0,mut_stdVec=mut_stdVec,boundsMat=boundsMat,Mutants=200)
    r2Vec=EvaluatePopulation(Population=Population,smooth_peaks=smooth_peaks)
    Population,r2ListFit=FitnessSelector(r2Vec=r2Vec,Population=Population,NSelect=20) 
    Population,bp_r2ListFit=FitnessPeakSelector(r2Vec=r2ListFit,Population=Population,NSelect=5) 
    r2Mat=[]
    r2Max_Min=0
    stuck_counter=0
    for x in np.arange(10):
        Population=Population+Population0            
        Population,r2ListFit=Mate_MutantGenerations(Population=Population,smooth_peaks=smooth_peaks,Generations=5,NSelect=5,boundsMat=boundsMat,mut_stdVec=mut_stdVec,Mutants=Mutants)     
        Population=RefineParametersPopulation(smooth_peaks=smooth_peaks,Population=Population,boundsMat=boundsMat)
        Population,r2ListFit=Mate_Generations(Population=Population,smooth_peaks=smooth_peaks,Generations=3,NSelect=5)                 
        r2Mat.append(r2ListFit)
        r2Max=max(r2ListFit)
        r2Max_Min=min(r2ListFit)
    return Population

import numpy as np
def Mate_square_WildPop(SeedPopulation,boundsMat,NOffspring=3):
    NSeedIndividuals=len(SeedPopulation)
    Integral=boundsMat[2,1]
    NPeaks=len(SeedPopulation[0])
    Population=SeedPopulation.copy()
    for individual_1 in np.arange(NSeedIndividuals,dtype='int'):
        ParametersMat_i1=SeedPopulation[individual_1].copy()        
        for individual_2 in np.arange(individual_1,NSeedIndividuals,dtype='int'):
            ParametersMat_i2=SeedPopulation[individual_2].copy()
            ParametersMat=np.append(ParametersMat_i1,ParametersMat_i2,axis=0)
            ParametersMat=ParametersMat[ParametersMat[:,0].argsort(),:]   
            ParametersMat=UniquePeaks(ParametersMat,PeakTol=[0.1,0.01,1e3])
            NNPeaks=len(ParametersMat[:,0])
            if NNPeaks==NPeaks:
                break
            for offs in np.arange(NOffspring):
                RandomPeaks=np.random.randint(low=0,high=NNPeaks,size=NPeaks)
                NewParametersMat=ParametersMat[RandomPeaks,:]
                PeaksIntegral=np.sum(NewParametersMat[:,2])
                NewParametersMat[:,2]=NewParametersMat[:,2]*Integral/PeaksIntegral
                Population.append(NewParametersMat)
    return Population

import numpy as np
def BiggestSelector(r2,r2Vec,Population):
    BiggestPeakList=[]
    LevelLineVec=np.where(r2Vec==r2)[0]
    if len(LevelLineVec)==1:
        FittestIndividual_id=LevelLineVec[0]
        return FittestIndividual_id
    for Individual_id in LevelLineVec:
        Individual=Population[Individual_id]
        MostIntensePeakInt=np.max(Individual[:,2]/Individual[:,1])
        BiggestPeakList.append(MostIntensePeakInt)
    if len(BiggestPeakList)==0:
        return -1
    BiggestPeakVec=np.array(BiggestPeakList)
    BiggestPeak=np.max(BiggestPeakVec)
    BiggestPeakLoc=np.where(BiggestPeakVec==BiggestPeak)[0][0]
    FittestIndividual_id=LevelLineVec[BiggestPeakLoc]
    return FittestIndividual_id

import numpy as np
def RemoveChromBackGround(PeakSeed,stdDistance,ChromPoints):
    Chromatogram=PeakSeed[1]
    GaussianParameters=PeakSeed[0]
    min_RT=min(Chromatogram[:,2])
    max_RT=max(Chromatogram[:,2])
    max_std=(max_RT-min_RT)/stdDistance/2
    RT_vec=np.linspace(min_RT,max_RT,ChromPoints)
    std_Loc=GaussianParameters[:,1]<max_std
    ParametersMat=GaussianParameters[std_Loc,:]
    TresholdList=[min_RT,max_RT]
    return [ParametersMat,TresholdList,RT_vec]

import numpy as np
def UniquePeaks(ParametersMat,PeakTol=[0.1,0.01,1e3],KeepAllPeaks=False,boundsMat=[]):    
    minIntLoc=ParametersMat[:,2]>PeakTol[2]
    ParametersMat=ParametersMat[minIntLoc,:]
    NPeaks=len(ParametersMat[:,0])
    UniqueParametersMat=(ParametersMat[0,:].copy()).reshape(1,-1)  
    EarlierPeak=ParametersMat[0,:].copy()
    for peak_id in np.arange(1,NPeaks):        
        Peak=(ParametersMat[peak_id,:].copy()).reshape(1,-1)  
        PeakDif=Peak-EarlierPeak        
        EvalPeakDif=np.where((PeakDif-PeakTol)<0)[0]
        if len(EvalPeakDif)<3:
            UniqueParametersMat=np.append(UniqueParametersMat,Peak,axis=0)
            EarlierPeak=Peak
        elif KeepAllPeaks:
            UniqueParametersMat=np.append(UniqueParametersMat,Peak,axis=0)
            UniqueParametersMat[-1,2]=UniqueParametersMat[-1,2].copy()+UniqueParametersMat[-2,2].copy()
            UniqueParametersMat[-1,2]=0
            UniqueParametersMat[-1,0]=boundsMat[0,0]
            EarlierPeak=Peak
    return UniqueParametersMat

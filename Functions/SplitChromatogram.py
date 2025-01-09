import numpy as np
from RT_edges import *
def SplitChromatogram(Chromatogram0,RT_tol=5,minSignals=5,minInt=1):
    edgesVecList=RT_edges(Chromatogram=Chromatogram0,RT_tol=RT_tol)
    ChromatogramList=[]
    for edges in edgesVecList:
        early_RT=int(edges[0])
        late_RT=int(edges[1])
        if (late_RT-early_RT)>minSignals:
            Chromatogram=Chromatogram0[early_RT:late_RT,:].copy()
            LChrom=len(Chromatogram[:,0])
            MaxInt=np.max(Chromatogram[:,1])
            MaxIntF=MaxInt*minInt/100
            MinIntFil=Chromatogram[:,1]>MaxIntF
            Chromatogram=Chromatogram[MinIntFil,:]
            if len(Chromatogram[:,0])<LChrom:
                Chromatograms=SplitChromatogram(Chromatogram0=Chromatogram,RT_tol=5,minSignals=5,minInt=1)
            else:
                Chromatograms=[Chromatogram]
            ChromatogramList=Chromatograms+ChromatogramList
    return ChromatogramList

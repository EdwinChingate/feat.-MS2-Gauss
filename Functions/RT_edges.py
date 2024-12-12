import numpy as np
def RT_edges(Chromatogram,RT_tol=10):
    NSignals=len(Chromatogram[:,0])
    low_RTVec=Chromatogram[:-1,2]
    high_RTVec=Chromatogram[1:,2]
    RT_difVec=high_RTVec-low_RTVec
    difLoc=np.where(RT_difVec>RT_tol)[0]+1
    N_difLoc=len(difLoc)
    mz_divMat=np.zeros((N_difLoc+1,2))
    mz_divMat[0,0]=0
    mz_divMat[1:,0]=difLoc
    mz_divMat[:-1,1]=difLoc
    mz_divMat[-1,1]=len(Chromatogram[:,0])
    edgesVecList=list(mz_divMat)
    return edgesVecList

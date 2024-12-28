import numpy as np
def RefineChromMat(ChromatogramMatrix,Chromatogram,ParametersMat,int_col=1,stdDistance=4):
    IntVec=Chromatogram[:,int_col]
    ChromatogramMatrix_Adj=ChromatogramMatrix.copy()
    Refined_ChromatogramMatrix=ChromatogramMatrix.copy()
    NContributions=len(ChromatogramMatrix[0,:])
    SumSubstractVec=np.ones(NContributions)
    for peak_id in np.arange(NContributions,dtype='int'):
        RT,RT_std=ParametersMat[peak_id,:2]
        min_RT=RT-stdDistance*RT_std
        max_RT=RT+stdDistance*RT_std
        RTLoc=(RT_vec>min_RT)&(RT_vec<max_RT)
        SumSubstractVec[peak_id]=0
        Others_int_Contribution=np.matmul(ChromatogramMatrix_Adj[RTLoc,:],SumSubstractVec)
        SumSubstractVec[peak_id]=1
        Refin_int_Contribution=IntVec[RTLoc]-Others_int_Contribution
        Refined_ChromatogramMatrix[RTLoc,peak_id]=Refin_int_Contribution
    return Refined_ChromatogramMatrix

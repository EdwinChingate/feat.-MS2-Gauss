import numpy as np
def RefineChromMat(ChromatogramMatrix,Chromatogram,RT_col=0,int_col=1):
    IntVec=Chromatogram[:,int_col]
    ChromatogramMatrix_Adj=ChromatogramMatrix.copy()
    ChromResidualSignal=Chromatogram[:,int_col]-sum(ChromatogramMatrix.T)
    minIntDif=np.min(ChromResidualSignal)
    #if minIntDif<0:
     #   ChromatogramMatrix_Adj=ChromatogramMatrix_Adj+minIntDif
    Refined_ChromatogramMatrix=ChromatogramMatrix.copy()
    NContributions=len(ChromatogramMatrix[0,:])
    SumSubstractVec=np.ones(NContributions)
    for peak_id in np.arange(NContributions,dtype='int'):
        SumSubstractVec[peak_id]=0
        Others_int_Contribution=np.matmul(ChromatogramMatrix_Adj,SumSubstractVec)
        SumSubstractVec[peak_id]=1
        Refin_int_Contribution=IntVec-Others_int_Contribution
        Refined_ChromatogramMatrix[:,peak_id]=Refin_int_Contribution
    return Refined_ChromatogramMatrix

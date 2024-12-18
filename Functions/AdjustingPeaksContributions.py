import numpy as np
def AdjustingPeaksContributions(smooth_peak,ChromatogramMatrix,Background=0):
    IntVec=smooth_peak[:,1]
    NSignals=len(IntVec)
    BackgroundVec=np.ones(NSignals)*Background
    BackgroundVec=BackgroundVec.reshape(-1,1)
    ChromatogramMatrixBG=np.append(ChromatogramMatrix,BackgroundVec,axis=1)
    ChromatogramMatrixTranspose=ChromatogramMatrixBG.T
    MatrixTransInt=np.matmul(ChromatogramMatrixTranspose,IntVec)
    MatrixTransChromMat=np.matmul(ChromatogramMatrixTranspose,ChromatogramMatrixBG)
    InvMatrixTransChromMat=np.linalg.inv(MatrixTransChromMat)
    ContributionsVec=np.matmul(InvMatrixTransChromMat,MatrixTransInt)
    ContributionsVec[-1]=ContributionsVec[-1]*Background
    return ContributionsVec

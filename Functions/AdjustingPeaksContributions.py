import numpy as np
def AdjustingPeaksContributions(smooth_peak,ChromatogramMatrix):
    IntVec=smooth_peak[:,1]
    ChromatogramMatrixTranspose=ChromatogramMatrix.T
    MatrixTransInt=np.matmul(ChromatogramMatrixTranspose,IntVec)
    MatrixTransChromMat=np.matmul(ChromatogramMatrixTranspose,ChromatogramMatrix)
    InvMatrixTransChromMat=np.linalg.inv(MatrixTransChromMat)
    ContributionsVec=np.matmul(InvMatrixTransChromMat,MatrixTransInt)
    return ContributionsVec

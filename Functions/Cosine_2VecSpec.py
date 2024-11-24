import numpy as np
def Cosine_2VecSpec(AlignedSpecMat):
    S1_dot_S2=np.sum(AlignedSpecMat[:,1]*AlignedSpecMat[:,2])
    S1_dot_S1=np.sum(AlignedSpecMat[:,1]*AlignedSpecMat[:,1])
    S2_dot_S2=np.sum(AlignedSpecMat[:,2]*AlignedSpecMat[:,2])
    Cosine=S1_dot_S2/np.sqrt(S1_dot_S1*S2_dot_S2)
    return Cosine

import numpy as np
def NPeaksRestrict(GaussianParMat,boundsMat,stdDistance=4):
    GaussianParMat=GaussianParMat[GaussianParMat[:,1].argsort(),:]
    NPeaks=len(GaussianParMat[:,0])
    std_Acum_Vec=np.zeros(NPeaks)
    RT_interval=boundsMat[0,2]
    std_Acum_Vec[0]=GaussianParMat[0,1]
    for peak_id in np.arange(1,NPeaks):
        std_Acum_Vec[peak_id]=std_Acum_Vec[peak_id-1]+GaussianParMat[peak_id,1]
    std_Acum_Vec=std_Acum_Vec*stdDistance
    NPeaks_std_cut=np.where(std_Acum_Vec<RT_interval)[0][-1]+2
    return NPeaks_std_cut

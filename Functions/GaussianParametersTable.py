import numpy as np
import pandas as pd
def GaussianParametersTable(GaussianParametersList):
    GaussianParametersMat=GaussianParametersList[0][0]
    NPeaksGroups=len(GaussianParametersList)
    for PeakGroup_id in np.arange(1,NPeaksGroups):
        Peak=GaussianParametersList[PeakGroup_id]
        GaussianParameters=Peak[0]
        GaussianParametersMat=np.append(GaussianParametersMat,GaussianParameters,axis=0)
    GaussianParametersMat=GaussianParametersMat[GaussianParametersMat[:,0].argsort(),:]
    GaussianParametersDF=pd.DataFrame(GaussianParametersMat,columns=['RT_(s)','RT_std_(s)','Integral'])
    return GaussianParametersDF

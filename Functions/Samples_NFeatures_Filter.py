import numpy as np
from SamplesNames_common_Attributes import *
def Samples_NFeatures_Filter(AlignedSamplesDF,SamplesInfDF,AttributeList,attributeList,Min_Feat,MoreThan=True):
    Index=SamplesNames_common_Attributes(SamplesInfDF=SamplesInfDF,AttributeList=AttributeList,attributeList=attributeList)    
    SamplesDF=AlignedSamplesDF[Index].copy()
    SampLocMat=np.array(SamplesDF.copy())
    SampOnesLoc=np.where(SampLocMat>0)
    SampLocMat[SampOnesLoc]=1
    Filter=sum(SampLocMat.T)>=Min_Feat
    if MoreThan:        
        return [Filter,Index]
    else:
        return [~Filter,Index]

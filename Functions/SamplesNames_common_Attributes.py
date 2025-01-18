import numpy as np
from Samples_AttributesFilter import *
def SamplesNames_common_Attributes(SamplesInfDF,AttributeList,attributeList):
    if len(AttributeList)!=len(attributeList):
        print('The list of attributes should match its list of values')
        return 0
    Filter=Samples_AttributesFilter(SamplesInfDF=SamplesInfDF,AttributeList=AttributeList,attributeList=attributeList)
    Index=SamplesInfDF[Filter].index
    Index=np.array(Index,dtype='str')
    return Index

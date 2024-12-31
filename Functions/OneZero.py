import numpy as np
def OneZero(SelectorVector,NPeaks,SelectorVectorList=[]):
    OnesVec=np.where(SelectorVector==1)[0]
    for one in OnesVec:
        SelectorOne=SelectorVector.copy()
        SelectorOne[one]=0
        if sum(SelectorOne)>NPeaks:
            SelectorVectorList=OneZero(SelectorVector=SelectorOne,NPeaks=NPeaks,SelectorVectorList=SelectorVectorList)
        else:
            SelectorVectorList.append(SelectorOne)
    return SelectorVectorList

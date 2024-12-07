def Samples_AttributesFilter(SamplesInfDF,AttributeList,attributeList,Filter=[]):
    if len(AttributeList)==0:
        return []
    Filter=Samples_AttributesFilter(SamplesInfDF=SamplesInfDF,AttributeList=AttributeList[1:],attributeList=attributeList[1:])
    Attribute=AttributeList[0]
    attribute=attributeList[0]
    Filt=(SamplesInfDF[Attribute]==attribute)
    if len(Filter)>0:
        Filter=Filt&Filter
    else:
        Filter=Filt
    return Filter

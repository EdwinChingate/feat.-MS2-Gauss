from Samples_NFeatures_Filter import *
def SetsFeatures(AlignedSamplesDF,SamplesInfDF,FeaturesEffluentAppear=6,CarbonSource=['Aniline','Histidine', 'Succinate']):    
    SetsList=[]
    for carbon_source in CarbonSource:
        EffluentFilter,EffluentSamples_index=Samples_NFeatures_Filter(AlignedSamplesDF=AlignedSamplesDF,SamplesInfDF=SamplesInfDF,AttributeList=['Source','Primary carbon source'],attributeList=['Effluent',carbon_source],Min_Feat=FeaturesEffluentAppear)
        FeaturesIndex=set(AlignedSamplesDF[EffluentFilter].index)
        SetsList.append(FeaturesIndex)
    return SetsList

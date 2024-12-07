from Samples_NFeatures_Filter import *
def RemoveBlankFeatures(AlignedSamplesDF,SamplesInfDF,FeaturesBlankAppear=2,FeaturesEffluentAppear=6,Min_Feat_Blank=4,CarbonSource=['Aniline','Histidine', 'Succinate'],BlankSource=['EffluentClean', 'Influent', 'InfluentClean'],AllBlanksAllSamples=True):    
    FirstCS=True
    for carbon_source in CarbonSource:
        EffluentFilter,EffluentSamples_index=Samples_NFeatures_Filter(AlignedSamplesDF=AlignedSamplesDF,SamplesInfDF=SamplesInfDF,AttributeList=['Source','Primary carbon source'],attributeList=['Effluent',carbon_source],Min_Feat=FeaturesEffluentAppear)
        FirstBlank=True
        for blank_source in BlankSource:
            BlankSamplesLoc=Samples_NFeatures_Filter(AlignedSamplesDF=AlignedSamplesDF,SamplesInfDF=SamplesInfDF,AttributeList=['Source','Primary carbon source'],attributeList=[blank_source,carbon_source],Min_Feat=FeaturesBlankAppear,MoreThan=False)[0]
            if FirstBlank:
                BlankFilter=BlankSamplesLoc
                FirstBlank=False
            else:
                BlankFilter=BlankFilter&BlankSamplesLoc
        CS_Filter=(BlankFilter&EffluentFilter)       
        if FirstCS:
            Features_to_keep=CS_Filter
            Features_to_keepBlanks=BlankFilter
            FirstCS=False                
        else:
            Features_to_keep=Features_to_keep|CS_Filter      
            Features_to_keepBlanks=BlankFilter&Features_to_keepBlanks
    if AllBlanksAllSamples:
        Features_to_keep=Features_to_keep&Features_to_keepBlanks
    CarbonSourceFeatures=AlignedSamplesDF[Features_to_keep].copy()
    return CarbonSourceFeatures
    

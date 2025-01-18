from Samples_NFeatures_Filter import *
def RemoveBlankFeatures(AlignedSamplesDF,AlignedSamples_RT_DF,SamplesInfDF,FeaturesBlankAppear=2,FeaturesEffluentAppear=6,Min_Feat_Blank=4,CarbonSource=['Aniline','Histidine', 'Succinate'],BlankSource=['EffluentClean', 'Influent', 'InfluentClean'],AllBlanksAllSamples=True):    
    FirstCS=True
    ListEffluentSamples_index=['mz_(Da)','mz_std_(Da)','mz_ConfidenceInterval_(Da)','mz_ConfidenceInterval_(ppm)','RT_(s)','min_RT_(s)','max_RT_(s)']
    for carbon_source in CarbonSource:
        EffluentFilter,EffluentSamples_index=Samples_NFeatures_Filter(AlignedSamplesDF=AlignedSamplesDF,SamplesInfDF=SamplesInfDF,AttributeList=['Source','Primary carbon source'],attributeList=['Effluent',carbon_source],Min_Feat=FeaturesEffluentAppear)
        ListEffluentSamples_index=ListEffluentSamples_index+list(EffluentSamples_index)
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
    CarbonSourceFeatures_RT=AlignedSamples_RT_DF[Features_to_keep].copy()
    CarbonSourceFeatures=CarbonSourceFeatures[ListEffluentSamples_index]
    CarbonSourceFeatures_RT=CarbonSourceFeatures_RT[ListEffluentSamples_index]
    return [CarbonSourceFeatures,CarbonSourceFeatures_RT]

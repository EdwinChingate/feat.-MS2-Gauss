import numpy as np
import pandas as pd
import os
from JoiningFeatures import *
from ms2_SpectralSimilarityClustering import *
def Features_ms2_SamplesAligment(ResultsFolderName,mz_min=254,mz_max=255,RT_min=0,RT_max=2000,RT_tol=30,mz_Tol=0,min_Int_Frac=1,cos_tol=0.9,ToReplace='.mzML.xlsx',ms2Folder='ms2_spectra',ToAdd='mzML'):
    home=os.getcwd()
    ResultsFolder=home+'/'+ResultsFolderName
    All_FeaturesTable,SamplesNames=JoiningFeatures(ResultsFolder=ResultsFolder,mz_min=mz_min,mz_max=mz_max,RT_min=RT_min,RT_max=RT_max,ToReplace=ToReplace)
    Modules=ms2_SpectralSimilarityClustering(SummMS2_raw=All_FeaturesTable,SamplesNames=SamplesNames,mz_col=3,RT_col=2,RT_tol=RT_tol,mz_Tol=mz_Tol,sample_id_col=16,ms2_spec_id_col=15,ms2Folder=ms2Folder,ToAdd=ToAdd,min_Int_Frac=min_Int_Frac,cos_tol=cos_tol)
    N_samples=len(SamplesNames)
    N_Features=len(Modules)
    AlignedSamplesMat=np.zeros((N_Features,N_samples+2))
    for feature_id in np.arange(N_Features,dtype='int'):
        Feature_module=Modules[feature_id]
        FeatureTable=All_FeaturesTable[Feature_module,:]
        MaxInt=np.max(FeatureTable[:,5])
        MaxInt_Loc=np.where(FeatureTable[:,5]==MaxInt)[0]
        AlignedSamplesMat[feature_id,0]=FeatureTable[MaxInt_Loc,3]
        AlignedSamplesMat[feature_id,1]=FeatureTable[MaxInt_Loc,2]
        Samples_ids=np.array(FeatureTable[:,16],dtype='int')
        AlignedSamplesMat_loc=Samples_ids+2
        AlignedSamplesMat[feature_id,AlignedSamplesMat_loc]=FeatureTable[:,5]
    AlignedSamplesMat=AlignedSamplesMat[AlignedSamplesMat[:,0].argsort()]    
    Columns=['mz_(Da)']+['RT_(s)']+SamplesNames
    AlignedSamplesDF=pd.DataFrame(AlignedSamplesMat,columns=Columns)
    return AlignedSamplesDF

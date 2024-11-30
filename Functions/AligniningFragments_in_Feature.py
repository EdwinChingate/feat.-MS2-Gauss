import numpy as np
def AligniningFragments_in_Feature(Frag_Modules,All_ms2,N_features):
    N_Fragments=len(Frag_Modules)
    AlignedFragmentsMat=np.zeros((N_Fragments,N_features+1))
    for fragment_id in np.arange(N_Fragments,dtype='int'):
        Fragment_module=Frag_Modules[fragment_id]
        FragmentTable=All_ms2[Fragment_module,:]
        MaxInt=np.max(FragmentTable[:,2])
        MaxInt_Loc=np.where(FragmentTable[:,2]==MaxInt)[0]
        AlignedFragmentsMat[fragment_id,0]=FragmentTable[MaxInt_Loc,0]
        Fragments_ids=np.array(FragmentTable[:,10],dtype='int')
        AlignedFragmentsMat_loc=Fragments_ids+1
        AlignedFragmentsMat[fragment_id,AlignedFragmentsMat_loc]=FragmentTable[:,9]
    AlignedFragmentsMat=AlignedFragmentsMat[AlignedFragmentsMat[:,0].argsort()]    
    return AlignedFragmentsMat

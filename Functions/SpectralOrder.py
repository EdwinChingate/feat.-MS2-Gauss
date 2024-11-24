def SpectralOrder(Spectrum_1,Spectrum_2):
    L_spec1=len(Spectrum_1[:,0])
    L_spec2=len(Spectrum_2[:,0])
    if L_spec2>L_spec1:
        TempSpec=Spectrum_1.copy()
        Spectrum_1=Spectrum_2.copy()
        Spectrum_2=TempSpec
        L_temp=L_spec1
        L_spec1=L_spec2        
        L_spec2=L_temp
    return [Spectrum_1,Spectrum_2,L_spec1,L_spec2]

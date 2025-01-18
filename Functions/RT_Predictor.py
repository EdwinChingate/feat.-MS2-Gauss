import numpy as np
from scipy import stats
def RT_Predictor(CarbonSourceFeatures_RT):
    CarbonSourceFeatures_RT=CarbonSourceFeatures_RT.sort_values(by=['RT_(s)'])
    RT_vec=np.array(CarbonSourceFeatures_RT['RT_(s)']) 
    RT_SamplesMat=np.array(CarbonSourceFeatures_RT)[:,7:]#The column would change later when including the Confidence interval in ppm
    SamplesIds=CarbonSourceFeatures_RT.columns[7:]
    NSamples=len(RT_SamplesMat[0,:])
    for sample_id in np.arange(NSamples):
        SampleRT_vec=RT_SamplesMat[:,sample_id].copy()
        SignalLoc=SampleRT_vec>0
        if len(RT_vec[SignalLoc])>3:
            reg=stats.linregress(x=RT_vec[SignalLoc],y=SampleRT_vec[SignalLoc])
            m=reg[0]
            b=reg[1]
            r2=reg[2]**2
            SampleRT_vec[~SignalLoc]=RT_vec[~SignalLoc]*m+b
        else:
            SampleRT_vec[~SignalLoc]=RT_vec[~SignalLoc]
        RT_SamplesMat[:,sample_id]=SampleRT_vec
    CarbonSourceFeatures_RT[SamplesIds]=RT_SamplesMat
    return CarbonSourceFeatures_RT

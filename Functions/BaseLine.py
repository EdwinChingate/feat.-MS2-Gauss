from scipy import stats
def BaseLine(EarlyLoc,LateLoc,Chromatogram,RT_col=2,int_col=5,BaseLinePoints_2=3):
    N_spec=len(Chromatogram[:,0])
    EarlyBaseLine=EarlyLoc-BaseLinePoints_2
    if EarlyBaseLine<0:
        EarlyBaseLine=0    
    LateBaseLine=LateLoc+BaseLinePoints_2
    if LateBaseLine>N_spec:
        LateBaseLine=N_spec 
    EarlyBaseLineMat=Chromatogram[EarlyBaseLine:EarlyLoc,:]
    LateBaseLineMat=Chromatogram[LateLoc:LateBaseLine,:]
    BaseLineMat=np.append(EarlyBaseLineMat,LateBaseLineMat,axis=0)
    X=BaseLineMat[:,RT_col]
    Y=BaseLineMat[:,int_col]
    reg=stats.linregress(X,Y)
    m=reg[0]
    b=reg[1]
    r2=reg[2]**2
    BL=Chromatogram[EarlyLoc:LateLoc,2]*m+b    
    return BL

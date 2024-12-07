import pandas as pd
def SamplesNames_from_List(SamplesInfName):
    SamplesInfDF=pd.read_excel(SamplesInfName,index_col=0)
    return SamplesInfDF

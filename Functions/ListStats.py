import numpy as np
def ListStats(DataList):
    Data_mean=np.mean(DataList)
    Data_std=np.std(DataList)
    return [Data_mean,Data_std,Data_mean-Data_std]

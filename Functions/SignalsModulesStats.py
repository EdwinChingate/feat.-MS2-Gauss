import numpy as np
def SignalsModulesStats(Modules,SignalVec):
    ModulesStats=[]
    for module in Modules:
        Signals=SignalVec[module]
        Signals_mean=np.mean(Signals)
        Signals_std=np.std(Signals)
        Signals_max=np.max(Signals)
        Signals_min=np.min(Signals)
        NSignals=len(module)
        ModulesStats.append([Signals_mean,Signals_std,Signals_max,Signals_min,NSignals])
    ModulesStats=np.array(ModulesStats)
    ModulesStats=ModulesStats[ModulesStats[:,2].argsort(),:]
    return ModulesStats

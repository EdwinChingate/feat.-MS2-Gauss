import matplotlib.pyplot as plt
def PlotSpec(RawSpectrum,xlim=[],ylim=[],show=True):
    if len(xlim)>0:
        plt.xlim(xlim)
    if len(ylim)>0:
        plt.ylim(ylim)
    plt.plot(RawSpectrum[:,0],RawSpectrum[:,1],'.')
    if show:
        plt.show()

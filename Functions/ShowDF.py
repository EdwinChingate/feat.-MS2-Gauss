from IPython.display import HTML, display
import tabulate	
import numpy as np
import pandas as pd
def ShowDF(DF,col=''):
    if type(DF)==type(np.zeros((0))):
        DF=pd.DataFrame(DF)
    if col=='':
        col=list(DF.columns)
    display(HTML(tabulate.tabulate(DF[col], headers= col,tablefmt='html')))    

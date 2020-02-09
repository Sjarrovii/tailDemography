import pandas as pd
import numpy as np

def candidate(m,dv,placement=(1,1)):
    assert(dv in m.columns)
    return m[dv].sort_values().reset_index().iloc[placement[0]:placement[1]+1,:]

def topcorr(corrdf,lowestrank,dvs):
"""
param: corrdf

param: lowestrank:  this sets the number of ranks to be returned

param: dvs: The list of dependant variables to be correlated against those in the _corrdf_
"""
    candidates = [candidate(corrdf,dv,(1,lowestrank)) for dv in dvs]
    merger =  reduce(lambda x, y: pd.merge(x, y, on = 'index', how = 'outer'), candidates).fillna('--')
    return merger
    
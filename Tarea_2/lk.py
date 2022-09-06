import dask.array as da
import pandas as pd
import numpy as np

def generate_lk(n, lkmax, N):

    assert(n>=5) 

    if n % 2 == 0:

        m = int(n/2 - 1)
        
        lk = da.random.randint(-lkmax, lkmax+1, (N, m+m))
        lk = lk.to_dask_dataframe().drop_duplicates().to_dask_array()
        lk = lk.compute()

        l1 = (lk[:, 0] == 0)
        lk[:, 0][l1] = np.random.randint(1, lkmax+1, lk[:, 0][l1].shape)*(-1)**da.random.randint(0, 2, lk[:, 0][l1].shape)
        
        k1 = (lk[:, m] == 0)
        lk[:, m][k1] = np.random.randint(1, lkmax+1, lk[:, 0][k1].shape)*(-1)**da.random.randint(0, 2, lk[:, 0][k1].shape)

        lk = np.unique(lk, axis=0)
        
        return lk

    if n % 2 != 0:

        m = int((n-3)/2)
        
        lk = da.random.randint(-lkmax, lkmax+1, (N, m+m+1))
        lk = lk.to_dask_dataframe().drop_duplicates().to_dask_array()
        lk = lk.compute()

        l1 = (lk[:, 0] == 0)
        lk[:, 0][l1] = np.random.randint(1, lkmax+1, lk[:, 0][l1].shape)*(-1)**da.random.randint(0, 2, lk[:, 0][l1].shape)
        
        k1 = (lk[:, m] == 0)
        lk[:, m][k1] = np.random.randint(1, lkmax+1, lk[:, 0][k1].shape)*(-1)**da.random.randint(0, 2, lk[:, 0][k1].shape)

        lk = np.unique(lk, axis=0)
        
        return lk

    else:
        
        raise RuntimeError("What is that input you gave me!")
    
   
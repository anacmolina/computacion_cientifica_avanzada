import dask.array as da
import pandas as pd

def generate_lk(n, lkmax, N):

    assert(n>=5)

    if n % 2 == 0:

        m = int(n/2 - 1)
        
        lk = da.random.randint(0, lkmax, (N, m+m))*(-1)**da.random.randint(0, 2, (N, m+m))
    
        lk[:, 0] = da.random.randint(1, lkmax+1, (1, N))*(-1)**da.random.randint(0, 2, (1, N))
        lk[:, m] = da.random.randint(1, lkmax+1, (1, N))*(-1)**da.random.randint(0, 2, (1, N))
        
        return lk

    if n % 2 != 0:

        m = int((n-3)/2)
        
        lk = da.random.randint(0, lkmax+1, (N, m+m+1))*(-1)**da.random.randint(0, 2, (N, m+m+1))

        lk[:, 0] = da.random.randint(1, lkmax+1, (1, N))*(-1)**da.random.randint(0, 2, (1, N))
        lk[:, m] = da.random.randint(1, lkmax+1, (1, N))*(-1)**da.random.randint(0, 2, (1, N))
        
        return lk

    else:
        
        raise RuntimeError("What is that input you give me!")
    
   
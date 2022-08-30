import numpy as np

def vectorlike_generator(n):

    assert(n>=5)

    upper = int(n/2 + 1)

    if n % 2 == 0:
    
        m = int(n/2 - 1)
        
        l = np.random.randint(0, upper, m)*(-1)**np.random.randint(0, 2, m)
        k = np.random.randint(0, upper, m)*(-1)**np.random.randint(0, 2, m)

        l[0] = np.random.randint(1, upper, 1)*(-1)**np.random.randint(0, 2, 1)
        k[0] = np.random.randint(1, upper, 1)*(-1)**np.random.randint(0, 2, 1)

    elif n % 2 != 0:
    
        m = int((n-3)/2)
    
        l = np.random.randint(0, upper, m)*(-1)**np.random.randint(0, 2, m)
        k = np.random.randint(0, upper, m+1)*(-1)**np.random.randint(0, 2, m+1)

        l[0] = np.random.randint(1, upper, 1)*(-1)**np.random.randint(0, 2, 1)
        k[0] = np.random.randint(1, upper, 1)*(-1)**np.random.randint(0, 2, 1)

    else:
        
        raise RuntimeError("The input is wrong!")
    
    return l, k
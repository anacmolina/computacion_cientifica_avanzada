import numpy as np
import matplotlib.pyplot as plt

def linear_combination(x, y):

    result = np.sum(x*(y**2))*x - np.sum((x**2)*y)*y
    gcd = np.gcd.reduce(result)

    if (gcd==0):
        result = sorted_absval(result)
    else:
        result = sorted_absval(result/gcd)

    return np.array(result).astype(int), gcd

def sorted_absval(x):

    return sorted(x, key=abs, reverse=True)

def vectorlike_sum(l, k, n):

    if (n % 2) == 0:
        
        vp = np.hstack([l[0], k, (-1)*l[0], (-1)*k])
        vm = np.hstack([0, 0, l, (-1)*l])
        
        return linear_combination(vp, vm)
    
    elif (n % 2) != 0:

        up = np.hstack([0, k, (-1)*k])
        um = np.hstack([l, k[0], 0, (-1)*l, (-1)*k[0]])
        
        return linear_combination(vp, vm)

    else:

        raise RuntimeError("The input is wrong!")

def vectorlike_generator(n):

    assert(n>=5)
    
    upper = int(n/2)

    if n % 2 == 0:
    
        m = int(n/2 - 1)
        
        l = np.random.randint(1, upper, m)*(-1)**np.random.randint(0, 2, m)
        k = np.random.randint(1, upper, m)*(-1)**np.random.randint(0, 2, m)
    
    elif n % 2 != 0:
    
        m = int((n-3)/2 - 1)
    
        l = np.random.randint(1, upper, m)*(-1)**np.random.randint(0, 2, m)
        k = np.random.randint(1, upper, m+1)*(-1)**np.random.randint(0, 2, m)
    
    else:
        
        raise RuntimeError("The input is wrong!")
    
    return l, k

def find_anomaly_free_set(n, z1):

    l, k = vectorlike_generator(n)
    z, gcd = vectorlike_sum(l, k, n)

    N = np.unique(z).size
    N_unique = np.unique(np.abs(z)).size

    if ( (N==N_unique) and (np.abs(z).min()>0) and np.abs(z[0])<=z1) :

        return z, gcd, k, l

    else:
        
        return find_anomaly_free_set(n, z1)

n = 6#30

z_ = find_anomaly_free_set(n, 12)

print(z_)
z_ = z_[0]
print(z_, z_.sum(), (z_**3).sum())

l = np.array([1, 2])
k = np.array([1, -2])

z, gcd = vectorlike_sum(l, k, n)

print(gcd, z, z.sum(), (z**3).sum())

# funtion to sorted accoding to the absolute value
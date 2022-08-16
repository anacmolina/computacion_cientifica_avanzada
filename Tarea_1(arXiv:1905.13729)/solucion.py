import numpy as np
import matplotlib.pyplot as plt

n = 30

def linear_combination(x, y):
    return np.sum(x*(y**2))*x - np.sum((x**2)*y)*y

def anomaly_free_set(l, k):
    
    m = n/2 - 1

    if (n % 2) == 0:
        
        vp = np.hstack([l[0], k, (-1)*l[0], (-1)*k])
        vm = np.hstack([0, 0, l, (-1)*l])
        
        return linear_combination(vp, vm)
    
    elif (n % 2) != 0:

        up = np.hstack([0, k, (-1)*k])
        um = np.hstack([l, k[0], 0, (-1)*l, (-1)*k[0]])
        
        return linear_combination(vp, vm)

    else:
        raise RuntimeError("The input is wrong! Fix it!")



l = np.array([1, -1])
k = np.array([2, 0])

z = anomaly_free_set(l, k)

print(z, z.sum(), (z**3).sum())

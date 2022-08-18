import numpy as np
import matplotlib.pyplot as plt

n = 30

def linear_combination(x, y):
    result = np.sum(x*(y**2))*x - np.sum((x**2)*y)*y
    return np.array(sorted_absval(result)).astype(int)

def sorted_absval(x):
    return sorted(x, key=abs, reverse=True)

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
        raise RuntimeError("The input is wrong!")

def number_generator(n):

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

x_ = np.random.randint(1, 6, 6)*(-1)**np.random.randint(0, 2, 6)

print(sorted_absval(x_))

print(number_generator(6))

l = np.array([1, 2])
k = np.array([1, -2])

z = anomaly_free_set(l, k)

print(z, z.sum(), (z**3).sum())

# funtion to sorted accoding to the absolute value
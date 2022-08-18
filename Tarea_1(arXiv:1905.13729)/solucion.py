import numpy as np
import matplotlib.pyplot as plt

def sorted_absval(x):
    return np.array(sorted(x, key=abs, reverse=True))

def linear_combination(x, y):

    result = np.sum(x*(y**2))*x - np.sum((x**2)*y)*y

    result = sorted_absval(result).astype(int)

    if(result[0]<0):
        result = result*(-1)

    gcd = np.gcd.reduce(result)

    if (gcd!=0):
        result = result/gcd
    else:
        result = result

    return result.astype(int), gcd


def vectorlike_sum(l, k, n):

    if (n % 2) == 0:
        
        vp = np.hstack([l[0], k, (-1)*l[0], (-1)*k])
        vm = np.hstack([np.zeros(2), l, (-1)*l])

        """
        vp = np.array([])
        vm = np.array([])

        for vp_ in [l[0], k, (-1)*l[0], (-1)*k]:
            vp = np.append(vp, vp_)
        
        for vm_ in [np.zeros(2), l, (-1)*l]:
            vm = np.append(vm, vm_)

        #print(vp, vm)

        vp = vp.flatten()
        vm = vm.flatten()
        """

        return linear_combination(vp, vm)
    
    elif (n % 2) != 0:

        up = np.hstack([np.zeros(1), k, (-1)*k])
        um = np.hstack([l, k[0], np.zeros(1), (-1)*l, (-1)*k[0]])

        """
        up = np.array([])
        um = np.array([])

        for up_ in [np.zeros(1), k, (-1)*k]:
            up = np.append(up, up_)
        
        for um_ in [l, k[0], np.zeros(1), (-1)*l, (-1)*k[0]]:
            um = np.append(um, um_)

        #print(vp, vm)

        up = up.flatten()
        um = um.flatten()
        """
        
        return linear_combination(up, um)

    else:

        raise RuntimeError("The input is wrong!")

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

def find_anomaly_free_set(n, z1):

    l, k = vectorlike_generator(n)
    z, gcd = vectorlike_sum(l, k, n)

    N = np.unique(z).size
    N_unique = np.unique(np.abs(z)).size

    if ( (N==N_unique) and (np.abs(z).min()>0) and np.abs(z[0])<=z1 
        and z.sum()==0 and (z**3).sum()==0 ) :

        return z, gcd, k, l

    else:
        
        return find_anomaly_free_set(n, z1)

def find_several_sets(n, z1, iters):

    sets = []

    for i in range(iters):
        set = find_anomaly_free_set(n, z1)
        sets.append(set)

    return sets

def print_results(z, gcd, l, k):
    print('\n')
    print( 'Set: ', z )
    print( 'l: ', l )
    print( 'k: ', k )
    print( 'gcd: %d '%(gcd) )
    print( 'sum(zi) = %d \t sum(z_i^3) = %d'%(z.sum(), (z**3).sum()) )

"""
print("Test for knowns l and k")

l = np.array([1, 2])
k = np.array([1, -2])
z, gcd = vectorlike_sum(l, k, 6)

print_results(z, gcd, l, k)
"""

#"""

print('\nOne set for n=6 and z1 <= 12')

n = 6
z1 = 12
iters = 100

set = find_anomaly_free_set(n, z1)

print_results(*set)

print('\nPrimitive sets for n=6 and z1 <= 12')

sets = find_several_sets(n, z1, iters)

z = np.array(sets)[:, 0]
z = np.vstack(z)

print(np.unique(z, axis=0))

#"""

print('\nOne set for n=30')

n = 30
z1 = 1500
iters = 5

set = find_anomaly_free_set(n, z1)

print_results(*set)

print('\nPrimitive sets for n=30')

sets = find_several_sets(n, z1, iters)

z = np.array(sets)[:, 0]
z = np.vstack(z)

print(np.unique(z, axis=0))


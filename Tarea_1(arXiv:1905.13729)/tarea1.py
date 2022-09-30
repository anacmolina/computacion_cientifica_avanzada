import time as time
import numpy as np
import pandas as pd

import warnings

warnings.filterwarnings("ignore")


def sorted_absval(x):
    return np.array(sorted(x, key=abs, reverse=True))


def linear_combination(x, y):

    result = np.sum(x * (y**2)) * x - np.sum((x**2) * y) * y

    result = sorted_absval(result).astype(int)

    if result[0] < 0:
        result = result * (-1)

    gcd = np.gcd.reduce(result)

    if gcd != 0:
        result = result / gcd
    else:
        result = result

    return result.astype(int), gcd


def vectorlike_sum(l, k, n):

    if (n % 2) == 0:

        vp = np.hstack([l[0], k, (-1) * l[0], (-1) * k])
        vm = np.hstack([np.zeros(2), l, (-1) * l])

        return linear_combination(vp, vm)

    elif (n % 2) != 0:

        up = np.hstack([np.zeros(1), k, (-1) * k])
        um = np.hstack([l, k[0], np.zeros(1), (-1) * l, (-1) * k[0]])

        return linear_combination(up, um)

    else:

        raise RuntimeError("The input is wrong!")


def vectorlike_generator(n, zmax):

    assert n >= 5

    upper = int(zmax / 2)

    if n % 2 == 0:

        m = int(n / 2 - 1)

        l = np.random.randint(0, upper, m) * (-1) ** np.random.randint(0, 2, m)
        k = np.random.randint(0, upper, m) * (-1) ** np.random.randint(0, 2, m)

        l[0] = np.random.randint(1, upper, 1) * (-1) ** np.random.randint(0, 2, 1)
        k[0] = np.random.randint(1, upper, 1) * (-1) ** np.random.randint(0, 2, 1)

    elif n % 2 != 0:

        m = int((n - 3) / 2)

        l = np.random.randint(0, upper, m) * (-1) ** np.random.randint(0, 2, m)
        k = np.random.randint(0, upper, m + 1) * (-1) ** np.random.randint(0, 2, m + 1)

        l[0] = np.random.randint(1, upper, 1) * (-1) ** np.random.randint(0, 2, 1)
        k[0] = np.random.randint(1, upper, 1) * (-1) ** np.random.randint(0, 2, 1)

    else:

        raise RuntimeError("The input is wrong!")

    return l, k


def find_anomaly_free_set(n, zmax):

    l, k = vectorlike_generator(n, zmax)
    z, gcd = vectorlike_sum(l, k, n)

    N = np.unique(z).size
    N_unique = np.unique(np.abs(z)).size

    if (
        (N == N_unique)
        and (np.abs(z).min() > 0)
        and np.abs(z[0]) <= zmax
        and z.sum() == 0
        and (z**3).sum() == 0
    ):

        results = {"z": z, "l": l, "k": k, "gcd": gcd}

        return results

    else:

        return find_anomaly_free_set(n, zmax)


def find_several_sets(n, zmax, iters):

    sets = []

    for i in range(iters):
        set = find_anomaly_free_set(n, zmax)
        sets.append(set)

    return sets


def print_set_info(z, l, k, gcd):
    df = pd.DataFrame(columns=["z", "l", "k", "gcd"])
    df["z"] = [z]
    df["l"] = [l]
    df["k"] = [k]
    df["gcd"] = gcd

    print(df)
    print("sum(zi) = {} \t sum(z_i^3) = {}".format(z.sum(), ((z) ** 3).sum()))
    del df


print("------------------------------------------------")
print("Calculating 'z' for a known 'l' and 'k':\n")

l = np.array([1, 2])
k = np.array([1, -2])
z, gcd = vectorlike_sum(l, k, 6)

test_info = {"z": z, "l": l, "k": k, "gcd": gcd}
print_set_info(**test_info)

print("------------------------------------------------")
print("Find one set for n = 5 and zmax <= 30:\n")

n = 5
zmax = 30

set = find_anomaly_free_set(n, zmax)
print_set_info(**set)

print("------------------------------------------------")
print("Find one set for n = 6 and zmax <= 30:\n")

n = 6
zmax = 30

set = find_anomaly_free_set(n, zmax)
print_set_info(**set)

print("------------------------------------------------")
print("Sets for n=6 and zmax <= 30")

iters = 2000
ti = time.time()

sets = find_several_sets(n, zmax, iters)

df = pd.DataFrame(sets)
df = df.sort_values(by=["gcd"], ignore_index=True)
df["copy"] = df["z"].astype(str)
df = df.drop_duplicates("copy").drop("copy", axis="columns").reset_index(drop=True)

tf = time.time() - ti

print("Time : {:.2f}s".format(tf))


df.to_csv("solutions_n6_zmax30.csv", index=False)

print("# Solutions: {}".format(df.shape[0]))
print("Solutions save in file -> solutions_n6_zmax30.csv")
print("------------------------------------------------")

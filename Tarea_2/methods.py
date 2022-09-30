import pandas as pd
import numpy as np

from anomalies import anomaly
import dask.array as da
import multiprocessing as multiprocessing


def generate_lk(n, lkmax, N):

    assert n >= 5

    if n % 2 == 0:

        m = int(n / 2 - 1)

        lk = da.random.randint(-lkmax, lkmax + 1, (N, m + m))
        lk = lk.to_dask_dataframe().drop_duplicates().to_dask_array()
        lk = lk.compute()

        l1 = lk[:, 0] == 0
        lk[:, 0][l1] = np.random.randint(1, lkmax + 1, lk[:, 0][l1].shape) * (
            -1
        ) ** da.random.randint(0, 2, lk[:, 0][l1].shape)

        k1 = lk[:, m] == 0
        lk[:, m][k1] = np.random.randint(1, lkmax + 1, lk[:, 0][k1].shape) * (
            -1
        ) ** da.random.randint(0, 2, lk[:, 0][k1].shape)

        lk = np.unique(lk, axis=0)

        return lk

    if n % 2 != 0:

        m = int((n - 3) / 2)

        lk = da.random.randint(-lkmax, lkmax + 1, (N, m + m + 1))
        lk = lk.to_dask_dataframe().drop_duplicates().to_dask_array()
        lk = lk.compute()

        l1 = lk[:, 0] == 0
        lk[:, 0][l1] = np.random.randint(1, lkmax + 1, lk[:, 0][l1].shape) * (
            -1
        ) ** da.random.randint(0, 2, lk[:, 0][l1].shape)

        k1 = lk[:, m] == 0
        lk[:, m][k1] = np.random.randint(1, lkmax + 1, lk[:, 0][k1].shape) * (
            -1
        ) ** da.random.randint(0, 2, lk[:, 0][k1].shape)

        lk = np.unique(lk, axis=0)

        return lk

    else:

        raise RuntimeError("What is that input you gave me!")


def compute_z(lk, zmax=30):

    n = len(lk)

    l, k = lk[: int(n / 2)].flatten(), lk[int(n / 2) :].flatten()

    z_ = anomaly.free(l, k)

    if z_[0] < 0:
        z_ = (-1) * z_

    gcd = np.gcd.reduce(z_)

    if gcd == 0:
        z = z_
    else:
        z = (z_ / gcd).astype(int)

    if 0 in z:

        return {}

    elif np.abs(z).max() > zmax:

        return {}

    elif np.unique(np.abs(z)).shape != np.unique(z).shape:

        return {}

    else:

        results = {
            "l": l.tolist(),
            "k": k.tolist(),
            "z": z.tolist(),
            "gcd": gcd,
        }

        return results


def find_all_z(n, lkmax, N):

    lk = generate_lk(n, lkmax, N)

    pool = multiprocessing.Pool()
    results = pool.map(compute_z, lk)

    return results


def solution_set(n, lkmax, N):

    zs = find_all_z(n, lkmax, N)

    all_zs = [d for d in zs if d]

    df = pd.DataFrame(all_zs)
    df = df.sort_values(by=["gcd"], ignore_index=True)

    df["copy"] = df["z"].astype(str)
    df = df.drop_duplicates("copy").drop("copy", axis="columns").reset_index(drop=True)

    return df

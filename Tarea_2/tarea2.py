# Usar anomalies python package
# Implementar multiprocessing para calcular las soluciones

import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

from anomalies import anomaly
from methods import solution_set
import time as time

n = [5, 6]
lkmax = [6, 9]
N = [500, 50000]

ti = time.time()
df_5 = solution_set(n[0], lkmax[0], N[0])
tf = time.time() - ti

print("-----------------------------------------------------")

print("n = {}, lkmax = {}, N = {}, zmax = 30".format(n[0], lkmax[0], N[0]))
print("# Solution: {}".format(df_5.shape[0]))
print("Time : {:.2f}s".format(tf))

df_5.to_csv("solutions_n5_zmax30.csv", index=False)

ti = time.time()
df_6 = solution_set(n[1], lkmax[1], N[1])
tf = time.time() - ti

print("-----------------------------------------------------")

print("n = {}, lkmax = {}, N = {}, zmax = 30".format(n[1], lkmax[1], N[1]))
print("# Solution: {}".format(df_6.shape[0]))
print("Time : {:.2f}s".format(tf))

df_6.to_csv("solutions_n6_zmax30.csv", index=False)

print("-----------------------------------------------------")

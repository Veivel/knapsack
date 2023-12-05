'''
runs & compares Unbounded Knapsack DP & BnB
for each dataset. 
'''

import numpy as np
import time
import tracemalloc
import sys
import dp as dp
import bnb_v1 as bnb
import dataset

orig_stdout = sys.stdout
f = open('output.txt', 'w')

# comment this out to print to stdout
sys.stdout = f

for key, filename in {
  "small": "dataset/small.txt",
  "medium": "dataset/medium.txt",
  "large": "dataset/large.txt",
}.items():
  print(f"\n({key})")
  lst, W = dataset.read_dataset(filename)
  
  for alg_name, run_alg in {
    "dynamic programming": dp.unbounded_knapsack_dp, 
    "branch and bound": bnb.unbounded_knapsack_bnb,
  }.items():
    tracemalloc.start()
    ts_1 = time.time()
    res = run_alg(lst, W) 
    ts_2 = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"----- {alg_name} -----")
    print(f"> cost: {sum([x[1] for x in res])}")
    print(f"> memory usage: current {current / 10**5} MB, peak {peak / 10**6} MB")
    print(f"> time taken: {ts_2 - ts_1:.4f}s")

sys.stdout = orig_stdout
f.close()
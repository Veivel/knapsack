'''
runs & compares Unbounded Knapsack DP & BnB
for each dataset. 
'''

import numpy as np
import time
import tracemalloc
import sys
import unbounded_knapsack as uk
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
    "dynamic programming": uk.unbounded_knapsack_dp, 
    "branch and bound": uk.unbounded_knapsack_bnb,
  }.items():
    tracemalloc.start()
    ts_1 = time.time()
    run_alg(lst, W) 
    ts_2 = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"----- {alg_name} -----")
    print(f"> memory usage: current {current / 10**5} MB, peak {peak / 10**6} MB")
    print(f"> time taken: {ts_2 - ts_1:.4f}s")

sys.stdout = orig_stdout
f.close()
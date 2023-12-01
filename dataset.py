'''
Generate & read dataset
'''

import numpy as np
import time
import random
import re

def read_dataset(filename: str) -> (list, int):
  '''
  Reads dataset from disk
  
  Returns
  -----
  arr: list of (weight, value) pairs
  W: maximum capaciy
  '''
  with open(filename, 'r') as f:
    txt = f.readlines()
    arr = []
    W = 0
    for i, line in enumerate(txt):
      if i == 0:
        W = int(line.strip())
      else:
        pair = re.sub(r'[\(\)]', "", line.strip()).split(",")
        arr.append((int(pair[0]), int(pair[1])))
  return arr, W

def generate_dataset() -> None:
  '''
  Generates a randomized dataset for the given size, 
  including (weight, value) pairs and max knapsack capacity.
  '''
  print(f"dataset generated at: {time.ctime(time.time())}\n")
  for key, n in {
    "small": 10**2,
    "medium": 10**3,
    "large": 10**4,
  }.items():
    arr = [ (random.randint(1, i+1), random.randint(1, i+1)) for i in range(n) ]
    W = random.randint(5, (n//10)*5)
    arr.insert(0, W)
    
    np.savetxt(f"dataset/{key}.txt", arr, delimiter =",", fmt ='% s')
      
if __name__ == "__main__":
  # generate_dataset()
  
  arr, W = read_dataset("./dataset/medium.txt")
  print(arr)
  print(W)
  
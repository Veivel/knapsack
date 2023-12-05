def unbounded_knapsack_dp(items, W) -> list:
  '''
  ASSUME: all weight and value are integers
  
  Parameters
  -----
  W: maximum weight
  items: list of n items of tuples (weight, value)
  
  Returns
  -----
  choices: list of tuples (weight, value); items chosen for knapsack
  '''
  
  n = len(items)
  # dp[i] stores maximum value achievable for knapsack of capacity 'i'
  dp = [0 for i in range(W + 1)] 
  # choices[i] stores selection of items made for knapsack of capacity 'i'
  choices = [[] for i in range(W + 1)]

  for i in range(W + 1): 
      for j in range(n): 
          if (items[j][0] <= i):
              with_j = dp[i - items[j][0]] + items[j][1]
              if with_j > dp[i]:
                dp[i] = with_j
                choices[i] = choices[i - items[j][0]] + [items[j]]
  return choices[W] 


if __name__ == "__main__":
  # item: (weight, value)
  # items = [(50, 99), (20, 49)]
  items = [(1, 10), (3, 40), (4, 50), (5, 70), (21, 290)]
  W = 6
  
  res = unbounded_knapsack_dp(items, W)
  total_value = sum([x[1] for x in res])
  print(res, total_value)
  

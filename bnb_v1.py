from queue import PriorityQueue

class Node:
  '''
  Single node
  '''
  def __init__(self, level, profit, weight, items_chosen):
    self.level = level
    self.profit = profit
    self.weight = weight
    self.items_chosen = items_chosen.copy()
    self.bound = 0 

  def __lt__(self, other):
    '''
    less than (<) operator
    '''
    return self.bound < other.bound

  def __gt__(self, other):
    '''
    greater than (>) operator
    '''
    return self.bound > other.bound

def bound(node, W, items):
    '''
    Find maximum possible value of a node
    
    Parameters
    -----
    node = node
    W = maximum capacity
    items = items
    
    Returns
    ----
    bound value
    '''
    n = len(items)
    if node.weight >= W: # kill
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_w = node.weight

    while j < n and total_w + items[j][0] <= W:
        total_w += items[j][0]
        profit_bound += items[j][1]
        j += 1

    if j < n:
        profit_bound += (W - total_w) * items[j][1] / items[j][0]

    return profit_bound

def unbounded_knapsack_bnb(items, W):
    '''
    ASSUME: all weight and value are integers
    
    Parameters
    -----
    items: list of n items of tuples (weight, value)
    W: maximum weight
    
    Returns
    -----
    choices: list of tuples (weight, value); items chosen for knapsack
    '''
    n = len(items)
    items.sort(key=lambda item: item[1] / item[0], reverse=True)
    u = Node(-1, 0, 0, [])
    max_profit_node = u

    queue = PriorityQueue()
    queue.put(u)

    while not queue.empty():
        u = queue.get()

        if u.level == -1:
            v = Node(0, 0, 0, [])
        elif u.level == n - 1:
            continue
        else:
            v = Node(u.level + 1, u.profit, u.weight, u.items_chosen)

        while v.weight + items[v.level][0] <= W:
            v.weight += items[v.level][0]
            v.profit += items[v.level][1]
            v.items_chosen.append(items[v.level])

            if v.weight <= W and v.profit > max_profit_node.profit:
                max_profit_node = v 

        v.bound = bound(v, W, items)

        if v.bound > max_profit_node.profit:
            queue.put(v)

        v = Node(u.level + 1, u.profit, u.weight, u.items_chosen)
        v.bound = bound(v, W, items)

        if v.bound > max_profit_node.profit: # kill branch if bound < max profit
            queue.put(v)

    return max_profit_node.items_chosen
  
if __name__ == "__main__":
  # item: (weight, value)
  # items = [(50, 99), (20, 49)]
  items = [(1, 10), (3, 40), (4, 50), (5, 70), (21, 290)]
  W = 23
  
  res = unbounded_knapsack_bnb(items, W)
  total_value = sum([x[1] for x in res])
  print(res, total_value)

  
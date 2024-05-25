## Characteristics
1. Local Optimization
   - best local optimum made each step leads up to the best global optimum
2. Irrevocability
   - once a choice is made, it cannot be undone or revisited unlike DP

## Related Problems
- Kruskal's or Prim's MST
- Dijikstra's Shortest Path
- Fractional Knapsack
- Activity Selection
- Greedy Best-First Search

### Boats to Save People Problem
```python
def numRescueBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0

    while i < j:
        # local optimum
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    
    # when the last person is left
    if i == j:
        boats += 1
    return boats 

```
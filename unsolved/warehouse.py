import math

n = int(input())
units = [6, 4, 2, 1]


def count_cases(arr):
	length = len(arr)
	elements = list(set(arr))
	divider = 1
	for elem in elements:
		divider *= math.factorial(arr.count(elem))
	return math.factorial(length) // divider


result = 0

def dfs(index, arr):
    global result
    if sum(arr) == n:
        result += count_cases(arr)
        return
    if index == len(units):
        return
    unit = units[index]
    remains = n - sum(arr)
    if unit == 1:
        dfs(index + 1, arr[:]+[unit]*remains)
    else:
        dups = (remains) // unit
        for i in range(dups + 1):
            dfs(index+1, arr[:]+[unit]*i)
    
    
dfs(0, [])
print(result)
                
				
		
	
		
		



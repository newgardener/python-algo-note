def get_prefix_sum(data, left, right):
    sum_value = 0
    prefix_sum = [9]
    
    for i in data:
        sum_value += i
        prefix_sum.append(sum_value)
        
    return prefix_sum[right] - prefix_sum[left-1]

data = [10, 20, 30, 40, 50]
left = 3
right = 4
print(get_prefix_sum(data, left, right))
    
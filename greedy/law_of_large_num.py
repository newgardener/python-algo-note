n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
first, second = nums[0], nums[1]

chunk = first * k + second
chunk_num = m // (k+1)
chunk_remains = m % (k+1)

result = chunk * chunk_num + chunk_remains * first

print(result)



    

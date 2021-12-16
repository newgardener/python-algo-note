#%% 빗물 트래핑
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trap(height):
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
            
    return volume

print(trap(height))

#%% 세 숫자의 합 = 0

nums = [-4, -1, -1, 0, 1, 2]

def three_sum(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # 세 숫자의 합이 0인 경우
                results.append([nums[i], nums[left], nums[right]])
                # two_pointers left, right에 대해서 중복 제거
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
    return results

print(three_sum(nums))
                
                
# %%

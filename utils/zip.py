# %% zip
from collections import Counter

nums = [1, 1, 1, 2, 2]
print(Counter(nums))
print(Counter(nums).most_common(2))

# unpacking 했을 때
print(list(zip(*Counter(nums).most_common(2))))

# unpacking 안했을 때
print(list(zip(Counter(nums).most_common(2))))

# %% sequence unpacking *

fruits = ["lemon", "pear", "watermelon", "tomato"]
print(*fruits)

a, *b = [1, 2, 3, 4]
print(a)
print(b)

# %% key/value pair unpacking **

data_info = {"year": "2021", "month": "12", "day": "28"}
new_info = {**data_info, "day": "29"}
print(new_info)

# %%

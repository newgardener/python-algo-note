# %%
from bisect import bisect_left


# Locate the leftmost value exactly equal to x
def index_of_x(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


a = [1, 2, 3, 3, 5]
print(index_of_x(a, 3))
print(index_of_x(a, 6))

# %%
from bisect import bisect_left


# Locate rightmost value less than x
def index_of_less_than_x(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    return None


a = [1, 3, 4, 6, 6, 7]
print(index_of_less_than_x(a, 6))
print(index_of_less_than_x(a, 4))


# %%
from bisect import bisect_right


# Locate the rightmost value less than or equal to x
def index_of_less_than_or_equal_than_x(a, x):
    i = bisect_right(a, x)
    if i:
        return i - 1
    return None


a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(index_of_less_than_or_equal_than_x(a, 15))

# %%
from bisect import bisect_right


# Locate the leftmost value greater than x
def index_of_greater_than_x(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return i
    return None


a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(index_of_greater_than_x(a, 17))
# %%
from bisect import bisect_left


# Locate the leftmost value greater than or equal to x
def index_of_greater_equal_than_x(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return i
    return None


a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(index_of_greater_equal_than_x(a, 3))
print(index_of_greater_equal_than_x(a, 5))

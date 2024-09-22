# %%
# add
s = {1, 2, 3}
s.add(4)
print(s)

# %%
# remove or discard
# remove raises KeyError if element is not found, whereas discard does not

s = {1, 2, 3}
# s.remove(4)
s.discard(4)
print(s)

# %%
# clear
# remove all elements in a set

s = {1, 2, 3}
s.clear()
print(s)

# %%
# union
# setA(a) + setB(b)

a = {1, 2}
b = {3, 4, 5}
print(a.union(b))

# %%
# intersection

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))

# %%
# difference

a = {1, 2, 3}
b = {2, 3}
print(a.difference(b))
print(b.difference(a))

# %%
# issubset
# set A belongs to B

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))


# %%
# issuperset
# set B is a superset of set A

a = {1, 2}
b = {1, 2, 3}
print(b.issuperset(a))

# %%
# array item deduplication using set

arr = [[1, 2], [1, 2]]

# convert inner list to tuple to make a set
unique_set = set(map(tuple, arr))
print(f"unique_set: {unique_set}")

# convert back to list of lists
result = list(map(list, unique_set))
print(f"result: {result}")

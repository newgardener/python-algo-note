# %% import Counter
from collections import Counter

# %% arithmetic operation
counter1 = Counter({"x": 4, "y": 2, "z": -2})
counter2 = Counter({"x": -12, "y": 5, "z": 4})

counter3 = counter1 + counter2
print(counter3)  # only positive values will be returned

counter4 = counter1 - counter2
print(counter4)

counter5 = counter1 & counter2
print(counter5)  # all common positive minimum values from counter 1 & 2

counter6 = counter1 | counter2
print(counter6)  # positive max values from counter 1 & 2


# %% method - elements
counter1 = Counter({"x": 5, "y": 2, "z": -1, "k": 0})
print(list(counter1.elements()))

# %% method - subtract
counter1 = Counter({"x": 5, "y": 12, "z": -2, "k": 0})
counter2 = Counter({"x": 2, "y": 5})

counter1.subtract("x")
print(counter1)

counter1.update(counter2)
print(counter1)

# %%

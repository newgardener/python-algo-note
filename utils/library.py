# %% 내장 함수

# sum, min, max
result = sum([1, 2, 3, 4, 5])
result1 = min([1, 2, 3, 4, 5])
result2 = max([1, 2, 3, 4, 5])
print(result, result1, result2)

# sorted
sorted_ascend = sorted([9, 1, 8, 5, 4])
sorted_descend = sorted([9, 1, 8, 5, 4], reverse=True)
sorted_tuple = sorted(
    [("홍길동", 35), ("이순신", 75), ("아무개", 50)], key=lambda x: x[1], reverse=True
)
print(sorted_ascend, sorted_descend, sorted_tuple)

# sort
data = [9, 1, 8, 5, 4]
data.sort()
print(data)

# %% itertools

from itertools import permutations
from itertools import combinations
from itertools import product

data = ["A", "B", "C"]
result_permute = list(permutations(data, 3))
result_combi = list(combinations(data, 2))
result_product = list(product(data, repeat=2))

print(result_permute)
print(result_combi)
print(result_product)

# %% bisect
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

# %% collections (1)
# dequeue - 첫번째 원소 제거 (popleft()), 마지막 원소 제거 (pop()), 첫번째 인덱스에 x 삽입 (appendleft(x)), 마지막 인덱스에 x 삽입 (append(x))

from collections import deque
from collections import Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])
print(counter)
print(counter["blue"])
print(counter.most_common(2))  # Counter 객체에서 빈도수가 가장 높은 top 2
print(dict(counter))

# %% collections (2)

from collections import defaultdict
from collections import OrderedDict

dict = defaultdict(int)
# 존재하지 않는 key에 대해서 KeyError를 발생시키지 않고 default 0을 기준으로 1을 더한 값을 value로
dict["A"] = 5
dict["B"] = 10
dict["C"] += 1

for k, v in dict.items():
    print(k, v)

ordered_dict = OrderedDict({"banana": 3, "apple": 2, "pear": 1, "orange": 2})
print(ordered_dict)

# %% collections (3)

from collections import defaultdict

A = [5, 7, 3, 7, 5, 8]

freq = defaultdict(int)

for num in A:
    freq[num] += 1

maxUnique = -1

for key, value in freq.items():
    if value == 1:
        maxUnique = max(maxUnique, key)

print(maxUnique)

# %%
from collections import OrderedDict

ordered_dict = OrderedDict({"x": 100, "y": 200, "z": 300})
print(ordered_dict)

# update
ordered_dict.update({"d": 400, "e": 500})
print(ordered_dict)

# popitem
lifo_popped = ordered_dict.popitem(last=True)
print(lifo_popped, ordered_dict)

# move_to_end(key, last)
ordered_dict.move_to_end("x", last=True)
print(ordered_dict)


# %% lambda
sum = lambda a, b: a + b
sum(3, 4)

# %% map
li = [1, 2, 3]
result = list(map(lambda x: x**2, li))
print(result)

el = [-3, -2, 0, 6, 8]
print(["양수" if i > 0 else ("음수" if i < 0 else 0) for i in el])
print(list(map(lambda i: "양수" if i > 0 else ("음수" if i < 0 else 0), el)))

# %% filter
li = [-2, -3, 5, 6]
list(filter(lambda x: x > 0, li))
# %% reduce
from functools import reduce

# reduce를 활용해 리스트의 합 구하기
acc = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(acc)  # ((((1+2)+3)+4)+5)

# reduce를 활용해 최대값 구하기
max_elem = reduce(lambda a, b: a if a > b else b, [10, 3, 5, 2, 1, 9])
print(max_elem)

# reduce를 이용해 문자 개수 세기
data = ["a", "a", "a", "b", "b", "c", "c", "c"]
data_counted = reduce(lambda a, b: a.update({b: a.get(b, 0) + 1}) or a, data, {})
print(data_counted)


# reduce를 활용한 data-grouping
def names_by_sex(acc, cur):
    sex = cur["sex"]
    if sex not in acc:
        acc[sex] = []
    acc[sex].append(cur["name"])
    return acc


users = [
    {"mail": "gregorythomas@gmail.com", "name": "Brett Holland", "sex": "M", "age": 73},
    {
        "mail": "hintoncynthia@hotmail.com",
        "name": "Madison Martinez",
        "sex": "F",
        "age": 29,
    },
    {"mail": "wwagner@gmail.com", "name": "Michael Jenkins", "sex": "M", "age": 51},
    {"mail": "daniel79@gmail.com", "name": "Karen Rodriguez", "sex": "F", "age": 32},
    {"mail": "ujackson@gmail.com", "name": "Amber Rhodes", "sex": "F", "age": 42},
]

grouped_by_sex = reduce(names_by_sex, users, {})
print(grouped_by_sex)

# %%
from collections import deque

d = deque("ghi")

d.append("j")
d.appendleft("f")
d.pop()
d.popleft()
list(d)
list(reversed(d))
d.extend("jkl")
d.rotate(1)  # right rotation
d.rotate(-1)  # left rotation

deque(reversed(d))
d.clear()
# d.pop()
d.extendleft("abc")
d


# %%
from collections import deque


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()


result = roundrobin("ABC", "D", "EF")
print(result, *result)

# %%

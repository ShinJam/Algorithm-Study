# N = int(input())
# nums = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
#
# min_, max_ = 1e9, -1e9
#
# def dfs(i, res, add, sub, mul, div):
#     global max_, min_
#     if i == N:
#         max_ = max(res, max_)
#         min_ = min(res, min_)
#         return
#
#     else:
#         if add:
#             dfs(i+1, res+nums[i], add-1, sub, mul, div)
#         if sub:
#             dfs(i+1, res-nums[i], add, sub-1, mul, div)
#         if mul:
#             dfs(i+1, res*nums[i], add, sub, mul-1, div)
#         if div:
#             dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)
#
# dfs(1, nums[0], add, sub, mul, div)
# print(max_)
# print(min_)


from itertools import permutations
from collections import deque
from copy import deepcopy

N = int(input())
nums = deque(list(input().split()))
add_, sub_, mul_, div_ = map(int, input().split())
check = dict()
value = []
candidate = ['+'] * add_ + ['-'] * sub_ + ['*'] * mul_ + ['/'] * div_

for case in permutations(candidate, len(candidate)):
    if check.get(''.join(case)):
        continue
    check[''.join(case)] = True
    temp = deepcopy(nums)

    for op in case:
        a = temp.popleft()
        b = temp.popleft()
        c = str(eval(a + op + b))

        temp.appendleft(str(int(float(c))))
    value.append(int(temp[0]))

print(max(value))
print(min(value))

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
start, end = 0, len(lst) - 1
check = float('inf')

while start < end:

    mid = lst[start] + lst[end]

    if abs(mid) < check:
        check = abs(mid)
        a, b = lst[start], lst[end]

    if mid == 0:
        break

    if mid < 0:
        start += 1
    else:
        end -= 1

print(a, b)





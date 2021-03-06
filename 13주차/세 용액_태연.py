import heapq

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
final_result = []
for i in range(len(lst)):
    new_lst = lst[:i] + lst[i + 1:]
    start, end = 0, len(new_lst) - 1
    check = float('inf')
    while start < end:
        mid = new_lst[start] + new_lst[end] + lst[i]

        if abs(mid) < check:
            check = abs(mid)
            result = [check, new_lst[start], new_lst[end], lst[i]]

        if mid == 0:
            break

        if mid < 0:
            start += 1
        else:
            end -= 1

    heapq.heappush(final_result, result)

a = [final_result[0][0], final_result[0][1], final_result[0][2]]
a.sort()
print(a[0], a[1], a[2])

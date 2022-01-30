import copy

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
final_result = []

for i in range(len(lst)):
    new_lst = copy.deepcopy(lst)
    new_lst.pop(i)
    start, end = 0, len(new_lst) -1
    check = float('inf')
    print(new_lst)
    while start < end:
        mid = new_lst[start] + new_lst[end] + lst[i]

        if abs(mid) < check:
            check = abs(mid)
            result = [new_lst[start], new_lst[end], lst[i], check]

        if mid == 0:
            break

        if mid < 0:
            start += 1
        else:
            end -= 1

    final_result.append(result)
print(final_result)
final_result.sort(key=lambda x:x[3])
a = [final_result[0][0], final_result[0][1], final_result[0][2]]
a.sort()
print(a[0], a[1], a[2])


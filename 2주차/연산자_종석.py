import copy
result = []
def back(lst, cnt, oper):
    global N, result
    if cnt == N-1:
        result.append(oper)
        return oper

    else:
        for j, oo in enumerate(lst):
            if oo == 0:
                continue
            else:
                op3 = copy.deepcopy(lst)

                op3[j] -= 1
                back(op3, cnt+1, oper + [j])

N = int(input())
numbers = list(map(int,input().split()))
op = list(map(int,input().split()))

for i, o in enumerate(op):
    if o == 0:
        continue
    else:
        op2 = copy.deepcopy(op)
        op2[i] -= 1
        back(op2, 1, [i])

final_result = []
for r in result:
    cnt = numbers[0]
    for w in range(len(numbers) -1):
        if r[w] == 0: # +
            cnt += numbers[w+1]
        elif r[w] == 1: # -
            cnt -= numbers[w+1]
        elif r[w] == 2: # *
            cnt *= numbers[w+1]
        elif r[w] == 3: # //
            if cnt < 0:
                cnt = -(-cnt // numbers[w+1])
            else:
                cnt = cnt // numbers[w+1]

    final_result.append(cnt)

print(max(final_result))
print(min(final_result))

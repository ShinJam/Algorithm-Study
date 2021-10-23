import copy


def back(s_idx, l_idx, cnt, case, lst):

    if cnt == 6:
        print(' '.join(map(str,lst)))
        return

    for i in range(s_idx, l_idx+1):
        lst2 = copy.deepcopy(lst)
        back(i+1, l_idx, cnt+1, case, lst2 + [case[i]])
    return


cases = []
while True:
    try:
        cases.append(list(map(int,input().split())))
    except:
        pass
    if len(cases[-1]) == 1:
        cases.pop()
        break

for i in range(len(cases)):
    back(1, cases[i][0], 0, cases[i], [])
    if i != len(cases)-1:
        print()


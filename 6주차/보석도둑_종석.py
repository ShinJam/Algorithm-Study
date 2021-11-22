# 아직 푸는중


N, K = map(int, input().split())
jewels = [list(map(int , input().split())) for _ in range(N)]
C = [int(input()) for _ in range(K)]
C.sort()
jewels.sort(key=lambda x: (-x[1] , x[0]))
visit_dict = {}
for i in range(len(C)):
    visit_dict[i] = C[i]
cnt = 0
for x, y in jewels:
    target = 'flag'
    for j, bag in visit_dict.items():

        if x <= bag:
            cnt += y
            target = j
            break
    if target == 'flag':
        continue
    else:

        del visit_dict[target]
        if not visit_dict:
            break

print(cnt)
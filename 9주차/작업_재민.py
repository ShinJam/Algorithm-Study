    cost = [0]*10001
    ans = 0
    for i in range(1, int(sys.stdin.readline())+1):
        cost[i], *prior = map(int, sys.stdin.readline().split())
        if len(prior) > 1:
            cost[i] += max(cost[p] for p in prior[1:])
        if ans < cost[i]:
            ans = cost[i]
    print(ans)

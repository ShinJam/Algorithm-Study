N, S = map(int, input().split())
NUMS = list(map(int, input().split()))

ACC = [0] * (N+1)
for i in range(1, N+1):
    ACC[i] = NUMS[i-1] + ACC[i-1]
    
ans = 1000001
i, j = 0, 1
while i < j and j <= N:
    if ACC[j] - ACC[i] >= S:
        ans = min(ans, j - i)
        i += 1
    else:
        j +=1
        
        
if ans == 1000001:
    ans = 0
print(ans)

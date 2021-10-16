import sys

input = sys.stdin.readline

N = int(input())

time = [0]*N
price = [0]*N
for i in range(N):
    time[i], price[i] = map(int, input().split())

ans = 0
def cal_price(day, cur_sum):
    global ans, N
    
    if day == N:
        ans = max(ans, cur_sum)
        return
    elif day > N:
        return
    
    # 포함
    cal_price(day+time[day], cur_sum + price[day])
    # 미포함
    cal_price(day+1, cur_sum)
    
cal_price(0, 0)
print(ans)

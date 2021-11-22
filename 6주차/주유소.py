N = int(input())
road_distance = list(map(int, input().split()))
price = list(map(int,input().split()))
price.pop()
total_d = sum(road_distance)
cnt = 0
check = 0
cur_min = 0

for d, p in zip(road_distance, price):
    if cnt == 0:
        cnt = total_d * p
        check = d * p
        total_d = total_d - d
        cur_min = p
    else:
        if cur_min < p:  # 현재 거리값과 이전 거리들 min 값을 계산해서 초기값을 나눠야함
            if cnt > check + (p * total_d):
                cnt = check + (p * total_d)
            check += d * cur_min
            total_d = total_d - d
        else:
            cur_min = p
            if cnt > check + (p * total_d):
                cnt = check + (p * total_d)
            check += d * cur_min
            total_d = total_d - d

print(cnt)

"""

5
3 2 1 4
5 8 9 4 1
answer = 46

"""
N, C = map(int, input().split())
house = [int(input()) for __ in range(N)]
house.sort()
answer = 0
start, end = 1, house[-1] - house[0]

while start <= end:

    mid = (start + end) // 2
    wifi_start = house[0]
    cnt = 1

    for i in range(1, len(house)):

        if house[i] >= wifi_start + mid:
            cnt += 1
            wifi_start = house[i]

    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1


print(answer)
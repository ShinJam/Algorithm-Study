N, S = map(int, input().split())
number = list(map(int, input().split()))
start, end = 0, 0
result = []
target = 0
while end <= N-1:
    target += number[end]
    if target >= S:
        result.append(end - start +1)

        while start <= end:
            target -= number[start]

            if target < S:
                start += 1

                break
            else:
                result.append(end - start)

            start += 1

    end += 1
if result:
    print(min(result))
else:
    print(0)
cnt = 0

def find(x, y, N, r, c):
    global cnt

    if N != 2:
        new_N = N // 2

        x_a, y_a = x + new_N, y + new_N

        if x <= r < x_a and y <= c < y_a:  # 1사분면
            find(x, y, new_N, r, c)

        elif x <= r < x_a and c >= y_a:  # 2사분면
            cnt += (new_N ** 2)
            find(x, y + new_N, new_N, r, c)

        elif r >= x_a and y <= c < y_a:  # 3사분면
            cnt += (new_N ** 2) * 2
            find(x + new_N, y, new_N, r, c)

        elif r >= x_a and c >= y_a:  # 4사분면
            cnt += (new_N ** 2) * 3
            find(x + new_N, y + new_N, new_N, r, c)

    else:
        for k in range(x, x + N):
            for w in range(y, y + N):
                cnt += 1

                if k == r and w == c:
                    cnt -= 1
                    return
        return

N, r, c = map(int,input().split())
find(0, 0, 2 ** N, r, c)
print(cnt)
N, r, c = list(map(int, input().split()))

def dfs(minV, maxV, x_left_index, x_right_index, y_left_index, y_right_index):
    if minV + 1 == maxV:
        print(minV)
        exit(0)

    d = (maxV - minV) // 4
    divide_V = [minV, minV + d, minV + 2 * d, minV + 3 * d, maxV]
    x_middle = (x_right_index - x_left_index) // 2
    y_middle = (y_right_index - y_left_index) // 2
    divide_x_index = [x_left_index, x_left_index + x_middle, x_right_index]
    divide_y_index = [y_left_index, y_left_index + y_middle, y_right_index]

    for i in range(2):  # find x range
        if divide_x_index[i] <= c < divide_x_index[i + 1]:
            x = i
            break

    for i in range(2):  # find y range
        if divide_y_index[i] <= r < divide_y_index[i + 1]:
            y = i
            break

    dfs(divide_V[x + 2 * y], divide_V[x + 2 * y + 1], divide_x_index[x], divide_x_index[x + 1], divide_y_index[y],
        divide_y_index[y + 1])


dfs(0, 2 ** (2 * N), 0, 2 ** N, 0, 2 ** N)

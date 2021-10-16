def z(x, y, index, cnt):
  if index == 0:
    print(cnt)
    return

  d = int(2**(index-1))

  if (x <= r < x+d) and (y <= c < y+d):
    z(x, y, index - 1, cnt)
  elif (x <= r < x+d) and (y+d <= c):
    z(x, y + d, index - 1, cnt + d*d)
  elif (x+d <= r) and (y <= c < y+d):
    z(x + d, y, index - 1, cnt + d*d*2)
  elif (x+d <= r) and (y+d <= c):
    z(x + d, y + d, index - 1, cnt + d*d*3)


if __name__ == "__main__":
  n, r, c = map(int, input().split())
  z(0, 0, n, 0)

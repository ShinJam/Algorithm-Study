N = int(input())
temp = list(map(int, input().split()))
temp.sort()

left, right = 0, len(temp) - 1
LEFT, RIGHT = temp[0], temp[-1]

while left < right:
    if temp[right] + temp[left] == 0:
        LEFT, RIGHT = temp[left], temp[right]
        break
    
    if abs(temp[left] + temp[right]) < abs(LEFT + RIGHT):
        LEFT, RIGHT = temp[left], temp[right]

    if temp[left] + temp[right] < 0:
        left += 1
    else:
        right -= 1

print(LEFT, RIGHT)

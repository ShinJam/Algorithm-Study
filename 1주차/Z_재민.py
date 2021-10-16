N, r, c = map(int, input().split())

def recursive(l, r, c, num=0):

    if l == 0:
        return num
    
    half_l = l // 2
    if r < half_l:
        if c < half_l: # 1 사분면 
            return recursive(half_l, r, c, num)
        else: # 2 사분면
            return recursive(half_l, r, c - half_l, num + half_l ** 2)
    else:
        if c < half_l: # 3 사분면
            return recursive(half_l, r- half_l, c , num + (half_l ** 2)*2)
        else: # 4 사분면
            return recursive(half_l, r- half_l, c- half_l , num + (half_l ** 2)*3)
        
ans = recursive(2**N, r, c)
print(ans)

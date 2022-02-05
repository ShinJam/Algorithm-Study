from collections import defaultdict


def solution(gems):
    result = [0, len(gems)]
    kinds = len(set(gems))
    current = defaultdict(int)

    l, r = 0, 0
    while r <= len(gems):
        if len(current) == kinds:
            if result[1] - result[0] > r -1 - l:
                result = [l + 1, r ]
                
            current[gems[l]] -= 1
            if current[gems[l]] == 0:
                del current[gems[l]]
            l += 1

        else:
            if r < len(gems):
                current[gems[r]] += 1
            r += 1
            

    return result


def back(idx, vowel_cnt, cnt, words, target, a, L):

    if vowel_cnt >= 1 and cnt >=2 and len(target) == L:
        print(''.join(target))

    for i in range(idx, a):

        if words[i] in vowels:
            back(i + 1, vowel_cnt +1, cnt, words, target + [words[i]], a, L)
        else:
            back(i + 1, vowel_cnt, cnt +1, words, target + [words[i]], a, L)

    return

L, C = map(int,input().split())
words= list(input().split())
words.sort()
vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
# 최소 한개의 모음과 2개의 자음
a = len(words)
for i in range(a):
    if words[i] in vowels:
        back(i + 1, 1, 0, words, [words[i]], a, L)
    else:
        back(i + 1, 0, 1, words, [words[i]], a, L)

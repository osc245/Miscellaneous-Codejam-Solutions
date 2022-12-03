for case in range(1, int(input()) + 1):
    word = input()
    ans = word[0]
    for c in word[1:]:
        if c >= ans[0]:
            ans = c + ans
        else:
            ans += c
    print('Case #{}: {}'.format(case, ans))

for case in range(1, int(input()) + 1):
    ans = ''
    depth = 0
    for n in input():
        num = int(n)
        if num < depth:
            ans += ')' * (depth - num)
        else:
            ans += '(' * (num - depth)
        ans += n
        depth = num
    ans += ')'*depth
    print('Case #{}: {}'.format(case, ans))

for case in range(1, int(input()) + 1):
    input()
    ans = input().replace('S', '-').replace('E', 'S').replace('-', 'E')
    print('Case #{}: {}'.format(case, ans))

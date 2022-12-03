for case in range(1, int(input()) + 1):
    dist, horses = [int(x) for x in input().split()]
    info = [[int(x) for x in input().split()] for _ in range(horses)]
    ans = dist/max([(dist - x[0]) / x[1] for x in info])
    print('Case #{}: {}'.format(case, ans))
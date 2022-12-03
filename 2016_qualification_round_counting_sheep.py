for case in range(1, int(input()) + 1):
    i = j = int(input())
    nums = set(list(str(i)))
    ans = 'INSOMNIA'
    if i:
        while len(nums) < 10:
            i += j
            nums.update(list(str(i)))
        ans = i
    print('Case #{}: {}'.format(case, ans))

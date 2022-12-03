for case in range(1, int(input()) + 1):
    row1 = int(input())
    nums = set([input().split() for _ in range(4)][row1 - 1])
    row2 = int(input())
    nums &= set([input().split() for _ in range(4)][row2 - 1])
    ans = 'Volunteer cheated!'
    if len(nums) == 1:
        ans = list(nums)[0]
    elif len(nums) > 1:
        ans = 'Bad magician!'
    print('Case #{}: {}'.format(case, ans))

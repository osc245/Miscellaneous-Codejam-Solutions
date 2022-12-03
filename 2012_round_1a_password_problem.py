for case in range(1, int(input()) + 1):
    done, total = [int(x) for x in input().split()]
    probabilities = [float(p) for p in input().split()]
    ans = total + 2
    correctProb = 1
    for i, prob in enumerate(probabilities):
        correctProb *= prob
        ans = min(ans, done + 2 * (total - i) - correctProb*(total + 1))
    print('Case #{}: {}'.format(case, ans))

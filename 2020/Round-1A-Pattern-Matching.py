# this solution only passes the first two test sets

for case in range(1, int(input()) + 1):
    words = [input().split("*") for _ in range(int(input()))]
    prefs, suffs = [w[0] for w in words], [w[1] for w in words]
    maxPref, maxSuff = max(prefs, key=len), max(suffs, key=len)
    ans = maxPref + maxSuff if all([maxPref[:len(p)] == p for p in prefs]) and all(maxSuff[::-1][:len(s)] == s[::-1] for s in suffs) else "*"
    print("Case #{}: {}".format(case, ans))

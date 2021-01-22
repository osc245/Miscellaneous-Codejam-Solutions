# Incomplete

for case in range(1, int(input()) + 1):
    print(input())
    people = [int(n) for n in input().split()[1]]
    count = ans = 0
    for i in range(len(people)):
        if count + ans < i:
            ans += 1
        count += people[i]
    print("Case #{}: {}".format(case, ans))

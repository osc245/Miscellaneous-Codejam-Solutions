# incomplete

for case in range(1, int(input()) + 1):
    input()
    partySize = input().split()
    people = [(chr(ord("A") + i), int(partySize[i])) for i in range(len(partySize))]
    people.sort(key=lambda x: -x[1])
    print(people)
    ans = ""
    print("Case #{}: {}".format(case, ans))

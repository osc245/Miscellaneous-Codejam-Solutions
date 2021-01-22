# incomplete

for case in range(1, int(input()) + 1):
    input()
    partySize = input().split()
    people = [(chr(ord("A") + i), int(partySize[i])) for i in range(len(partySize))]
    ans = ""
    # case for when len(people) == 1 or 2
    while # not all 0:
        # don't sort each time just swap around the third index with first and second
        people.sort(key=lambda x: -x[1])
        print(people)
    print("Case #{}: {}".format(case, ans))

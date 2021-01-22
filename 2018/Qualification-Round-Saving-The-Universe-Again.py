for case in range(1, int(input()) + 1):
    universe, moves = input().split()
    ans = "IMPOSSIBLE"
    if moves.count("S") <= int(universe):
        ans = 0
        while True:
            strength, damage = 1, 0
            for m in moves:
                if m == "C":
                    strength *= 2
                else:
                    damage += strength
            if damage <= int(universe):
                break
            moves = moves[::-1].replace("SC", "CS", 1)[::-1]  # replace last occurrence of CS
            ans += 1
    print("Case #{}: {}".format(case, ans))

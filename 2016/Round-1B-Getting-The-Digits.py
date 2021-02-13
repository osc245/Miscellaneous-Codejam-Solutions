info = [("Z", "ZERO", 0), ("W", "TWO", 2), ("U", "FOUR", 4), 
("X", "SIX", 6), ("O", "ONE", 1), ("R" , "THREE", 3), 
("F" , "FIVE", 5), ("V" , "SEVEN", 7), ("H", "EIGHT", 8), 
("N" , "NINE", 9)]

for case in range(1, int(input()) + 1):
    string = input()
    nums = []
    for x in info:
        while x[0] in string:
            for c in x[1]:
                string = string.replace(c, "", 1)
            nums.append(x[2])
    ans = "".join([str(x) for x in sorted(nums)])
    print("Case #{}: {}".format(case, ans))

translation = {"a": "y", "o": "e", "z": "q"}
inString = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
outString = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
for i in range(len(inString)):
    translation[inString[i]] = outString[i]
for case in range(1, int(input()) + 1):
    ans = ""
    for c in input():
        ans += translation[c]
    print("Case #{}: {}".format(case, ans))

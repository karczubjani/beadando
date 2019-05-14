import sys

s = sys.argv[1]
kis = []
nagy = []
par = []
paratlan = []
nulla = []
for i in range(0, len(s)):
    if s[i].isupper():
        nagy.append(s[i])
        continue
    if s[i].islower():
        kis.append(s[i])
        continue
    if s[i].isdigit() and s[i] != "0":
        if ord(s[i]) % 2 == 0:
            par.append(s[i])
        else:
            paratlan.append(s[i])
        continue
    nulla.append(s[i])
kis.sort()
nagy.sort()
par.sort()
paratlan.sort()
for i in range(0, len(kis)):
    print(kis[i], end="")
for i in range(0, len(nagy)):
    print(nagy[i], end="")
for i in range(0, len(par)):
    print(par[i], end="")
for i in range(0, len(paratlan)):
    print(paratlan[i], end="")
for i in range(0, len(nulla)):
    print(nulla[i], end="")





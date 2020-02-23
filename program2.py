from itertools import permutations
ls=list(map(str,input().split()))
a=list(permutations(ls))
max=0
for i in a:
    s=""
    for j in i:
        s=s+j
    if int(s)>max:
        max=int(s)
print(max)

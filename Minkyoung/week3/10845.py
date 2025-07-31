import sys
input = sys.stdin.readline

n = int(input())
result = list()
p = list()
for i in range(n):
    s = input()
    if s[:2]=='pu':
        result.append(s[5:-1])
    elif s[:2]=='po':
        if len(result) ==0:
            p.append(-1)
        else:
            r = result.pop(0)
            p.append(r)
    elif s[:2]=='si':
        p.append(len(result))
    elif s[:2]=='em':
        if len(result) == 0:
            p.append(1)
        else:
            p.append(0)
    elif s[:2]=='fr':
        if len(result)==0:
            p.append(-1)
        else:
            p.append(result[0])
    elif s[:2]=='ba':
        if len(result)==0:
            p.append(-1)
        else:
            p.append(result[-1])

for i in p:
    print(i)



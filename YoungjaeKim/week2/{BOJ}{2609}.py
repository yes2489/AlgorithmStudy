def _gcd(a, b): # 최대 공약수
    if b == 0:
        return a
    else:
        return _gcd(b, a%b)

def _lcm(a, b): # 최소 공배수
    return a * b // _gcd(a, b)


a, b = map(int, input().split())
print(_gcd(a,b))
print(_lcm(a,b))

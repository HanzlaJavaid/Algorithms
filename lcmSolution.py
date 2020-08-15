# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        x = a%b
        return gcd(b,x)

def lcm(a, b):
    g = gcd(a,b)
    return (a * b)//g

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))


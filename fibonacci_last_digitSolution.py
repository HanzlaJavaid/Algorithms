# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1 

    for _ in range(n - 1):
        temp = current % 10
        previous, current = current, previous + temp

    return current % 10

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))

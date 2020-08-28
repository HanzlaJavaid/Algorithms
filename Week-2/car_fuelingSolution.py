# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    covered = 0
    count = 0
    x = 0
    stops.append(distance)
    for i in range(x,len(stops)):
        if(stops[i]>covered + tank):
            t = i - 1
            if(stops[t] == covered):
                return -1
            covered = stops[t]
            count = count + 1
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

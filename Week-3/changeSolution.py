# Uses python3
import sys

def get_change(m):
    #write your code here
    s = 0
    l = []
    e = [10,5,1]
    i = 0
    while s!=m:
        s = e[i] + s
        if(s > m):
            s = s - e[i]
            i = i + 1
            continue
        l.append(e[i])
    return len(l)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

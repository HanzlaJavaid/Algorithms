# python3

"""Majority element detection using divide-and-conquer."""


def divide_func(seq, l, r):
    """Return the majority element in ``seq[l:r]`` or ``-1`` if none exists.

    The original implementation returned ``seq[l]`` when ``r - l == 2`` which
    incorrectly assumed that the first of the two elements was the majority.
    For a sequence such as ``[1, 2]`` this resulted in reporting a majority
    element even though none exists.  The function now correctly handles
    two-element slices by checking whether both elements are equal.
    """
    if l + 1 == r:
        # Only one element – it is trivially the majority
        return seq[l]
    elif l + 2 == r:
        # Two elements – return the value only if both are the same
        return seq[l] if seq[l] == seq[l + 1] else -1
    m = (l+r)//2
    left = divide_func(seq, l, m)
    right = divide_func(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else:
        return -1


if __name__ == "__main__":
    n = int(input())
    seq = [int(i) for i in input().split()]
    print(int(divide_func(seq, 0, n) != -1))


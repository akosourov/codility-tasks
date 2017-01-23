"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of 
integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should 
return 3, because there are three numbers divisible by 2 within 
the range [6..11], namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
"""

def solution(A, B, K):
    import math

    a1 = K * math.ceil(float(A) / K)
    an = K * math.floor(float(B) / K)   # an = a1 + (n-1)K
    if a1 <= an <= B:
        N = (an - a1)/K + 1
    else:
        N = 0
    return int(N)


if __name__ == '__main__':
    print(solution(6, 11, 2), 3)
    print(solution(1,1,11), 0)
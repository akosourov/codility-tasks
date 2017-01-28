"""
A non-empty zero-indexed array A consisting of N integers is given.
The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] 
(0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty zero-indexed array A, returns the value 
of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(1), beyond input storage 
(not counting the storage required for input arguments).
"""

def solution(A):
    A.sort()
    n = len(A)
    if A[0] >= 0 and A[n-1] >= 0 or A[0] < 0 and A[n-1] < 0:
        # all positive or all negative
        res = A[n-1] * A[n-2] * A[n-3]
    elif A[0] < 0 and A[1] < 0:
        first_two = A[0] * A[1]
        last_two = A[n-1] * A[n-2]
        res = max(first_two*A[n-1], last_two*A[n-3])
    else:
        res = A[n-1] * A[n-2] * A[n-3]
    return res


if __name__ == '__main__':
    assert solution([-3,1,2,-2,5,6]) == 60
    assert solution([1,1,1]) == 1
    assert solution([7,7,7,1,1,1]) == 343
    assert solution([-10, 0, 0, 1]) == 0
    assert solution([-1,-2,-3]) == -6
    assert solution([-10, -9, -8, 0, 1, 2]) == 180
    assert solution([-10, -9, -8, 0, 100, 200]) == 90 * 200
    assert solution([-10, 0, 1, 2, 3]) == 6
    assert solution([-10, -9, -2, -1]) == -18
    assert solution([-5, -3, 1, 2, 3, 4, 7]) == 105
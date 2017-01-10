"""
Write a function:

def solution(A)
that, given a non-empty zero-indexed array A of N integers, 
returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

def solution(A):
    count_positive = 0
    min_positive = None
    for el in A:
        if el > 0:
            count_positive += 1
            if min_positive is None or el < min_positive:
                min_positive = el

    if min_positive is None or min_positive > 1:
        return 1

    len_c = count_positive + 1
    count_arr = [0] * len_c
    for el in A:
        if el >= len_c:
            continue
        if el > 0:
            count_arr[el] += 1

    for i in range(2, len_c):
        if count_arr[i] == 0:
            return i
    
    return len_c

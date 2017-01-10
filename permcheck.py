def solution(A):
    n = len(A)
    count_arr = [0] * (n + 1)
    for el in A:
        if el > n:
            return 0
        count_arr[el] += 1
        if count_arr[el] > 1:
            return 0

    for i in range(1, len(count_arr)):
        if count_arr[i] == 0:
            return 0
    return 1
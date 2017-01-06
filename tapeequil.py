def solution(A):
    L = []  # sum from left to right exclusive
    sum_left = 0
    for el in A:
        L.append(sum_left)
        sum_left += el

    R = []  # sum from right to left inclusive (reverse order)
    sum_right = 0
    for el in reversed(A):
        sum_right += el
        R.append(sum_right)

    min_diff = None
    len_a = len(A)
    for i in range(1, len_a):
        l_sum = L[i]
        r_sum = R[-i-1]
        diff = abs(l_sum - r_sum)
        if i == 1:
            min_diff = diff
        else:
            if diff < min_diff:
                min_diff = diff

    return min_diff

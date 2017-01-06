def shift(A):
    for i in range(len(A)-1, 0, -1):
        A[i], A[i-1] = A[i-1], A[i]
    return A

def solution_slow(A, K):
    for k in range(K):
        shift(A)
    return A

def solution(A, K):
    for k in range(K):
        for i in range(len(A)-1-k, K-k, -K):
            A[i], A[i-K] = A[i-K], A[i]
    return A

if __name__ == '__main__':

    # test1
    A1 = [1,2,3,4,5,6,7]
    print(str(A1), shift(A1))

    A2 = [1,2,3,4,5,6,7]
    print(str(A2), solution_slow(A2, 2), [6,7,1,2,3,4,5])


    A3 = [1,2,3,4,5,6,7,8]
    print(str(A3), solution_slow(A3, 2), [7,8,1,2,3,4,5,6])

    A4 = [1,2,3,4,5,6,7,8]
    print(str(A4), solution(A4, 2), [7,8,1,2,3,4,5,6])

    #  ([3, 8, 9, 7, 6], 3) 
def insertion_sort(A):
    for each in range(0, len(A)):
        for i in range(0, len(A)):
            if A[each] < A[i]:
                A[each], A[i] = A[i], A[each]
    return A

A = [6, 2, 4, 6, 7, 8, 98, 12, 5]

print(insertion_sort(A))
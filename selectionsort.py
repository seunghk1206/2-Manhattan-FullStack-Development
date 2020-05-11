"""
1. first one = minimum
2. iteration 돌리면서 새로운 minimum을 
"""
def selection_sort(A):
    for i in range(0, len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                A[i], A[minIndex] = A[minIndex], A[i]
    return A

A = [6, 2, 4, 6, 7, 8, 98, 12, 5]

print(selection_sort(A))
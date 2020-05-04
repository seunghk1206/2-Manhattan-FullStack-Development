'''
Algorithm
1. for loop으로 리스트를 돌면서 왼쪽값이 더 크면 swap


'''

listA = [5, 3, 8, 6, 7, 2]
def bubblesort(listA):
    for i in range(0, len(listA) - 1):
        for j in range(0, len(listA) - 1 - i):
            if listA[j] > listA[j+1]:
                listA[j], listA[j+1] = listA[j+1], listA[j] #swap
    return listA
print(bubblesort(listA))

"""

"""

##

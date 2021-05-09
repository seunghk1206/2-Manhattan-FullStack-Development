def recursionSort(inpL, startInd, endInd):
    tempL = inpL
    if endInd != 0:
        if startInd != len(inpL)-1:
            if inpL[startInd] < inpL[startInd+1]:
                tempL[startInd], tempL[startInd+1] = tempL[startInd+1], tempL[startInd]
                return recursionSort(tempL, startInd, endInd)
            else:
                return recursionSort(tempL, startInd+1, endInd)
        else:
            return recursionSort(tempL, 0, endInd-1)
    else:
        return tempL


L = [1,6,2,6,8,4,7,4]
print(recursionSort(L, 0, len(L)-1))
import random


def findLongSubSeq(arr):
    theset = set(arr)
    ans = 0
    for i in arr:
        if i - 1 not in theset: #first in a sequence
            aux = i
            while(aux in theset):
                aux +=1

            ans = max(ans,aux-i)
    return ans

array  = [random.randrange(100) for x in range(100)]

print(findLongSubSeq(array))

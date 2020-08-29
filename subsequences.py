import random


def findLongSubSeq(arr):
    theset = set(arr)
    ans = 0
    for i in arr:
        if i - 1 not in theset:
            aux = i
            while(aux in s):
                aux +=1

            ans = max(ans,aux-i)
    return ans

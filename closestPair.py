import sys
def closestPair(arr):
    arr.sort()
    if len(arr)==2:
        return abs(arr[1]-arr[0])
    elif len(arr)==1:
        return sys.maxsize
    mid=(len(arr)//2)
    #print(mid)
    return min(closestPair(arr[:mid]),closestPair(arr[mid:]),abs(arr[mid]-arr[mid-1]))
    
print(closestPair([8,5,7,3,11,18]))

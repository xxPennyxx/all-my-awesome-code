def quicksort(A,a,b):
    if a>=b:
        return
    left=a
    right=b
    mid=(left+right)//2
    pivot=A[mid]
    while left<=right:
        while left<=right and A[left]<pivot:
            left+=1
        while left<=right and A[right]>pivot:
            right-=1
        if left<=right:
            A[left],A[right]=A[right],A[left] #swap the 2 elements at their respective pointers, when left is less that or equal to the right.
            left+=1
            right-=1
    #put pivot in right place indicated by left
    if a<right:
        quicksort(A,a,right) #if the start is less than the right pointer then perform quicksort on left half
    if left<b:
        quicksort(A,left,b) #similarly, if the left is less than the end index then perform quicksort on right half
    return A



A=[int(x) for x in input().split()]
print(quicksort(A,0,len(A)-1))

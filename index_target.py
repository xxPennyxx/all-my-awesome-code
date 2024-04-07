def findtarget(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return (lookup[target - num], i)
        lookup[num] = i


n = []
a = int(input("Enter a number of elements:"))
for i in range(0, a):
    p = int(input("Enter a number:"))
    n.append(p)
t = int(input("Enter target:"))

print(findtarget(n, t))

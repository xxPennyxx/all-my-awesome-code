class Heap:
    def __init__(self,arr,l):
        self.elements = arr
        self.sz = l
 
    def insert(self, k):
        
        self.elements.append(k)
        self.sz += 1
        self.upheap(self.sz-1)
        
    def upheap(self, i):
        while (i // 2 )> 0:
            if self.elements[i] < self.elements[i // 2]:
                self.elements[i], self.elements[i // 2] = self.elements[i // 2], self.elements[i]
            i = i // 2
        
 
    def downheap(self, i):
        while (i * 2) < self.sz:
            min = self.findMin(i)
            if self.elements[i] > self.elements[min]:
                self.elements[i], self.elements[min] = self.elements[min], self.elements[i]
            i = min
 
    def findMin(self, i):
        if (i * 2)+1 > self.sz-1:
            return i * 2
        else:
            if self.elements[i*2] < self.elements[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def deleteMin(self):
        if len(self.elements) == 1:
            return
        root = self.elements[0]
        self.elements[0] = self.elements[self.sz-1]
        *self.elements, _ = self.elements
        self.sz -= 1
        self.downheap(0)
        return 
        
    def printHeap(self):
        print(self.elements)
def main():
    arraySize = int(input())
    arr = list(map(int, input().split()))
    heap = Heap(arr,arraySize)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              heap.insert(int(operation[1]))
              heap.printHeap()
         elif (operation[0] == "R"):
              heap.deleteMin()
              heap.printHeap()
         inputs -= 1

if __name__ == '__main__':
    main()

'''
5  
2 6 9 20 50
5
I 8
I 40
I 3
R
R
'''
 

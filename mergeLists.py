class LinkedList:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    def __init__(self):
        self.head=None
        #no tail???
    
    def addElement(self,n):
        newElement=self.Node(n)
        if(self.head is None):
            self.head=newElement
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newElement
    
def mergeUnion(l1,l2):
    ans=[]
    curr1=l1.head
    curr2=l2.head
    while (curr1 or curr2) and (curr1.next or curr2.next):
        if curr1.data==curr2.data:
            ans.append(curr1.data)
            curr1=curr1.next
            curr2=curr2.next
        elif curr1.data<curr2.data:
            ans.append(curr1.data)
            curr1=curr1.next
        else:
            ans.append(curr2.data)
            curr2=curr2.next
        if curr1.next is None and curr2.next is None:
            if curr1.data<curr2.data:
                ans.append(curr1.data)
                ans.append(curr2.data)
            elif curr1.data>curr2.data:
                ans.append(curr2.data)
                ans.append(curr1.data)
            else:
                ans.append(curr1.data)
        
    return ans

def mergeIntersection(l1,l2):
    ans=[]
    curr1=l1.head
    curr2=l2.head
    while curr1 and curr2:
        if curr1.data==curr2.data:
            ans.append(curr1.data)
            curr1=curr1.next
            curr2=curr2.next
        elif curr1.data<curr2.data:
            curr1=curr1.next
        else:
            curr2=curr2.next
    return ans
    
list1=LinkedList()
list2=LinkedList()
'''
A 1: append 1 to linked list 1
B 5: append 5 to linked list 2
'''
ops=int(input())
for i in range(ops):
    command=input()
    params=command.split()
    if params[0]=='A':
        list1.addElement(params[1])
    elif params[0]=='B':
        list2.addElement(params[1])
    else:
        pass

print(mergeUnion(list1,list2))
print(mergeIntersection(list1,list2))

'''
15
A 1
A 2
A 3
A 5
A 8
A 13
A 21
A 34
B 1
B 2
B 4
B 8
B 16
B 32
B 64

'''

            

class SLList:

    class node:
        def __init__(self,data):
            self.element = data
            self.next = None
        
    def __init__(self):
        self.head = self.node(None)# node is a part of SLList
        self.sz = 0
          
          
    def insertLast(self,data):
        if self.isEmpty():
            self.head.element = data
            self.sz += 1
            return #if empty, make the head element store the data and increment size
        
        curr = self.head
        while curr.next:
            curr = curr.next #iterate till last element

        newNode = self.node(data)
        curr.next = newNode #now make the last element point to new element, now the new tail
        self.sz += 1
        return
    
    def insertAfter(self,u,v):
        curr = self.head
        while curr:
            if curr.element == v: #if the current element is v
                
                if not curr.next:
                    self.insertLast(u) #if it happens to be the last element, insert at last
                    return
                
                newNode = self.node(u) #new element is u
                newNode.next = curr.next #the next element is curr's next
                curr.next = newNode #make curr's next the element at newNode
                self.sz += 1
                return
            curr = curr.next #don't forget this one!
            
        print("Node to insert after not found") #if not found
        return    
    def deleteAfter(self,u):
        toBeDel=self.head
        uNode = self.findNode(u) #find u
        if uNode:
            if uNode.next: #for the normal algorithm you'll require at least 2 elements after unode. If there's just one, follow the deleteLast() method to delete the one after unode
                if not toBeDel.next: #if that is the last element
                    self.deleteLast()
                    return
                toBeDel = uNode.next
                uNode.next = toBeDel.next #make the next element of unode the element AFTER toBeDel
                del toBeDel
                self.sz-=1
                return
            else:
                pass 
        print("Node to delete after not found") #if that node doesn't exist
        return          


    def insertFirst(self,data):
        if not self.head.element:
            self.head.element = data
            self.sz += 1
            return
        
        newNode = self.node(data)
        newNode.next = self.head #make the newnode point to the head
        self.head = newNode
        self.sz += 1
        return
     
    def deleteFirst(self):
        if self.isEmpty():
            self.head = self.node(None)
            print("ListEmptyException")
            return
        
        toBeDel = self.head
        self.head = toBeDel.next #the one following head is the new head
        del toBeDel
        self.sz -= 1
        return

    def deleteLast(self):
        if self.isEmpty():
            self.head = self.node(None) #Don't forget!!
            print("ListEmptyException")
            return
        
        if self.size() == 1:
            return self.deleteFirst() #deleteFirst if containing only one element 
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next #now prev will have the penultimate element and curr will be at tail
        prev.next = None #just do that xD
        del curr
        self.sz -= 1
        return

    def reverse(self):
        prev=None
        curr=self.head
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def deleteDuplicates(self):
        curr=self.head
        arr=[]
        while curr:
            if curr.element not in arr:
                arr.append(curr.element)
            curr=curr.next
        self.__init__()
        #print(arr)
        for i in arr:
            self.insertLast(i)


    def printList(self):
        if (self.isEmpty()):
            print ("List Empty")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print("None")
            
        return
     
    def findNode(self, val):
        curr = self.head
        #pos=0
        while curr:
            if curr.element == val:
                #print(pos)
                return curr
            curr = curr.next
            #pos+=1
        return None
    def findByPosition(self, i):
        curr = self.head
        pos=0
        while curr:
            if pos == i:
                print(curr.element)
                return curr.element
            curr = curr.next
            pos+=1
        return None
        
    def getHead(self):
        return self.head.element
            
    def isEmpty(self):
        return self.sz == 0
        
    def size(self):
        return self.sz
        		  
    def getLastNode(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.element
        		  
    def delKth(self, k):
        curr = self.head
        prev = self.head
        i = 1
        while curr.next:
            if i == k:
                prev.next = curr.next
                del curr
                self.sz -= 1
                return
            prev = curr
            curr = curr.next
            i += 1
        return

    def swapAdj(self):
        curr = self.head
        while curr.next != None:
            curr.element, curr.next.element = curr.next.element, curr.element
            curr = curr.next
            
            if not curr.next:
                return
            curr = curr.next
        return
             
def testSLL():
    sll = SLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(sll.size())
        elif(operation[0]=="I"):
            print(sll.isEmpty())
        elif(operation[0]=="IF"):
            sll.insertFirst((operation[1]))
            sll.printList()
        elif(operation[0]=="R"):
            sll.reverse()
            sll.printList()
        elif(operation[0]=="IL"):
            sll.insertLast((operation[1]))
            sll.printList()
        elif(operation[0]=="DD"):
            sll.deleteDuplicates()
            sll.printList()
        elif(operation[0]=="DF"):
            sll.deleteFirst()
            sll.printList()
        elif(operation[0]=="DL"):
            sll.deleteLast()
            sll.printList()
        elif(operation[0]=="F"):
            print(sll.getHead())
        elif(operation[0]=='L'):
            print(sll.getLastNode())
        elif(operation[0]=='FIND'):
            print(sll.findNode((operation[1])))
        elif(operation[0]=='FB'):
            print(sll.findByPosition(int(operation[1])))
        elif(operation[0]=='DK'):
            sll.delKth(int(operation[1]))
            sll.printList()
        elif(operation[0]=='SA'):
            sll.swapAdj()
            sll.printList()
        inputs-=1


def main():
    testSLL()

if __name__ == '__main__':
    main()

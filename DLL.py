class DLList:
    class node:
        def __init__(self,data):
            self.element = data
            self.next = None
            self.prev = None
           
          
    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0

    def getHead(self):
        return self.head        
    
    def getLastNode(self):
        return self.tail        
    
    
    def insertAt(self,position,data): #insert data at position
        newNode = self.node(data)
        if(position < 1):
            return
        elif (position == 1):
            self.insertFirst(data)
        else: 
            curnode=self.head
            pos=1
            while pos<position:
              curnode=curnode.next
              pos+=1
            self.insertAfter(data,curnode.prev.element)
            return
    
    
     
    def insertLast(self,u):
        if self.isEmpty():
            self.head.element = u
            self.sz += 1
            return
        
        newNode = self.node(u)
        self.tail.next = newNode
        newNode.next = None
        newNode.prev = self.tail
        self.tail = newNode
        self.sz += 1	        

    def insertFirst(self,u):
        if self.isEmpty():
            self.head.element = u
            self.sz += 1
            return
        
        newNode = self.node(u)
        newNode.prev = None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.sz += 1       
   
    def insertAfter(self,u,v):
        curr = self.head
        while curr:
            if curr.element == v:
                
                if not curr.next: #boundary condition
                    self.insertLast(u)
                    return
                
                newNode = self.node(u)
                newNode.next = curr.next
                curr.next.prev = newNode
                curr.next = newNode
                newNode.prev = curr
                self.sz += 1
                return
            curr = curr.next
            
        print("Node to insert after not found")
        return      


    def insertBefore(self,u,v):
        curr = self.tail
        while curr:
            if curr.element == v:
                
                if not curr.prev: #boundary condition
                    self.insertFirst(u)
                    return
                
                newNode = self.node(u)
                newNode.next = curr
                newNode.prev = curr.prev
                curr.prev.next = newNode
                curr.prev = newNode
                self.sz += 1
                return
            curr = curr.prev
            
        print("Node to insert before not found")
        return        

    def deleteFirst(self):
        if(self.isEmpty()):
            print("List Empty")
            return
        if self.size() == 1:
            self.head.element = None
            self.sz-=1
            #self.__init__()
            return
        
        toBeDel = self.head
        toBeDel.next.prev = None
        self.head = toBeDel.next
        toBeDel.next = None
        del toBeDel
        self.sz-=1	        

    def deleteLast(self):
        if(self.isEmpty()):
            print("List Empty")
            return
        if self.size() == 1:
            self.tail.element = None
            self.sz-=1
            return
        
        toBeDel = self.tail
        toBeDel.prev.next = None
        self.tail = toBeDel.prev
        toBeDel.prev = None
        del toBeDel
        self.sz-=1          

   
    def deleteAfter(self,u):
        uNode = self.findNode(u)
        if uNode:
            if uNode.next:
                toBeDel = uNode.next
                uNode.next = toBeDel.next
                if toBeDel.next:
                    toBeDel.next.prev = uNode
                else:
                    self.deleteLast() #if the element to be deleted is that last
                    return
                del toBeDel
                self.sz-=1
                return
            else:
                return #if that element is the last and you can't delete AFTER that :D
        print("Node to delete after not found")
        return        

  
    def deleteBefore(self,u):
        uNode = self.findNode(u)
        if uNode:
            if uNode.prev:
                toBeDel = uNode.prev
                uNode.prev = toBeDel.prev
                if toBeDel.prev:
                    toBeDel.prev.next = uNode
                else:
                    self.deleteFirst()
                    return
                del toBeDel
                self.sz-=1
                return
            else:
                return
       
        print("Node to delete before not found")
        return   
    
    def delByValue(self, data):  
        if self.sz==0:
            return        
        curnode=self.head
        while curnode.next:
            if curnode.element==data:
                if curnode.prev:
                    self.deleteAfter(curnode.prev.element)
                else:
                    self.deleteFirst()
            curnode=curnode.next
        return


        
    def delByPosition(self, position):

        if position <= 0:
            self.deleteFirst()

        elif position >= self.sz-1:
            self.deleteLast()
        else:
            curnode=self.head
            pos=1
            while pos<position:
              curnode=curnode.next
              pos+=1
            self.deleteAfter(curnode.prev.element)
            return
            
    

    def findNode(self, val):
        curr = self.head
        if curr.element == val:
            return curr
        while curr:
            if curr.element == val:
                return curr
            curr = curr.next
        return None        

    def swap(self,u,v):
        uNode = self.findNode(u)
        vNode = self.findNode(v)
        if uNode and vNode:
            uNode.element = v
            vNode.element = u        
 
    def isEmpty(self):
        return (self.sz==0)

    def size(self):
        return self.sz

    def printList(self):
        if (self.isEmpty()):
            print ("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.prev
            print(" ")
        return
    
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
    
def testDLL():
    dll = DLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(dll.size())
        elif(operation[0]=="I"):
            print(dll.isEmpty())
        elif(operation[0]=="IF"):
            dll.insertFirst((operation[1]))
            dll.printList()
        elif(operation[0]=="IL"):
            dll.insertLast((operation[1]))
            dll.printList()
        elif(operation[0]=="DF"):
            dll.deleteFirst()
            dll.printList()
        elif(operation[0]=="DL"):
            dll.deleteLast()
            dll.printList()
        elif(operation[0]=="IA"):
            dll.insertAfter((operation[1]),(operation[2]))
            dll.printList()
        elif(operation[0]=="IB"):
            dll.insertBefore((operation[1]),(operation[2]))
            dll.printList()
        elif(operation[0]=="IP"):
            dll.insertAt(int(operation[1]),(operation[2]))
            dll.printList()
        elif(operation[0]=="DP"):
            dll.delByPosition(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DV"):
            dll.delByValue((operation[1]))
            dll.printList()
        elif(operation[0]=="DA"):
            dll.deleteAfter((operation[1]))
            dll.printList()
        elif(operation[0]=="DB"):
            dll.deleteBefore((operation[1]))
            dll.printList()
        elif(operation[0]=="DD"):
            dll.deleteDuplicates()
            dll.printList()
        elif(operation[0]=="F"):
            print(dll.getHead().element)
        elif(operation[0]=='L'):
            print(dll.getLastNode().element)
        elif(operation[0]=='FIND'):
            temp = dll.findNode(int(operation[1]))
            if (temp!=None):
                print(temp.element)
            else:
                print("NULL")
        elif(operation[0]=='SW'):
            dll.swap((operation[1]),(operation[2]))
            dll.printList()
        inputs-=1


def main():
    testDLL()

if __name__ == '__main__':
    main()

class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
            

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0
        

    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children
    
    def printchildren(self,curnode):
        ch=self.getChildren(curnode)
        if ch==[]:
            print(None)
        for i in ch:
            print(i.element,end=",")
    

    def isExternal(self, curnode):
        if (curnode.leftchild==None and curnode.rightchild==None):
            return (True)
        else:
            return (False)

    def isRoot(self,curnode):
        if (curnode.parent==None):
            return True
        else:
            return False

    def isBalanced(self,v):
        if not v.rightchild or v.leftchild:
            return True
        elif self.isBalanced(v.leftchild) and self.isBalanced(v.rightchild) and abs(self.findHeight(v.leftchild)-self.findHeight(v.rightchild))<=1:
            return True
        else:
            return False
            
    def isComplete(self,root):
        queue = [root]
        while len(queue):
            node = queue.pop(0)
            if not node: #run out of nodes in the tree
                break
            queue.append(node.leftchild)
            queue.append(node.rightchild)
            
        #popping one by one then appending left child first followed by rightchild. 
        #So then if it's complete all the nodes would be popped out of the queue and we will have None's in them (non-existent children xD).
        #If there's a gap in between then at means we have a non-None in between the None's that means the tree isn't complete
        for i in queue:
            if i is not None:
                return False

        return True
        
    '''
    def isComplete1(self,v,index,nodes):
        if(v==None):
            return True
        if(index>=nodes):
            return False
        return self.isComplete(v.leftchild,2*index+1,nodes) and self.isComplete(v.rightchild,2*index+1+1,nodes)
    def isComplete1helper(self):
        return self.isComplete1(self.root,0,0)
    '''
        
        
        
    def isPerfect(self,v,level=0):
        if not v: 
            return True
        elif not v.leftchild and not v.rightchild:
            return self.findDepth(v)==level+1
        elif not v.leftchild or not v.rightchild:
            return False
        return self.isPerfect(v.leftchild, level+1) and self.isPerfect(v.rightchild, level+1)
    '''def isPerfect1(self):
    return self.isPerfect(self.root,0)'''
        

    def inorderTraverse(self, v):
        if not v:
            return

        if v.leftchild:
            self.inorderTraverse(v.leftchild)
        print(v.element, end=',')
        if v.rightchild:
            self.inorderTraverse(v.rightchild)
			        

    def preorderTraverse(self, v):
        if not v:
            return
        print(v.element, end=',')
        if v.leftchild:
            self.preorderTraverse(v.leftchild)
        
        if v.rightchild:
            self.preorderTraverse(v.rightchild)	
       

    def postorderTraverse(self, v):

        if not v:
            return
        
        if v.leftchild:
            self.postorderTraverse(v.leftchild)
        
        if v.rightchild:
            self.postorderTraverse(v.rightchild)	
        print(v.element, end=',')	
			
        

    def levelorderTraverse(self, v):

        queue = []
        queue.append(v)
        while queue:
            curr = queue.pop(0)
            print(curr.element, end=',')
            if curr.leftchild:
                queue.append(curr.leftchild)
            if curr.rightchild:
                queue.append(curr.rightchild)	
			
       

    def findDepth(self, v):

        if v==None:
            return -1
        elif(v.parent==None):
            return 0
        else:
            return 1+self.findDepth(v.parent)	
			
    	

    def findHeight(self, v):

        if v==None:
            return -1
        else:
            return 1+max(self.findHeight(v.rightchild),self.findHeight(v.leftchild))	

    # delete leaves in the tree
    def delLeaves(self, v):

        if v == None:
            return None
        if v.leftchild==None and v.rightchild==None:
            if v.parent.leftchild==v:           
                v.parent.leftchild=None
            else:
                v.parent.rightchild=None
            del v
            return      
        self.delLeaves(v.leftchild)
        self.delLeaves(v.rightchild)	
			
        
    # returns true if tree is proper
    def isProper(self, v):

        if v==None:
            return True
        if len(self.getChildren(v))==1:
            return False
        return self.isProper(v.leftchild) and self.isProper(v.rightchild)	
        
    def depthSumHelper(self,v):
        nodes=1
        sum=0
        if v.leftchild!=None:
            nodes1,sum1=self.depthSumHelper(v.leftchild)
            sum+=nodes1+sum1
            nodes+=nodes1
        if v.rightchild!=None:
            nodes1,sum1=self.depthSumHelper(v.rightchild)
            sum+=nodes1+sum1
            nodes+=nodes1
        return (nodes,sum)
        
    def depthSum(self,root):
        n,s=self.depthSumHelper(root)
        return s
			
        
    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        if (v == None):
            return
        else:
            self.mirror(v.leftchild)
            self.mirror(v.rightchild)
            temp=v.leftchild
            v.leftchild=v.rightchild
            v.rightchild=temp	
   
        
			
    def rightView(self,root):
        curr=root
        while curr.rightchild:
            print(curr.element,end=" ")
            curr=curr.rightchild
        print(curr.element,end=" ")

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz=len(nodelist)
        return nodelist


    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element,end=" ")
            else:
                print(None)


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

    #determine whether there exists a root-to-leaf path whose nodes sum is equal to a specified integer
    def root2leafsum(self, k):

        print(self.root2leafhelper(self.root, k),end="")

    def root2leafhelper(self, v, sum):

        if not v:
            if sum == 0:
                return True
            else:
                return False

        return self.root2leafhelper(v.leftchild, sum-v.element) or self.root2leafhelper(v.rightchild, sum-v.element)	
			
        

    #determine the value of the leaf node in a given binary tree that is the terminal node of a path of least value from the root of the binary tree to any leaf. The value of a path is the sum of values of nodes along that path.
    def leastleaf(self):

        minsum,minleaf=self.dfs(self.root,sum=0)
        print(minleaf.element,end="")

        
    def dfs(self,v, sum):
        
        sum += v.element
        if (v.leftchild == None and v.rightchild == None):
            return sum, v
 
        leftsum, leftleaf = self.dfs(v.leftchild, sum)
        rightsum, rightleaf = self.dfs(v.rightchild, sum)
		
        if leftsum < rightsum:
            return leftsum, leftleaf
        else:
            return rightsum, rightleaf	
			        

def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              tree.inorderTraverse(tree.root)
              print()
         elif (operation[0] == "P"):
              tree.preorderTraverse(tree.root)
              print()
         elif (operation[0] == "GC"):
              pos = int(operation[1])
              tree.printchildren(nlist[pos])
              print()
         elif (operation[0] == "Post"):
              tree.postorderTraverse(tree.root)
              print()
         elif (operation[0] == "L"):
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == "D"):
              pos = int(operation[1])
              print(tree.findDepth(nlist[pos]))
         elif (operation[0] == "H"):
              pos = int(operation[1])
              print(tree.findHeight(nlist[pos]))
         elif (operation[0] == "IP"):
              print(tree.isProper(tree.root))
         elif (operation[0] == "IC"):
              print(tree.isComplete(tree.root))
         elif (operation[0] == "IB"):
              print(tree.isBalanced(tree.root))
         elif (operation[0] == "IPF"):
              print(tree.isPerfect(tree.root))
        
         elif (operation[0] == 'M'):
              tree.mirror(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'DL'):
              tree.delLeaves(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'RV'):
              tree.rightView(tree.root)
              print()
         elif (operation[0] == 'DS'):
              print(tree.depthSum(tree.root))
         elif (operation[0] == 'RL'):
              tree.root2leafsum(int(operation[1]))
              print()
         elif (operation[0] == 'ML'):
              tree.leastleaf()
              print()
         inputs -= 1

if __name__ == '__main__':
    main()

'''
8
-1 1 2 3 4 5 6 7
12
P
I
Post
L
D 1
H 1
D 5
IP
RL 5
ML 
M
DL
'''

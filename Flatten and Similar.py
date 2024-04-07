class BinaryTreeClass(object):
    
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
        
    def insert_left_child(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTreeClass(new_node)
        else:
            t = BinaryTreeClass(new_node)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right_child(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTreeClass(new_node)
        else:
            t = BinaryTreeClass(new_node)
            t.right_child = self.right_child
            self.right_child = t
            
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, obj):
        self.key = obj
        
    def get_root_val(self):
        return self.key
    
    def preorder(self,tree):
        if tree is None:
                return
        print(tree.key,end=' ')
        self.preorder(tree.left_child)
        self.preorder(tree.right_child)
            
    def inorder(self,tree):
        if tree is None:
            return
        
        self.inorder(tree.left_child)
        print(tree.key,end=' ')
        self.inorder(tree.right_child)
                    
    def postorder(self,tree):

        if tree is None:
            return
        self.postorder(tree.left_child)
        self.postorder(tree.right_child)
        print(tree.key,end=' ')
        
            
    def isCompleteBTree(self):
        queue = [ self ]
        while len(queue):
            node = queue.pop(0)
            if not node:
                break
            queue.append(node.left_child)
            queue.append(node.right_child)

        for i in queue:
            if i is not None:
                return False

        return True
        
    
    def isFullBTree(self):
        if self is None:
            return True
        elif not self.left_child and not self.right_child:
            return True
        elif not self.left_child:
            return False
        elif not self.right_child:
            return False
        else:
            return self.left_child.isFullBTree() and self.right_child.isFullBTree()

    
    def FlattenBTree(self):
        queue = [ self ]
        head = None
        tail = None

        while len(queue):
            node = queue.pop(0)

            if not node:
                continue

            if not head:
                head = BinaryTreeClass(node.key)
                tail = head
            else:
                tail.right_child = BinaryTreeClass(node.key)
                tail = tail.right_child

            queue.append(node.left_child)
            queue.append(node.right_child)

        while(head):
            print(head.key, end=" ")
            head = head.right_child
        print()

   
def similarTrees(tree1, tree2):

    queue = [ [ tree1, tree2 ] ]

    while len(queue):
        node1, node2 = queue.pop(0)

        if not node1 and not node2:
            continue
        elif not node1:
            return False
        elif not node2:
            return False

        numLeft1 = (node1.left_child != None)
        numLeft2 = (node2.left_child != None)
        numRight1 = (node1.right_child != None)
        numRigh2 = (node2.right_child != None)

        if numLeft1 != numLeft2:
            return False
        elif numRight1 != numRigh2:
            return False

        queue.append([ node1.left_child, node2.left_child ])
        queue.append([ node1.right_child, node2.right_child ])

    return True  
    
    

def testbtapp():
    testcases=int(input())
    inputs=int(input())

    trees = []
    while inputs>0:
        command=input()
        operation=command.split()
        
        if(operation[0]=="L"):
            curr = trees[-1]
            for op in operation[:-2]:
                if op == "L":
                    curr = curr.left_child
                elif op == "R":
                    curr = curr.right_child
            
            if operation[-2] == "L":
                curr.insert_left_child(int(operation[-1]))
            else:
                curr.insert_right_child(int(operation[-1]))
                        
        if(operation[0]=="R"):
            curr = trees[-1]
            for op in operation[:-2]:
                if op == "L":
                    curr = curr.left_child
                elif op == "R":
                    curr = curr.right_child
            
            if operation[-2] == "L":
                curr.insert_left_child(int(operation[-1]))
            else:
                curr.insert_right_child(int(operation[-1]))
        if(operation[0]=="B"):
            trees.append(BinaryTreeClass(int(operation[-1])))
            
        if(operation[0]=="P"):
                trees[-1].preorder(trees[-1])
                print()
        if(operation[0]=="I"):
                trees[-1].inorder(trees[-1])
                print()
        if(operation[0]=="O"):
                trees[-1].postorder(trees[-1])
                print()
        if(operation[0]=="S"):
            print(similarTrees(trees[-2],trees[-1]))
        if(operation[0]=="F"):
                print(trees[-1].isFullBTree())  
        if(operation[0]=="C"):
                print(trees[-1].isCompleteBTree()) 
        if(operation[0]=="N"):
            trees[-1].FlattenBTree()
        inputs-=1
        
def main():
    
    testbtapp()

if __name__ == '__main__':
    main()

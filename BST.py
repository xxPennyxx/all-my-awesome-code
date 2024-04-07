class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def buildTree(self, nodes):
        if not len(nodes):
            return
        
        nodes = nodes[1:]
        self.size = 1
        self.root = Node(nodes.pop(0))
        queue = [self.root]
        while len(nodes):
            currNode = queue.pop(0)
            leftElement = nodes.pop(0)
            if leftElement != -1:
                currNode.left = Node(leftElement)
                queue.append(currNode.left)
                self.size += 1
            
            if not len(nodes):
                break
            
            rightElement = nodes.pop(0)
            if rightElement != -1:
                currNode.right = Node(rightElement)
                queue.append(currNode.right)
                self.size += 1

    def treeSize(self):
        return self.size

    def doFindNode(self, node, target, depth = 0):
        if not node:
            return None, None

        if node.element == target:
            return node, depth
        elif node.element < target:
            return self.doFindNode(node.right, target, depth+1)
        else:
            return self.doFindNode(node.left, target, depth+1)
    
    def findNode(self, target):
        node, depth = self.doFindNode(self.root, target)
        if node:
            print("Element Found", depth)
        else:
            print("Search Unsuccessful")

    def isExternal(self, value):
        node, _ = self.doFindNode(self.root, value)
        return not node.left and not node.right

    def isInternal(self, value):
        return not self.isExternal(value)

    def isRoot(self,value):
        if not self.root:
            return False
        return self.root.element == value

    def getHeight(self):
        queue = [[self.root, 0]]
        height = 0
        while len(queue):
            currNode, currDepth = queue.pop(0)
            height = max(height, currDepth)
            
            if currNode.left:
                queue.append([currNode.left, currDepth + 1])
            if currNode.right:
                queue.append([currNode.right, currDepth + 1])

        return height

    def getChildren(self, value):
        if self.isExternal(value):
            print(False)
        node, _ = self.doFindNode(self.root, value)
        if node.left:
            print(node.left.element, end = " ")
        if node.right:
            print(node.right.element, end = " ")

    def inOrder(self, node):
        if not node:
            return

        self.inOrder(node.left)
        print(node.element, end=" ")
        self.inOrder(node.right)

    def preOrder(self, node):
        if not node:
            return

        print(node.element, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):
        if not node:
            return

        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.element, end=" ")

    def revInOrder(self, node):
        if not node:
            return

        self.revInOrder(node.right)
        print(node.element, end=" ")
        self.revInOrder(node.left)

    def levelOrder(self):
        queue = [self.root]
        while len(queue):
            currNode = queue.pop(0)
            print(currNode.element, end = " ")
            
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
    
    def eulerTour(self, node):
        if not node:
            return

        if not node.left and not node.right:
            print(node.element, end= " ")
            return

        print(node.element, end=" ")
        self.eulerTour(node.left)
        print(node.element, end=" ")
        self.eulerTour(node.right)
        print(node.element, end=" ")

    def printLeaves(self):
        stack = [self.root]
        while len(stack):
            currNode = stack.pop()
            if self.isExternal(currNode.element):
                print(currNode.element, end = " ")
            
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)

    def sortOrder(self):
        self.inOrder(self.root)
 
def main():

    n = int(input())
    nodes = [int(x) for x in input().split()]

    tree = BST()
    tree.buildTree(nodes)

    ops = int(input())
    while ops:
        ops -= 1

        op = input().strip().split()
        if op[0] == "FE":
            tree.findNode(int(op[1]))
        elif op[0] == "IE":
            print(tree.isExternal(int(op[1])))
        elif op[0] == "II":
            print(tree.isInternal(int(op[1])))
        elif op[0] == "IR":
            print(tree.isRoot(int(op[1])))
        elif op[0] == "GH":
            print(tree.getHeight())
        elif op[0] == "GC":
            tree.getChildren(int(op[1]))
            print()
        elif op[0] == "P":
            tree.preOrder(tree.root)
            print()
        elif op[0] == "S":
            print(tree.treeSize())
        elif op[0] == "PRI":
            tree.revInOrder(tree.root)
            print()
        elif op[0] == "PLO":
            tree.levelOrder()
            print()
        elif op[0] == "PET":
            tree.eulerTour(tree.root)
            print()
        elif op[0] == "PL":
            tree.printLeaves()
            print()
        elif op[0] == "POST":
            tree.postOrder(tree.root)
            print()
        elif op[0] == "SORT":
            tree.sortOrder()
            print()
main()

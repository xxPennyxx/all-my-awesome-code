from collections import OrderedDict
import sys
class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def upHeap(self,i):

        while i//2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.upHeap(self.currentSize)
    
    def size(self):
        return self.currentSize

    def downHeap(self,i):
        while (i * 2) <= self.currentSize:
            min = self.minChild(i)
            if self.heapList[i] > self.heapList[min]:
                self.heapList[i], self.heapList[min] = self.heapList[min], self.heapList[i]
            i = min
		

    def minChild(self,i):
        if (i * 2)+1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
		
    def delMin(self):
        if len(self.heapList) == 1:
            return 'Empty heap'
        root = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop(self.currentSize)
        self.currentSize -= 1
        self.downHeap(1)
        return root
    	
    def printHeap(self):
        print(self.heapList)



class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.front=[]
        self.back=[]
        self.depfs=[]
        self.edges=[]
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.vertList = OrderedDict(sorted(self.vertList.items()))
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):  #f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.edges.append([f,t,cost])
        

    def getVertices(self):
        return self.vertList.keys()

    
    def __iter__(self):
    	return iter(self.vertList.values())
    
    def createAdjMatrix(self):
        adjmat = list()
        n=self.numVertices
        adjmat=[[0]*n for i in range(n)]
        for i in self:
            for j in i.getConnections():
                adjmat[i.getId()][j.getId()]=i.getWeight(j)

        print("Adjacency matrix")
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print(adjmat[i][j], end=" ")
            print("")
        return
    
    def printdfs(self):
                print("Front edges:",self.front)
                print("Back edges:",self.back)
                print("dfs:",self.depfs)

    def dfs(self,stnode):
        self.depfs.append(stnode.getId() )
        neighbours=list(stnode.getConnections())
        

        def dfs2(s,visited,result,front,back):
            
            visited[s.getId()]= True
            neighbours=list(s.getConnections())
            result.append(s.getId())

            for i in neighbours:
                if visited[i.getId()] == False:
                    front.append([s.getId(),i.getId()])
                    dfs2(i, visited,result,front,back)
                else:
                    back.append([s.getId(),i.getId()])
                
            return result,front,back
       
        r,f,b=dfs2(stnode,[False]*self.numVertices,[],[],[])
        self.depfs=r
        self.front=f
        self.back=b
        return
        

    def bfs(self,stnode):
        queue=[]
        breadth=[]
        cross=[]
        breadth.append(stnode.getId())
        queue.append(stnode.getId())
        visited=[False]*self.numVertices
        visited[stnode.getId()]=True
        
        while queue:
          s = queue.pop(0)
          v=self.getVertex(s)

          for i in v.getConnections():
            temp=i.getId()
            if visited[temp] == False:
              queue.append(temp)
              breadth.append(temp)
              visited[temp] = True
            else:
              cross.append([v.getId(),temp])

        print("Bfs:",breadth)
        print("Cross edge:",cross)
        return
    

    def mstKruskal(self):
        wt=BinHeap()
        edge={}
        tree=[]
        re=[]
        for i in self.vertList.values():
            tree.append([i.getId()])
            for j in i.getConnections():
               wt.insert([i.getWeight(j),i.getId(),j.getId()])
               
        while len(tree)!=1:
            weight,a,b=wt.delMin()
            
            posa=None
            posb=None
            for i in range(len(tree)):
                if a in tree[i]:
                    posa=i
                if b in tree[i]:
                    posb=i
            
            if posa!=posb:
                re.append([a,b])
                tree[posa].extend(tree[posb])
                tree.pop(posb)

        print("Minimum spanning tree:",sorted(re))                  
        return
    
    
    def isCyclicUtil(self, v, visited, recStack):
  
        visited[v.getId()] = True
        recStack[v.getId()] = True
  
      
        for neighbour in self.vertList.values():
            if visited[neighbour.getId()] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour.getId()] == True:
                return True
    
        recStack[v.getId()] = False
        return False
    def isCyclic(self):
        visited = [False] * (self.numVertices+ 1)
        recStack = [False] * (self.numVertices + 1)
        for node in self.vertList.values():
            if visited[node.getId()] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
    
    def topologicalSortUtil(self,v,visited,stack):
        visited[v.getId()] = True
        for i in self.vertList.values():
            if visited[i.getId()] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        stack.insert(0,v.getId())
 
    def topologicalSort(self):
        visited = [False]*self.numVertices
        stack =[]
        for i in self.vertList.values():
            if visited[i.getId()] == False:
                self.topologicalSortUtil(i,visited,stack)
        print(stack)
    
    def shortestpath(self,start,end):
        inf=sys.maxsize
        visited=[False]*self.numVertices
        d=[inf]*self.numVertices
        d[start]=0
        pq=[[[self.getVertex(start)],0]]
        path=[]
        tree=[]
        cost=inf
        while pq:

            currpath,currcost=pq.pop(0)
            if currpath[-1].getId()==end:
                path=currpath.copy()
                cost=currcost
                break # stopping condition, currpath is min guaranteed
            for neighbour in currpath[-1].getConnections():
                temp=0
                temp+=currpath[-1].getWeight(neighbour) #add weight of each neighbour at a time to temp for checking
                temp+=currcost
                if temp< d[neighbour.getId()]:
                    d[neighbour.getId()]=temp #set new min cost
                    tree.append((currpath[-1].getId(),neighbour.getId())) #to get the edges that form the Shortest Path tree
                    newpath=currpath.copy()
                    newpath.append(neighbour) #that joins the currpath
                    pq.append([newpath,temp]) #that gets appended to pq
            pq.sort(key=lambda x:x[1]) #to sort heap based on cost
        
        print("Shortest path:")
        for node in path:
            print((node.getId()),end=" ")
        print("\nTotal cost:",cost)
        print("Shortest path tree:")
        for i in range(len(d)):
            if d[i]!=inf:
                print("Edge {}: d={}".format(i,d[i]))
        print("Edges forming the Shortest Path tree:")
        print(tree)
    
    def getEdges(self):
        return self.edges
        
    
    def bellmanFord(self,src):
        inf=sys.maxsize
        d=[inf]*self.numVertices
        d[src]=0
        for _ in range(self.numVertices-1):
            for u,v,w in self.edges:
                if d[u]!=inf and d[u]+w<d[v]:
                    d[v]=d[u]+w
        # check for -ve weight cycles
        for u,v,w in self.edges:
            if d[u]!=inf and d[u]+w<d[v]:
                print("Graph contains negative weight cycles")
                return
        for i in range(1,len(d),1):
            print("Shortest path from {} to {} is {} ".format(src,i,d[i]))
            



    def mstPrim(self,start):
        inf=sys.maxsize
        d=[inf]*self.numVertices
        d[start]=0
        pq=[[[self.getVertex(start)],0]]
        path=[]
        cost=inf
        while pq:
            currpath,currcost=pq.pop(0)
            for neighbour in currpath[-1].getConnections():
                temp=0
                temp+=currpath[-1].getWeight(neighbour) #add weight of each neighbour at a time to temp for checking
                temp+=currcost
                if temp< d[neighbour.getId()]:
                    d[neighbour.getId()]=temp #set new min cost
                    newpath=currpath.copy()
                    newpath.append(neighbour) #that joins the currpath
                    pq.append([newpath,temp]) #that gets appended to pq
            pq.sort(key=lambda x:x[1]) #to sort heap based on cost
        path=currpath.copy()
        print("Prim MST:")
        for node in path:
            print((node.getId()),end=" ")

    
def testGraph():

    g = Graph()
    for i in range(5):
        g.addVertex(i)
    g.vertList
    g.addEdge(1,2,8)
    g.addEdge(2,1,8)
    g.addEdge(1,3,6)
    g.addEdge(3,1,6)
    g.addEdge(3,5,1)
    g.addEdge(5,3,1)
    g.addEdge(3,4,3)
    g.addEdge(4,3,3)
    g.addEdge(4,5,1)
    g.addEdge(5,4,1)
    

    # this is assumed to be a directed graph so make edges commutative

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    
    
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "A"):
            AdjMat= g.createAdjMatrix()
        elif (operation[0] == "B"):
            start = g.getVertex(int(operation[1]))
            g.bfs(start)
        elif (operation[0] == "D"):
            start = g.getVertex(int(operation[1]))
            g.dfs(start)
            g.printdfs()
        elif (operation[0] == "MK"):
            g.mstKruskal()
        elif (operation[0] == "MP"):
            g.mstPrim(4)
        elif (operation[0] == "IC"):
            print(g.isCyclic())
        elif (operation[0] == "TS"):
            g.topologicalSort()
        elif (operation[0] == "SP"):
            g.shortestpath(int(operation[1]),int(operation[2])) 
        elif (operation[0] == "GE"):
            print(g.getEdges())
        elif (operation[0] == "BF"):
            g.bellmanFord(int(operation[1]))
        inputs-=1

def main():
    testGraph()


if __name__ == '__main__':
    main()

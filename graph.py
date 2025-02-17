from pprint import pprint
class Graph:
      def __init__(self):
        self.adjacencyList: map = {}
        

    def show(self):
        pprint(self.adjacencyList)

    def nodeExists(self, node: str):
        """returns true if node exists in this graph"""
        return node in self.adjacencyList
    

    def edgeExists(self, node: str, to: str):
        """checks if 'node' exists and then checks if an edge from 'node' to 'to' 
        exists. returns true if both exist"""
        if not self.nodeExists(node):
            raise Exception(f"node {node} does not exist in the graph.")
        if not self.nodeExists(to):
            raise Exception(f"node {to} does not exist in the graph.")
        for entry in self.adjacencyList[node]:
            if entry[0] == to:
                return True
        return False
    
    def undirectedEdgeExists(self, node: str, other: str):
        """checks if both 'node' and 'other' exist; and then checks if edges exist in
          both directions. returns True if all these exist"""
        if not self.nodeExists(node):
            raise Exception(f"node {node} does not exist in the graph.")
        if not self.nodeExists(other):
            raise Exception(f"node {other} does not exist in the graph.")
        forwardEdge = False
        backwardEdge = False
        for entry in self.adjacencyList[node]:
            if entry[0] == other:
                forwardEdge = True
        for entry in self.adjacencyList[other]:
            if entry[0] == node:
                backwardEdge = True
        return forwardEdge and backwardEdge
        
        

    def addNode(self, node: str):
        # raise error if the node already exists in the graph.
        if self.nodeExists(node):
            raise Exception(f"node {node} already exists in the graph.")
        # add the node to the graph
        self.adjacencyList[node] = []


    def deleteNode(self, node:str):
        try:
            # delete all the edges out of this node, and the node itself.
            self.adjacencyList.pop(node)
        except KeyError:
            # raise error if node does not exist
            raise Exception("the node {node} does not exist in the graph; thus, it can't be deleted.")
        # finally, remove all the edges into the deleted node
        for key in self.adjacencyList:
            for i in range(len(self.adjacencyList[key])):
                if self.adjacencyList[key][i][0] == node:
                    self.adjacencyList[key].pop(i)
                    break


    def addEdge(self, node: str, to: str, cost:float=0):
        # check if the edge doesn't already exist
        if self.edgeExists(node, to):
            raise Exception(f"the edge from {node} to {to} already exists.")
        # add the edge
        self.adjacencyList[node].append((to, cost))


    def addUndirectedEdge(self, node:str, other:str, forwardCost:float=0, backwardCost:float=0):
        # making sure the undirected edge doesn't already exist by doing the following two ...
        # making sure a forward directed edge doesn't exist
        if self.edgeExists(node, other):
            raise Exception(f"There already exists a directed graph from {node} to {other}.")
        # making sure a backward directed edge doesn't exist
        if self.edgeExists(other, node):
            raise Exception(f"There already exists a directed graph from {other} to {node}.")
        # add the undirected edge
        self.adjacencyList[node].append((other, forwardCost))
        self.adjacencyList[other].append((node, backwardCost))

    def deleteEdge(self, node: str, to:str):
        # raise error if the edge does not exist.
        if not self.edgeExists(node, to):
            raise Exception(f"There is no edge from {node} to {to}; thus it can't be deleted.")
        # delete the edge
        for i in range(len(self.adjacencyList[node])):
            if self.adjacencyList[node][i][0] == to:
                self.adjacencyList[node].pop(i)
                break

    def deleteUndirectedEdge(self, node: str, other:str):
        # the two methods below will check for existence of a two-way end delete it.
        self.deleteEdge(node, other)
        self.deleteEdge(other, node)


    def dfs(self, start: str, target: str):
        pass

    def bfs(self, start: str, target: str):
        pass

    def ucs(self, start: str, target: str):
        pass

    def iterativeDeepeningSearch(self, start: str, target: str):  # not sure about this signature. check it out
        pass

    def bidirectionalSearch(self, start: str, target: str): # not sure about this signature. check it out
        pass

    def greedySearch(self, node: str):
        stack = [node]
        app = []
        Vistednode=[]
        while stack:
            current = stack.pop()
            if current in self.adjacencyList:
                if self.adjacencyList[current] != []:
                    if current not in Vistednode:
                        print(current)
                    else:
                        break
                    Vistednode.append(current)
                    for i in self.adjacencyList[current]:
                        app.append(i[1])
                    if app == []:
                        break
                    check = app.index(min(app))
                    stack.append(self.adjacencyList[current][check][0])
                    app.clear()
                else:
                    print(node,"no cennection")
            else:
                print(node,"not found in graph")

    def aStarSearch(self, start: str, target: str, heuristic: any):
        pass
   def degree(self):
        # dgreeof centrality = number of connected nodes/nodes-1
        app = []
        chek = []
        final = []
        second = []
        finalNode = []
        for i in self.adjacencyList:
            app.append(i)
        numberofnodes = len(app)
        denumrator = numberofnodes - 1
        for j in self.adjacencyList:
            dgree = len(self.adjacencyList[j])
            temp = [j, dgree / denumrator]
            chek.append(temp)
        print("degree centrality of Nodes", chek)
        for k in chek:
            final = k[1]
            second.append(final)
        second.sort()

        for i in range(len(second) - 1, len(second) - 4, -1):

            for l in chek:
                if l[1] == second[i]:
                    temp2 = [l[0], l[1]]
                    if temp2 not in finalNode:
                        finalNode.append(temp2)
        print("the three Nodes highest in degree centrality in order  are", finalNode)


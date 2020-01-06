class Node:
    """
    A Node that is used in Graphs
    """

    def __init__(self, name, data=None, children: "tuple of Vertex" = ()):
        self.children = list(children)
        self.data = data
        self.name = name
        self.graphRoot = None

    def getChildren(self):
        return self.children

    def getData(self):
        return self.data

    def addChild(self, child):
        if type(child) != Node: raise TypeError
        child.parent = self
        self.children.append(child)
        return

    def __str__(self):
        return str(self.name) + ":" + str(self.data)

    def toString(self):
        x = ''
        for i in self.children: x += ("\t" + str(i.child) + " @ " + str(i.weight) + "\n")
        return str(self) + " Connections: \n" + x


class Vertex:
    def __init__(self, child: Node, parent: Node = None, weight: float = 0):
        self.child = child
        self.parent = parent
        self.weight = weight

    def __str__(self):
        return str(self.parent) + " -> " + str(self.child) + " @ " + str(self.weight)


class Graph:
    """
    A simple, generic Graph class with some functions to parse it.
    Graph nodes are Node objects.
    """

    class NodeNotInGraph(Exception):
        """The node you are attempting to connect to does not exist in the graph"""
        pass

    class NodeNameConflict(Exception):
        """The node you are attempting to add in the graph already exists"""
        pass

    def __init__(self, rootNode: Node):
        self.nodes = [rootNode]
        self.nodeNames = [rootNode.name]
        self.root = rootNode
        self.vertices = []

    def addNode(self, node: Node):
        if node not in self.nodes and node.name not in self.nodeNames:
            self.nodes.append(node)
            self.nodeNames.append(node.name)
        else:
            raise Graph.NodeNameConflict

    def nodeFromName(self, one):
        if type(one) is not Node:
            for i in self.nodes:
                if i.name == one:
                    one = i
                    break

        if type(one) is not Node: raise Graph.NodeNotInGraph

        return one

    def addVertex(self, start, end) -> Vertex:

        start, end = self.nodeFromName(start), self.nodeFromName(end)

        t = Vertex(end, start)
        self.vertices.append(t)
        start.children.append(t)
        return t

    def changeRoot(self, root: Node) -> Node:
        self.root = root
        return self.root

    def parseNodeList(self, data):
        pass

    def DFS(self, name) -> Node:
        temp = [self.root]

        def parse(iterator: Vertex):
            # print("\tChecking " + str(iterator.child) + " found " + str(iterator.child.name == name))
            if iterator.child.name == name:
                return iterator.child
            for i in iterator.child.children:
                if i.child not in temp:
                    temp.append(i.child)
                    t = parse(i)
                    try:
                        if t.name == name: return t
                    except Exception as e:
                        pass
            return None

        return parse(Vertex(self.root))

    def BFS(self, name) -> Node:
        pass

    def clearRoot(self):
        self.root.children = []
        self.root.graphRoot = self


class WeightedGraph(Graph):
    """
    A Graph that uses weighted node connections and includes some more useful
    functions to parse
    The weighted graph is by default bidirectional meaning every node points to
    it's parent
    """

    class GraphsNotDisjoint(Exception):
        """The 2 Graphs attempting to merge are not disjoint"""
        pass

    def __init__(self, rootNode: Node):
        super().__init__(rootNode)

    def addNode(self, node: Node):
        super().addNode(node)

    def addVertex(self, start, end, weight: float, bidirectional: bool = True) -> bool:
        try:
            t = super().addVertex(start, end)
            t.weight = weight
            if bidirectional: self.addVertex(end, start, weight, False)
        except Exception as e:
            print(e)
            return False
        return True

    def dijkstra(self, start, end):
        start, end = super().nodeFromName(start), super().nodeFromName(end)  # Get Nodes from Node Names

        dijkstra = {x: [float('inf'), x] for x in self.nodes}  # Create dict of all nodes with their
        dijkstra[start] = [0, start]  # distance from start and previous node
        visited = []  # Create list of visited nodes

        def nextNode():
            tempDist = float('inf')
            tempNode = None
            for j in dijkstra:
                if j not in visited and dijkstra[j][0] < tempDist:
                    tempNode = j
                    tempDist = dijkstra[j][0]
            return tempNode

        curr = start
        while curr is not None:
            for i in curr.children:
                if dijkstra[curr][0] + i.weight <= dijkstra[i.child][0]:
                    dijkstra[i.child][0] = dijkstra[curr][0] + i.weight
                    dijkstra[i.child][1] = curr
            visited.append(curr)
            curr = nextNode()

        visited = []
        curr = end
        while curr != start:
            visited.append(curr)
            curr = dijkstra[curr][1]
        visited.append(start)
        visited.reverse()
        return dijkstra[end][0], visited

    def kruskal(self):

        vert = self.vertices
        vert.sort(key=lambda x: x.weight)

        disjoints = [WeightedGraph(x) for x in self.nodes]
        for j in disjoints: j.clearRoot()

        def isDisjoint(x: Vertex) -> bool:
            return x.parent.graphRoot != x.child.graphRoot

        def join(x: Vertex) -> WeightedGraph:
            if not isDisjoint(x): raise WeightedGraph.GraphsNotDisjoint
            # print("Checking vertex " + str(x) + " is connecting disjoints")

            # Remove child Graph from disjoints list
            disjoints.remove(x.child.graphRoot)

            # Merge Node and Vertices lists
            x.parent.graphRoot.nodes += x.child.graphRoot.nodes
            x.parent.graphRoot.nodeNames += x.child.graphRoot.nodeNames
            x.parent.graphRoot.vertices += x.child.graphRoot.vertices
            # print('\tNow contains' + str(x.parent.graphRoot.nodeNames))

            # Make every node in child graph point to parent graph
            for k in x.child.graphRoot.nodes:
                k.graphRoot = x.parent.graphRoot
                # print("\t\tNode " + str(k) + " is changing root to point to " + str(x.parent.graphRoot.root))

            # Add vertex that joins the too trees
            x.parent.graphRoot.vertices.append(x)
            x.parent.graphRoot.vertices.append(Vertex(x.parent, x.child, x.weight))

        for j in vert:
            try:
                join(j)
            except Exception as e:
                pass

        return disjoints


class BinaryIndexedTree:
    """
    A class that acts like a BIT. Uses Node objects as nodes and includes
    append(), search(), pop(), sort() functions.
    """

    def __init__(self, rootData=0):
        self.n = 1
        self.root = Node(0, data=rootData, children=(None, None))

    def append(self, data):
        iterator = self.root

        while True:
            # if data == iterator.data: return        #Uncomment if you do not want duplicate values!
            if int(data) >= int(iterator.data):
                if iterator.children[1] is None:
                    iterator.children[1] = Vertex(Node(self.n, data=data, children=(None, None)))
                    self.n += 1
                    return
                else:
                    iterator = iterator.children[1].child
            else:
                if iterator.children[0] is None:
                    iterator.children[0] = Vertex(Node(self.n, data=data, children=(None, None)))
                    self.n += 1
                    return
                else:
                    iterator = iterator.children[0].child

    def sort(self):
        def get(iterator: Vertex):
            temp = []
            if iterator is None:
                return temp
            else:
                temp += get(iterator.child.children[0])
                if iterator is not None: temp.append(iterator.child.data)
                temp += get(iterator.child.children[1])
                return temp

        return get(Vertex(self.root))

    def search(self, data):
        def get(iterator: Vertex):
            if iterator is None:
                return False, None
            elif iterator.child.data == data:
                return True, iterator.child
            else:
                t = get(iterator.child.children[0])
                if t[0]: return t
                t = get(iterator.child.children[1])
                if t[0]:
                    return t
                else:
                    return False, None

        return get(Vertex(self.root))


if __name__ == '__main__':
    '''
    # A Binary Index Tree example
    a = BinaryIndexedTree(1);
    a.append(-2);
    a.append(-7);
    a.append(-4);
    a.append(2);
    a.append(99);
    a.append(-5)
    a.append(65);
    a.append(5);
    a.append(-9);
    a.append(0);
    a.append(104);
    a.append(-5)
    print(a.sort())
    case, res = a.search(-5)
    if case:
        print(res)
    else:
        print("Not found")
    '''
    '''
    # A simple graph example
    a: Graph = Graph(Node(1, data=""))
    a.addNode(Node(2, data=""))
    a.addNode(Node(3, data=""))
    a.addNode(Node(4, data=""))
    a.addNode(Node(5, data=""))
    a.addNode(Node(6, data=""))
    a.addNode(Node(7, data=""))
    a.addNode(Node(8, data=""))
    a.addVertex(1, 2)
    a.addVertex(2, 3)
    a.addVertex(3, 4)
    a.addVertex(1, 5)
    a.addVertex(5, 6)
    a.addVertex(6, 7)
    a.addVertex(6, 8)
    a.addVertex(4, 2)
    a.addVertex(6, 3)
    a.addVertex(1, 8)
    print("\nSTARTING SEARCH\n")
    print(a.DFS(8))
    '''
    '''
    # A simple weighted bidirectional graph (Dijkstra's algorithm)
    a = WeightedGraph(Node(1, data="1"))
    a.addNode(Node(2, data="2"))
    a.addNode(Node(3, data="3"))
    a.addNode(Node(4, data="4"))
    a.addNode(Node(5, data="5"))
    a.addNode(Node(6, data="6"))
    a.addVertex(1, 2, 7)
    a.addVertex(1, 3, 9)
    a.addVertex(1, 6, 14)
    a.addVertex(2, 3, 10)
    a.addVertex(2, 4, 15)
    a.addVertex(3, 4, 11)
    a.addVertex(4, 5, 6)
    a.addVertex(3, 6, 2)
    a.addVertex(6, 5, 9)
    shortestDist, path = a.dijkstra(1, 5)
    print(shortestDist)
    for i in path: print(i)
    '''
    # A simple weighted bidirectional graph (Kruskal's algorithm)
    a = WeightedGraph(Node(1, data="A"))
    a.addNode(Node(2, data="B"))
    a.addNode(Node(3, data="C"))
    a.addNode(Node(4, data="D"))
    a.addNode(Node(5, data="E"))
    a.addNode(Node(6, data="F"))
    a.addNode(Node(7, data="G"))
    a.addVertex(1, 2, 7)
    a.addVertex(1, 4, 5)
    a.addVertex(2, 3, 8)
    a.addVertex(2, 4, 9)
    a.addVertex(2, 5, 7)
    a.addVertex(3, 5, 5)
    a.addVertex(4, 5, 15)
    a.addVertex(4, 6, 6)
    a.addVertex(5, 6, 8)
    a.addVertex(5, 7, 9)
    a.addVertex(6, 7, 11)
    for i in a.kruskal()[0].vertices[::2]: print(i)

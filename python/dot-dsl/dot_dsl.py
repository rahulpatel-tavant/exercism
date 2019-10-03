NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data == None: return
    
        if not type(data) ==  list:
            raise TypeError('invalid type')  
        for graph_attr in data:
            if len(graph_attr) <= 2:
                raise TypeError('invalid type')
            if type(graph_attr[1]) == int:
                raise ValueError("invalid values")

            if graph_attr[0] == NODE:
                self.nodes.append(Node(graph_attr[1], graph_attr[2]))
            elif graph_attr[0] == EDGE: 
                self.edges.append(Edge(graph_attr[1], graph_attr[2], graph_attr[3]))
            else:
                self.attrs[graph_attr[1]] = graph_attr[2] 

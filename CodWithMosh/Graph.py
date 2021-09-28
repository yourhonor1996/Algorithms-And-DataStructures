class Graph(object):
    class Node(object):
        def __init__(self, label:str) -> None:
            self.label = label
            
        def __repr__(self) -> str:
            return str(self.label)

    def __init__(self) -> None:
        self.nodes : dict[str, Graph.Node] = {}
        self.adjacency : dict[Graph.Node, list[Graph.Node]] = {}

    def get_node(self, label):
        return self.nodes.get(label)

    def node_exists(self, label):
        return not self.get_node(label) is None

    def validate_edge(self, source: str, to: str):
        if (not self.node_exists(source)) or (not self.node_exists(to)):
            raise Exception("The node doesn't exist.")

    def add_node(self, label:str):
        new_node = Graph.Node(label)
        if not self.node_exists(label):
            self.nodes[label] = new_node
            self.adjacency[new_node] = []

    def add_edge(self, source:str, to:str):
        self.validate_edge(source, to)
        source_node = self.get_node(source)
        to_node = self.get_node(to)
        self.adjacency[source_node].append(to_node)
        
    def show_graph(self) -> str:
        for label, node in self.nodes.items():
            adjacency = self.adjacency[node]
            if len(adjacency) != 0:
                print(f"Node {label} is conndected to {adjacency}")
        
    def remove_node(self, label):
        node = self.get_node(label)
        if node is None:
            return
        
        for n in self.adjacency.keys():
            try:
                self.adjacency[n].remove(node)
            except ValueError:
                pass
        
        self.adjacency.pop(node)
        self.nodes.pop(node.label)

    def remove_edge(self, source:str, to:str):
        self.validate_edge(source, to)
        source_node = self.get_node(source)
        to_node = self.get_node(to)

        try:
            self.adjacency[source_node].remove(to_node)
        except ValueError:
            pass


graph = Graph()
graph.add_node('p0')
graph.add_node('p1')
graph.add_node('p2')
graph.add_node('p3')
graph.add_node('p4')
graph.add_edge('p0', 'p1')
graph.add_edge('p0', 'p2')
graph.add_edge('p3', 'p4')
graph.add_edge('p3', 'p1')

# graph.remove_edge('p3', 'p4')
# graph.remove_edge('p3', 'p4')
# graph.remove_edge('p3', 'p1')
graph.remove_node('p1')
graph.remove_node('p1')
print('done')
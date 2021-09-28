from typing import Dict
from SingleLinkedList import LinkedList


class Graph(object):
    class Node(object):
        def __init__(self, label: str, index: int = -1) -> None:
            self.label = label
            self.index: int = index
            self.edges = LinkedList()

        def __repr__(self) -> str:
            return f"{self.index}-{self.label}"
        
        def add_edge(self, index):
            result = self.edges.addlast_if_nonexistant(index)
            if result is None:
                return False
            return True
        
        def remove_edge(self, index):
            result = self.edges.pop(index)
            if result is None:
                return False
            return True
            

    def __init__(self) -> None:
        self.nodes: Dict[str, Graph.Node] = {}

    def validate_node(self, label: str):
        if not self.node_exists(label):
            print("The node doesn't exist.")
            return False
        return True

    def node_exists(self, label: str):
        return not self.nodes.get(label) is None

    def get_node(self, label: str):
        return self.nodes.get(label)

    def validate_edge(self, source: str, to: str):
        if (not self.node_exists(source)) or (not self.node_exists(to)):
            raise Exception("The node doesn't exist.")

    def edge_exists(self, source: str, to: str):
        self.validate_edge(source, to)

        source_node = self.get_node(source)
        to_index = self.get_node(to).index
        return source_node.edges.contains(to_index)

    def add_node(self, label: str):
        # if node already exists
        if self.node_exists(label):
            raise Exception("The node already exists. You cant add a node that already exists")

        new_node = Graph.Node(label, len(self.nodes))
        self.nodes[label] = new_node

    def remove_node(self, label: str):
        if not self.validate_node:
            return

        deleted_node = self.nodes.pop(label)
        for node in self.nodes.values():
            node.remove_edge(deleted_node.index)

        return deleted_node

    def add_edge(self, source: str, to: str):
        self.validate_edge(source, to)

        to_node = self.get_node(to)
        souce_node = self.get_node(source)
        return souce_node.add_edge(to_node.index)

    def remove_edge(self, source: str, to: str):
        self.validate_edge(source, to)

        to_node = self.get_node(to)
        source_node = self.get_node(source)
        source_node.remove_edge(to_node.index)

    def show_graph(self) -> str:
        for label, node in self.nodes.items():
            print(f"Node {label} has nodes {node.edges}")


graph = Graph()
graph.add_node("p0")
graph.add_node("p1")
graph.add_node("p2")
graph.add_node("p3")
graph.add_edge("p0", "p1")
graph.add_edge("p2", "p1")
graph.add_edge("p3", "p1")
graph.add_edge("p1", "p2")
graph.add_edge("p3", "p2")
graph.remove_edge("p3", "p2")
# graph.remove_node("p1")
graph.show_graph()
print("done")

from queue import PriorityQueue
from typing import Union


class MyPriorityQueue(PriorityQueue):
    def __repr__(self) -> str:
        return str(self.queue)


class WeightedGraph(object):
    class Node(object):
        def __init__(self, label: str) -> None:
            self.label = label
            self.edges: set[WeightedGraph.Edge] = set()

        def __repr__(self) -> str:
            return self.label

        def add_edge(self, to: "WeightedGraph.Node", weight: int):
            self.edges.add(WeightedGraph.Edge(self, to, weight))

        def get_edges(self):
            return self.edges

    class Edge(object):
        def __init__(self, source: "WeightedGraph.Node", to: "WeightedGraph.Node", weight: int) -> None:
            self.source: WeightedGraph.Node = source
            self.to: WeightedGraph.Node = to
            self.weight: int = weight

        def __repr__(self) -> str:
            return f"{self.source}>{self.to}:{self.weight}"

    class NodeEntry(object):
        def __init__(self, node: "WeightedGraph.Node", priority: int) -> None:
            self.node = node
            self.priority = priority

        def __repr__(self) -> str:
            return f"n:{self.node}|p:{self.priority}"

        def __eq__(self, other: "WeightedGraph.NodeEntry") -> bool:
            return self.priority == other.priority

        def __gt__(self, other: "WeightedGraph.NodeEntry") -> bool:
            return self.priority > other.priority

        def __ge__(self, other: "WeightedGraph.NodeEntry") -> bool:
            return self.priority >= other.priority

        def __lt__(self, other: "WeightedGraph.NodeEntry") -> bool:
            return self.priority < other.priority

        def __le__(self, other: "WeightedGraph.NodeEntry") -> bool:
            return self.priority <= other.priority

    class Path(object):
        def __init__(self) -> None:
            self.nodes: list[str] = []

        def add(self, node: "WeightedGraph.Node"):
            self.nodes.append(node.label)

        def __repr__(self) -> str:
            return str(self.nodes)

    def __init__(self) -> None:
        self.nodes: dict[str, WeightedGraph.Node] = {}
        # self.adjacency: dict[WeightedGraph.Node, list[WeightedGraph.Edge]] = {}

    @staticmethod
    def dict_set_generator(input_iterable: Union[set, dict]):
        if type(input_iterable) is set:
            for item in input_iterable:
                yield item
        if type(input_iterable) is dict:
            for key, value in input_iterable.items():
                yield (key, value)

    def get_node(self, label: str):
        return self.nodes.get(label)

    @property
    def size(self):
        return len(self.nodes)

    def node_exists(self, label: str):
        return not self.get_node(label) is None

    def __contains__(self, node: Union["WeightedGraph.Node", str]):
        if type(node) is str:
            return not self.get_node(node) is None

        elif type(node) is WeightedGraph.Node:
            return not self.get_node(node.label) is None

    def validate_edge(self, source: str, to: str):
        if self.get_node(source) is None:
            raise Exception(f"The node Node<{source}> doesn't exist!")
        if self.get_node(to) is None:
            raise Exception(f"The node Node<{to}> doesn't exist!")

    def add_node(self, label):
        if not label in self:
            self.nodes[label] = WeightedGraph.Node(label)

    def add_edge(self, source: str, to: str, weight: int):
        self.validate_edge(source, to)

        source_node = self.get_node(source)
        to_node = self.get_node(to)

        source_node.add_edge(to_node, weight)
        to_node.add_edge(source_node, weight)

    def show_graph(self):
        for label, node in self.nodes.items():
            edges = node.get_edges()
            if len(edges) != 0:
                print(f"Node {label} is conndected to {edges}")

    # TODO cerate shortest path method
    def get_shortest_path(self, source: str, to: str):
        source_node = self.get_node(source)
        to_node = self.get_node(to)

        distances: dict[WeightedGraph.Node, int] = {}
        for node in self.nodes.values():
            distances[node] = float("inf")
        distances[source_node] = 0

        previous_nodes: dict[WeightedGraph.Node, WeightedGraph.Node] = {}

        visited: set[WeightedGraph.Node] = set()
        pq = MyPriorityQueue()
        pq.put(WeightedGraph.NodeEntry(source_node, 0))

        while not pq.empty():
            current: WeightedGraph.Node = pq.get().node
            visited.add(current)

            for edge in current.get_edges():
                if edge.to in visited:
                    continue
                new_distance = distances.get(current) + edge.weight
                if new_distance < distances.get(edge.to):
                    distances[edge.to] = new_distance
                    previous_nodes[edge.to] = current
                    pq.put(WeightedGraph.NodeEntry(edge.to, new_distance))

        return self._build_path(to_node, previous_nodes)

    def _build_path(self, to_node: "WeightedGraph.Node", previous_nodes: dict):
        stack = []
        stack.append(to_node)
        previous = previous_nodes.get(to_node)
        # return distances.get(to_node)
        while not previous is None:
            stack.append(previous)
            previous = previous_nodes.get(previous)

        path = WeightedGraph.Path()
        while not len(stack) == 0:
            path.add(stack.pop())

        return path

    def get_min_spanning_tree(self):
        tree = WeightedGraph()
        priorityq: MyPriorityQueue[tuple[int, WeightedGraph.Edge]] = MyPriorityQueue()

        _, first_node = next(self.dict_set_generator(self.nodes))
        tree.add_node(first_node.label)

        for edge in first_node.get_edges():
            priorityq.put((edge.weight, edge))

        if priorityq.empty():
            return tree

        while tree.size < self.size:
            _, new_edge = priorityq.get()
            new_node = new_edge.to

            if new_node in tree:
                continue

            tree.add_node(new_node.label)
            tree.add_edge(new_edge.source.label, new_node.label, new_edge.weight)

            for edge in new_node.get_edges():
                if not edge.to in tree:
                    priorityq.put((edge.weight, edge))

        return tree

    def has_cycle(self):
        def _has_cycle(node: "WeightedGraph.Node", parent: "WeightedGraph.Node", visited: set):
            visited.add(node)

            for edge in node.get_edges():
                if edge.to == parent:
                    continue

                if edge.to in visited or _has_cycle(edge.to, node, visited):
                    return True

            return False

        visited = set()
        for node in self.nodes.values():
            if not node in visited and _has_cycle(node, None, visited):
                return True
            return False


q = PriorityQueue()
graph = WeightedGraph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge("A", "B", 3)
graph.add_edge("A", "D", 2)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "E", 1)
graph.add_edge("B", "D", 6)
graph.add_edge("E", "D", 5)
graph.add_edge("C", "D", 1)

# graph.add_edge("A", "B", 3)
# graph.add_edge("A", "C", 1)
# graph.add_edge("C", "B", 2)
# graph.add_edge("C", "D", 5)
# graph.add_edge("D", "B", 4)

# (graph.show_graph())
# print(graph.get_shortest_distance("C", "E"))
# graph.get_min_spanning_tree().show_graph()
# print(graph.has_cycle())
print(graph.get_shortest_path("A", "E"))

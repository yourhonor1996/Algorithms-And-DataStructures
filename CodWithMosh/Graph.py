class Graph(object):
    class Node(object):
        def __init__(self, label: str) -> None:
            self.label = label

        def __repr__(self) -> str:
            return str(self.label)

    def __init__(self) -> None:
        self.nodes: dict[str, Graph.Node] = {}
        self.adjacency: dict[Graph.Node, list[Graph.Node]] = {}

    def get_node(self, label):
        return self.nodes.get(label)

    @staticmethod
    def set_generator(input_set:set):
        for item in input_set:
            yield item

    def get_neighbors(self, label):
        return self.adjacency[self.get_node(label)]

    def node_has_nochildren(self, label: str):
        return len(self.get_neighbors(label)) == 0

    def node_exists(self, label):
        return not self.get_node(label) is None

    def validate_edge(self, source: str, to: str):
        if (not self.node_exists(source)) or (not self.node_exists(to)):
            raise Exception("The node doesn't exist.")

    def add_node(self, label: str):
        new_node = Graph.Node(label)
        if not self.node_exists(label):
            self.nodes[label] = new_node
            self.adjacency[new_node] = []

    def add_edge(self, source: str, to: str):
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

    def remove_edge(self, source: str, to: str):
        self.validate_edge(source, to)
        source_node = self.get_node(source)
        to_node = self.get_node(to)

        try:
            self.adjacency[source_node].remove(to_node)
        except ValueError:
            pass

    def dft_recursion(self, root_label: str):
        def _dft_recursion(results: list, root_label: str, visited: set = None):
            if visited == None:
                visited = set()

            root = self.get_node(root_label)
            if root is None:
                return

            # if root not in visited:
            #     results.append(root)
            #     visited.add(root)
            # else:
            #     return

            # if self.node_has_nochildren(root.label):
            #     return
            results.append(root)
            visited.add(root)

            for node in self.get_neighbors(root_label):
                if node not in visited:
                    _dft_recursion(results, node.label, visited)

        results = []
        _dft_recursion(results, root_label)
        return results

    def dft_iteration(self, root_label: str):
        root = self.get_node(root_label)
        if root is None:
            return

        results = []
        stack: list[Graph.Node] = []
        stack.append(root)
        visited = set()

        while len(stack) != 0:
            current = stack.pop()

            if current in visited:
                continue
            results.append(current)
            visited.add(current)

            for neighbor in self.get_neighbors(current.label):
                if not neighbor in visited:
                    stack.append(neighbor)

        return results

    def bft_iteration(self, root_label: str):
        root = self.get_node(root_label)
        if root is None:
            return

        results = []
        queue: list[Graph.Node] = []
        queue.append(root)
        visited = set()

        while len(queue) != 0:
            current = queue.pop(0)

            if current in visited:
                continue
            results.append(current)
            visited.add(current)

            for neighbor in self.get_neighbors(current.label):
                if not neighbor in visited:
                    queue.append(neighbor)

        return results

    def topological_sort(self):
        def traverse(stack: list, root_label: str, visited: set = None):
            if visited is None:
                visited = set()

            root = self.get_node(root_label)
            if root is None:
                return

            if root in visited:
                return

            visited.add(root)

            for node in self.get_neighbors(root_label):
                traverse(stack, node.label, visited)

            stack.append(root)

        tempstack = []
        tempset = set()
        for label in self.nodes.keys():
            traverse(tempstack, label, tempset)

        results = []
        while len(tempstack) != 0:
            results.append(tempstack.pop())

        return results

    def has_cycle(self) -> bool:
        def _has_cycle(root:"Graph.Node", all:set, visitting:set, visited:set):
            all.remove(root)
            visitting.add(root)

            for neighbor in self.get_neighbors(root.label):
                if neighbor in visited:
                    continue
                if neighbor in visitting:
                    return True
                if _has_cycle(neighbor, all, visitting, visited):
                    return True
            
            visitting.remove(root)
            visited.add(root)

            return False
        
        all = set(self.nodes.values())
        visitting = set()
        visited = set()
        
        generator = Graph.set_generator(all)
        while len(all) != 0:
            current = next(generator)
            if _has_cycle(current, all, visitting, visited):
                return True
        return False

graph = Graph()
# graph.add_node("A")
# graph.add_node("B")
# graph.add_node("C")
# graph.add_node("D")
# # graph.add_node("E")
# graph.add_edge("A", "B")
# graph.add_edge("B", "D")
# graph.add_edge("D", "C")
# graph.add_edge("A", "C")

graph.add_node("X")
graph.add_node("A")
graph.add_node("B")
graph.add_node("P")
# graph.add_node("E")
graph.add_edge("X", "A")
graph.add_edge("X", "B")
graph.add_edge("B", "A")
graph.add_edge("A", "X")
graph.add_edge("A", "P")
graph.add_edge("B", "P")
# graph.show_graph()
# results = []
# print(graph.dft_recursion(root_label="G"))
# print(graph.node_has_nochildren('A'))
# print(graph.dft_iteration('A'))
# print(graph.bft_iteration('A'))
# print(results)
# print(graph.topological_sort())
print(graph.has_cycle())
# print(graph.topological_sort())

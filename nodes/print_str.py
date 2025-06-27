from node import Node

class PrintStrNode(Node):
    def input(self, w: str):
        self._input = w

    def exec(self):
        print(self._input)

    def get_node_id(self) -> str:
        return "print_str_node"

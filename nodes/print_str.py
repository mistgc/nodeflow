from typing import Optional
from node import Node


class PrintStrNode(Node):
    _input: Optional[str] = None

    def input(self, w: str):
        self._input = w
        super().__init__()

    def exec(self):
        print(self._input)

    def get_node_id(self) -> str:
        return "print_str_node"

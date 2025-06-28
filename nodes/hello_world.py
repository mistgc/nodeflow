from typing import Optional
from node import Node


class HelloWorldNode(Node):
    _input: Optional[str] = None
    _output: Optional[str] = None

    def __init__(self, w: Optional[str] = None):
        self._input = w
        super().__init__()

    def input(self, w: str):
        self._input = w

    def exec(self):
        if self._input is None:
            self._input = ""
        self._output = f"Hello world from {self._input}!"

    def output(self) -> str:
        if self._output is None:
            raise ValueError("The output of the HelloWorldNode is None")
        return self._output

    def get_node_id(self) -> str:
        return "hello_world_node"

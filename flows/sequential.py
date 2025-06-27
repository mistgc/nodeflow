from typing import Optional, List, Any
from node import Node
from flow import Flow

class Sequential(Flow):
    _node_list: List[Node] = []
    _output: Optional[Any] = None

    def __init__(self, *nodes: Node):
        self._node_list.extend(nodes)

    def exec(self):
        params = None
        for node in self._node_list:
            if params is not None:
                node.input(params)
            node.exec()
            params = node.output()
        self._output = params

    def output(self):
        return self._output

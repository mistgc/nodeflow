from typing import Optional, List, Any
from node import Node, NodeStatus
from flow import Flow


class Sequential(Flow):
    _node_list: List[Node] = []
    _output: Optional[Any] = None

    def __init__(self, *nodes: Node):
        super().__init__()
        self._node_list.extend(nodes)

    def exec(self):
        params = None
        for node in self._node_list:
            if params is not None:
                node.input(params)
            node._exec()
            if node.status == NodeStatus.Completed:
                params = node.output()
            elif node.status == NodeStatus.Erred:
                raise RuntimeError(f"[Err] {node.node_id}: {node.emsg}")
            else:
                raise NotImplementedError()
        self._output = params

    def output(self):
        return self._output

import requests
from typing import Optional
from node import Node


class GetRequestNode(Node):
    _request_dest: str = ""
    _response: Optional[requests.Response] = None

    def __init__(self, request_dest: Optional[str] = None):
        if request_dest is not None:
            self._request_dest = request_dest
        super().__init__()

    def input(self, request_dest: Optional[str]):
        if request_dest is not None:
            self._request_dest = request_dest

    def exec(self):
        self._response = requests.get(self._request_dest)

    def output(self):
        return self._response

    @property
    def node_id(self) -> str:
        return "get_request_node"

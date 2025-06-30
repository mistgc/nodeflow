from enum import Enum
from typing import Optional
import requests
from node import Node


class Resp2TextNodeError(Enum):
    RespInvalid = 1


class Resp2TextNode(Node):
    _resp: Optional[requests.Response] = None
    _output: Optional[str] = None

    def input(self, resp: requests.Response):
        self._resp = resp

    def exec(self):
        if self._resp is None:
            self.err(
                Resp2TextNodeError.RespInvalid,
                "the `_resp` of the `Resp2TextNode` is none.",
            )
            return
        self._output = self._resp.text

    def output(self):
        return self._output

    @property
    def node_id(self) -> str:
        return "utils/resp2text_node"

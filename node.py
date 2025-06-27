from typing import Optional, Any
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self):
        _input: Optional[Any] = None
        _output: Optional[Any] = None

    def input(self, *_args, **_kwargs) -> Any:
        return None

    def exec(self, *_args, **_kwargs) -> Any:
        return None

    def output(self, *_args, **_kwargs) -> Any:
        return None

    @abstractmethod
    def get_node_id(self) -> str:
        pass

from pydantic import BaseModel
from typing import Any
from abc import ABC, abstractmethod


class Node(BaseModel, ABC):
    def __init__(self):
        return

    def input(self, *_args, **_kwargs) -> Any:
        return None

    def exec(self, *_args, **_kwargs) -> Any:
        return None

    def output(self, *_args, **_kwargs) -> Any:
        return None

    @abstractmethod
    def get_node_id(self) -> str:
        pass

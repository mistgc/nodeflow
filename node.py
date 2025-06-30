from pydantic import BaseModel
from typing import Any
from abc import ABC, abstractmethod
from typing import Optional
import time
from enum import Enum


class NodeStatus(Enum):
    padding = 1
    executing = 2
    completed = 3
    erred = 4


class Node(BaseModel, ABC):
    _exec_start_ms: float = 0.0
    _exec_end_ms: float = 0.0
    _status: NodeStatus = NodeStatus.padding
    _etype: Optional[Enum] = None
    _emsg: str = ""

    def __init__(self):
        return

    def err(self, etype: Enum, emsg: str = ""):
        self._status = NodeStatus.erred
        self._etype = etype
        self._emsg = emsg

    @property
    def emsg(self) -> str:
        return self._emsg

    @property
    def etype(self) -> Optional[Enum]:
        return self._etype

    def input(self, *_args, **_kwargs) -> Any:
        return None

    def _exec(self, *args, **kwargs) -> Any:
        self._status = NodeStatus.executing
        self._exec_start_ms = time.time() * 1000  # Convert into ms
        self.exec(*args, **kwargs)
        self._exec_end_ms = time.time() * 1000  # Convert into ms
        self._status = NodeStatus.completed

    @property
    def elapsed_time(self) -> float:
        """
        Return:
            Execution time in milliseconds
        """
        return self._exec_end_ms - self._exec_start_ms

    def exec(self, *_args, **_kwargs) -> Any:
        return None

    def output(self, *_args, **_kwargs) -> Any:
        return None

    @abstractmethod
    def get_node_id(self) -> str:
        pass

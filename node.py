from pydantic import BaseModel
from typing import Any
from abc import ABC, abstractmethod
import time


class Node(BaseModel, ABC):
    _exec_start_ms: float = 0.0
    _exec_end_ms: float = 0.0

    def __init__(self):
        return

    def input(self, *_args, **_kwargs) -> Any:
        return None

    def _exec(self, *args, **kwargs) -> Any:
        self._exec_start_ms = time.time() * 1000  # Convert into ms
        self.exec(*args, **kwargs)
        self._exec_end_ms = time.time() * 1000  # Convert into ms

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

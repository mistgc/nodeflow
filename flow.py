from pydantic import BaseModel
from typing import Any
from abc import ABC, abstractmethod

class Flow(BaseModel, ABC):
    def input(self, *args, **kwargs) -> Any:
        return None

    def output(self, *args, **kwargs) -> Any:
        return None

    @abstractmethod
    def exec(self, *args, **kwargs) -> Any:
        pass

    def terminate(self):
        raise InterruptedError("Flow terminate.")

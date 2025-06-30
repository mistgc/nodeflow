from typing import Optional
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
from node import Node


class ScatterNode(Node):
    _X: Optional[np.ndarray] = None
    _Y: Optional[np.ndarray] = None
    _fig: Optional[Figure] = None
    _axes: Optional[Axes] = None

    def __init__(self, X: Optional[np.ndarray] = None, Y: Optional[np.ndarray] = None):
        super().__init__()
        self._X = X
        self._Y = Y

    def input(self, X: np.ndarray, Y: np.ndarray):
        self._X = X
        self._Y = Y

    def exec(self):
        self._fig, self._axes = plt.subplots()
        if self._X is not None and self._Y is not None:
            self._axes.scatter(self._X, self._Y)

    def output(self) -> Figure:
        if self._fig is None:
            raise ValueError("The `_fig` of the `ScatterNode` is None.")
        return self._fig

    @property
    def node_id(self) -> str:
        return "plots/scatter_node"

from node import Node
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import Optional
import numpy as np


class PlotNode(Node):
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
            self._axes.plot(self._X, self._Y)

    def output(self) -> Figure:
        if self._fig is None:
            raise ValueError("The `_fig` of the `PlotNode` is None.")
        return self._fig

    def get_node_id(self) -> str:
        return "plots/plot_node"

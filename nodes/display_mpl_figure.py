import matplotlib.pyplot as plt
from node import Node
from typing import Optional
from matplotlib.figure import Figure


def _on_key(fig):
    return lambda _: plt.close(fig)


class DisplayMplFigureNode(Node):
    _fig: Optional[Figure] = None

    def input(self, fig: Figure):
        self._fig = fig

    def exec(self):
        if self._fig is None:
            raise ValueError("The `_fig` of the `DisplayImageNode` is None.")
        self._fig.canvas.mpl_connect("key_press_event", _on_key(self._fig))
        self._fig.show()
        plt.show()

    def get_node_id(self) -> str:
        return "display_image_node"

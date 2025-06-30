import matplotlib.pyplot as plt
from node import Node
from PIL.Image import Image
from typing import Optional
from matplotlib.figure import Figure
from matplotlib.axes import Axes


def _on_key(fig):
    return lambda _: plt.close(fig)


class DisplayImageNode(Node):
    _image: Optional[Image] = None
    _fig: Optional[Figure] = None
    _axes: Optional[Axes] = None

    def input(self, image: Image):
        self._image = image

    def exec(self):
        self._fig, self._axes = plt.subplots()
        if self._image is None:
            raise ValueError("The image of the `DisplayImageNode` is None.")
        self._axes.imshow(self._image)
        self._axes.axis("off")
        self._fig.canvas.mpl_connect("key_press_event", _on_key(self._fig))
        self._fig.show()
        plt.show()

    @property
    def node_id(self) -> str:
        return "display_image_node"

import io
import PIL.Image as pimage
from typing import Optional
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from node import Node


class Fig2ImgNode(Node):
    _fig: Optional[Figure] = None
    _img: Optional[pimage.Image] = None

    def input(self, fig: Figure):
        self._fig = fig

    def exec(self):
        img_buf = io.BytesIO()
        if self._fig is None:
            raise ValueError("The `_fig` of the `Fig2ImgNode` is None.")
        self._fig.savefig(img_buf, format="png", dpi=600)
        plt.close(self._fig)
        img = pimage.open(img_buf)
        self._img = img

    def output(self):
        if self._img is None:
            raise ValueError("The `_img` of the `Fig2ImgNode` is None.")
        return self._img

    def get_node_id(self) -> str:
        return "utils/fig2img_node"

import flows
import nodes
import nodes.utils
import nodes.plots as nplots
import numpy as np


def _f(x: np.ndarray):
    return np.sin(x)


def test_hello_world():
    flow = flows.Sequential(nodes.HelloWorldNode("NodeFlow"), nodes.PrintStrNode())
    flow()


def test_plot():
    x = np.linspace(0, 3.14159265 * 2, 1000)
    y = _f(x)
    plot_node = nplots.PlotNode()
    plot_node.input(x, y)
    display_mpl_fig_node = nodes.DisplayMplFigureNode()
    flow = flows.Sequential(plot_node, display_mpl_fig_node)
    flow()


def test_scatter():
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    plot_node = nplots.ScatterNode()
    plot_node.input(x, y)
    display_mpl_fig_node = nodes.DisplayMplFigureNode()
    flow = flows.Sequential(plot_node, display_mpl_fig_node)
    flow()


def test_img():
    x = np.linspace(0, 3.14159265 * 2, 1000)
    y = _f(x)
    plot_node = nplots.PlotNode()
    plot_node.input(x, y)
    fig2img_node = nodes.utils.Fig2ImgNode()
    display_image_node = nodes.DisplayImageNode()
    flow = flows.Sequential(plot_node, fig2img_node, display_image_node)
    flow()


def main():
    test_hello_world()
    test_plot()
    test_scatter()
    test_img()


if __name__ == "__main__":
    main()

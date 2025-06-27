import flows
import nodes


def main():
    flow = flows.Sequential(nodes.HelloWorldNode("NodeFlow"), nodes.PrintStrNode())
    flow.exec()


if __name__ == "__main__":
    main()

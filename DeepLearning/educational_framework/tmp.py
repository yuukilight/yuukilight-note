from core import Operation, Placeholder, Variable, Node, _default_graph
# from SimpleTensor.constant import runtime
from collections import deque, defaultdict
import numpy as np
from queue import Queue


def view_graph(node : Operation, file_name : str = "./dot", format="png"):
    from graphviz import Digraph
    dot = Digraph(format=format)

    if not isinstance(node, Operation):
        raise ValueError("input node must be an Operation!")
    queue = Queue()
    visit = set()
    queue.put(node)
    visit.add(node)
    node2id = {}
    for index, n in enumerate(_default_graph):
        dot.node(name=str(index), label=str(n.__class__.__name__))
        node2id[n] = str(index)

    while not queue.empty():
        cur_node = queue.get()
        for input_node in cur_node.input_nodes:
            if isinstance(input_node, Operation) and input_node not in visit:   
                visit.add(input_node)
                queue.put(input_node)
            dot.edge(node2id[input_node], node2id[cur_node])

    dot.render(filename=file_name, cleanup=True)
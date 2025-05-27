from core import Operation, Placeholder, Node, Linear, _default_graph
from tmp import view_graph



X = Placeholder()
out = Linear(13, 1, bias=True)(X)
view_graph(node=_default_graph[-1], format="pdf")
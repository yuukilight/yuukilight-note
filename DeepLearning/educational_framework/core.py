import numpy as np
from queue import Queue
from typing import Union, List

from utils import Register

class Node: pass
# class add: pass
# class minus: pass
# class negative: pass
# class multiply: pass
# class matmul: pass
# class elementwise_pow: pass

_register_act_functions = Register()
_default_graph = []

class Node(object):
    def __init__(self, node_name: str=""):
        """
            base for all types of node in the static calculation graph
        """
        self.next_nodes = []
        self.data = None
        self.node_name = node_name
        _default_graph.append(self)
    
    def __neg__(self):
        return negative(self)

    def __add__(self, node : Node):
        return add(self, node)
    
    def __sub__(self, node : Node):
        return minus(self, node)

    def __mul__(self, node : Node):
        return multiply(self, node)
    
    def __pow__(self, y : Union[int, float]):
        return elementwise_pow(self, y)
    
    def __matmul__(self, node : Node):
        return matmul(self, node)

    def __str__(self):
        return f"{self.__class__.__name__}({str(self.data)})"
    
    @property
    def numpy(self):
        if self.data is None:
            raise ValueError(f"the node {self.__class__} is empty, please run the session first!")
        return np.array(self.data)

    @property
    def shape(self):
        if self.data is None:
            raise ValueError(f"the node {self.__class__} is empty, please run the session first!")
        return np.array(self.data).shape
    
    def to_numpy(self):
        if self.data is None:
            raise ValueError(f"the node {self.__class__} is empty, please run the session first!")
        return np.array(self.data)
    
    def to_list(self):
        if self.data is None:
            raise ValueError(f"the node {self.__class__} is empty, please run the session first!")
        return list(self.data)
    
class Operation(Node):
    def __init__(self, input_nodes : List[Node] = [], node_name: str=""):
        super().__init__(node_name=node_name)
        self.input_nodes = input_nodes
        for node in input_nodes:
            node.next_nodes.append(self)
    
    def compute(self, *args):
        pass

class Placeholder(Node):
    def __init__(self):
        super().__init__()

class Variable(Node):
    def __init__(self, init_value : Union[np.ndarray, list] = None):
        super().__init__()
        self.data = init_value

# create session to update nodes' data in the graph
class Session(object):
    def run(self, root_op : Operation, feed_dict : dict = {}):
        for node in _default_graph:
            if isinstance(node, Variable):
                node.data = np.array(node.data)
            elif isinstance(node, Placeholder):
                node.data = np.array(feed_dict[node])
            else:
                input_datas = [n.data for n in node.input_nodes]
                node.data = node.compute(*input_datas)
        return root_op

# ==============================
# basic function used in core.py
# ==============================
class add(Operation):
    def __init__(self, x : Node, y : Node, node_name: str=""):
        super().__init__(input_nodes=[x, y], node_name=node_name)
    
    def compute(self, x_v : np.ndarray, y_v : np.ndarray):
        return x_v + y_v

class minus(Operation):
    def __init__(self, x : Node, y : Node, node_name: str=""):
        super().__init__(input_nodes=[x, y], node_name=node_name)
    
    def compute(self, x_v : np.ndarray, y_v : np.ndarray):
        return x_v - y_v

class negative(Operation):
    def __init__(self, x : Node, node_name: str=""):
        super().__init__(input_nodes=[x], node_name=node_name)
    
    def compute(self, x_v : np.ndarray):
        return -1. * x_v

class elementwise_pow(Operation):
    def __init__(self, x : Node, y : Union[int, float], node_name: str=""):
        super().__init__(input_nodes=[x], node_name=node_name)
        self.y = y
    
    def compute(self, x_v : np.ndarray):
        return x_v ** self.y

class matmul(Operation):
    def __init__(self, x : Node, y : Node, node_name: str=""):
        super().__init__(input_nodes=[x, y], node_name=node_name)
    
    def compute(self, x_v : np.ndarray, y_v : np.ndarray):
        return x_v @ y_v

class multiply(Operation):
    def __init__(self, x : Node, y : Node, node_name: str=""):
        super().__init__(input_nodes=[x, y], node_name=node_name)
    
    def compute(self, x_v : np.ndarray, y_v : np.ndarray):
        return x_v * y_v

class reduce_sum(Operation):
    def __init__(self, x : Node, axis : int = None, node_name: str=""):
        super().__init__(input_nodes=[x], node_name=node_name)
        self.axis = axis
    
    def compute(self, x_v : np.ndarray):
        return np.sum(x_v, axis=self.axis)

class reduce_mean(Operation):
    def __init__(self, x : Node, axis : int = None, node_name: str=""):
        super().__init__(input_nodes=[x], node_name=node_name)
        self.axis = axis
    
    def compute(self, x_v : np.ndarray):
        return np.mean(x_v, axis=self.axis)

# class log(Operation):
#     def __init__(self, x : Node, node_name: str=""):
#         super().__init__(input_nodes=[x], node_name=node_name)
    
#     def compute(self, x_v : np.ndarray):
#         if (x_v <= 0).any():
#             back_print("Oops, invalid value encountered in 'log', I guess you forget activation function", color="yellow")
#         return np.log(x_v)

@_register_act_functions("sigmoid")
class sigmoid(Operation):
    def __init__(self, x : Node):
        super().__init__(input_nodes=[x])
    
    def compute(self, x_v : np.ndarray):
        return 1 / (1 + np.exp(-1. * x_v))
    
class Linear(object):
    def __init__(self, input_dim : int, output_dim : int, bias : bool = True, act : str = None):
        self.input_dim = input_dim
        self.output_dim = output_dim
        if act and act not in _register_act_functions:
            raise ValueError(f"input activate function '{act}' is not in registered activate function list:{list(_register_act_functions.keys())}")
        self.act = act
        self.W = Variable(np.random.randn(input_dim, output_dim))
        if bias:
            self.b = Variable(np.random.randn(1, output_dim))
    
    def __call__(self, X : Node):
        if not isinstance(X, Node):
            raise ValueError("Linear's parameter X must be a Node!")
        out = X @ self.W + self.b
        if self.act:
            act_func = _register_act_functions[self.act]
            return act_func(out)
        else:
            return out
        


if __name__ == "__main__":
    from tmp import view_graph
    X = Placeholder()
    out = Linear(13, 1, bias=True)(X)
    view_graph(node=_default_graph[-1], format="pdf")
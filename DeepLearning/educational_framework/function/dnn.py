import numpy as np

from educational_framework import Node, Variable, DnnVarOperator
from educational_framework import runtime, core
from educational_framework.utils import back_print

class Linear(DnnVarOperator):
    def __init__(self, input_dim : int, output_dim : int, bias : bool = True, act : str = None, init: str=""):
        super().__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.bias = bias
        if act and act not in runtime.activate_func:
            raise ValueError(f"input activate function '{act}' is not in registered activate function list:{list(runtime.activate_func.keys())}")
        
        # TODO : consider a clever solution to initialize parameters
        # Now, it is unstable
        # https://www.cnblogs.com/wxkang/p/15366535.html
        if init and init not in runtime.init_func:
            raise ValueError("init not in registered init methods! Available methods are " + str(list(runtime.init_func.keys())))
        self.init = init
        
        W_param = self.get_params(self.input_dim, self.output_dim)
        self.W = Variable(W_param, node_name=self.cur_name)

        if self.bias:
            b_param = self.get_params(1, self.output_dim)
            self.b = Variable(b_param, node_name=self.cur_name)
        
        self.act = act
    
    def __call__(self, X : Node) -> Node:
        if not isinstance(X, Node):
            raise ValueError("Linear's parameter X must be a Node!")
        
        out = core.matmul(X, self.W, node_name=self.cur_name)
        out = core.add(out, self.b, node_name=self.cur_name)
        
        if self.act:
            act_func = runtime.activate_func[self.act]
            return act_func(out, node_name=self.cur_name)
        else:
            return out
    
    def get_params(self, input_size, output_size) -> np.ndarray:
        if self.init:
            return runtime.init_func[self.init]((input_size, output_size))
        else:
            return np.random.randn(input_size, output_size)
    
    def reset_params(self) -> None:
        W_param = self.get_params(self.input_dim, self.output_dim)
        self.W = Variable(W_param, node_name=self.cur_name)

        if self.bias:
            b_param = self.get_params(1, self.output_dim)
            self.b = Variable(b_param, node_name=self.cur_name)

class Conv2D(DnnVarOperator):
    ...

class Rnn(DnnVarOperator):
    ...
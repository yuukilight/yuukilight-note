import abc
from .core import Operation, Variable, Placeholder, Data
from .constant import runtime, EPSILON
from collections import deque
import numpy as np

def backwards(op_node: Operation):
    """
    do the BP from the op_node, 
    return a gradient dict including op_node's gradients with respect to all the nodes before op_node
    """
    # will do the BP through BFS
    grad_table = {}
    grad_table[op_node] = 1.
    visit_nodes = set()
    queue = deque()
    visit_nodes.add(op_node)
    queue.append(op_node)

    while len(queue) > 0:
        cur_node = queue.popleft()
        if cur_node != op_node and not (isinstance(cur_node, Placeholder) or isinstance(cur_node, Data)):
            grad_table[cur_node] = 0
            for next_node in cur_node.next_nodes:
                grad_loss_wrt_next_node : np.ndarray = grad_table[next_node]
                next_node_op_name : str = next_node.__class__.__name__          # next_node must be an Operation
                gradient_func = runtime.gradient_func[next_node_op_name]
                grad_loss_wrt_cur_node = gradient_func(next_node, grad_loss_wrt_next_node)

                if len(next_node.input_nodes) == 1:
                    grad_table[cur_node] += grad_loss_wrt_cur_node[0]
                else:
                    cur_node_in_next_index = next_node.input_nodes.index(cur_node)
                    grad_table[cur_node] += grad_loss_wrt_cur_node[cur_node_in_next_index]



        if isinstance(cur_node, Operation):
            for input_node in cur_node.input_nodes:
                if input_node not in visit_nodes:
                    visit_nodes.add(input_node)
                    queue.append(input_node)

    return grad_table

class Optimizer(abc.ABC):
    def __init__(self, learning_rate: float = 1e-3):
        """
            base for all the optimizer
        """
        self.learning_rate = learning_rate

    @abc.abstractmethod
    def minimize(self, loss_node: Operation):
        """
            concrete optimizer method,
            this method will update parameters before "loss" node(include loss)
        """
        pass

class SGD(Optimizer):
    def __init__(self, learning_rate : float = 1e-3):
        super().__init__(learning_rate=learning_rate)
    
    def minimize(self, loss_node : Operation):
        lr = self.learning_rate
        grad_table = backwards(op_node=loss_node)
        for node in grad_table:
            if isinstance(node, Variable):
                grad = grad_table[node]
                node.data -= lr * grad

        runtime.grad_table = grad_table
        return grad_table
    

optimizers = {
    "SGD" : SGD,
    # "Momentum" : Momentum,
    # "AdaGrad" : AdaGrad,
    # "RMSProp" : RMSProp,
    # "Adan" : Adam
}
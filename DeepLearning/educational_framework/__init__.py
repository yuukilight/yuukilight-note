__version__ = "1.0.1"

from educational_framework.constant import runtime, Clip
# from educational_framework.utils import numpy_one_hot
from educational_framework.core import Node, Operation, Variable, Placeholder, Data, DnnOperator, DnnVarOperator
from educational_framework.core import Session
from educational_framework.core import reduce_mean, reduce_sum, log
from educational_framework import optimizer
from educational_framework.function import dnn

# finish init and register, they are available in <runtime>
import educational_framework.function.activate
import educational_framework.function.gradient
# import educational_framework.initialize

from educational_framework import view
from educational_framework.function import measure
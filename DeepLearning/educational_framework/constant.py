import numpy as np
from educational_framework.utils import Register
from collections import defaultdict

EPSILON = 1e-5

class Clip:
    """Constant variable
    """
    PRECISE_LOW = 1E-127
    PRECISE_HIGH = 1E128
    EXP_PRECISE_LOW = -292.42
    EXP_PRECISE_HIGH = 294.73
    EXP = lambda x : np.exp(np.clip(x, Clip.EXP_PRECISE_LOW, Clip.EXP_PRECISE_HIGH))

class runtime:
    activate_func = Register()
    gradient_func = Register()
    init_func = Register()
    global_calc_graph = list()
    dnn_cnt = defaultdict(int)
    grad_table = None


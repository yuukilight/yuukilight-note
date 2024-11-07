from typing import List, Dict

class A:
    def __init__(self, 
                 a:int, 
                 b: float, 
                 c:str, 
                 d:List[int], 
                 e: Dict[str, int]):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __str__(self):
        return f"str_A(a={self.a},b={self.b},c={self.c},d={self.d},e={self.e})"

    def __repr__(self):
        return f"repr_A(a={self.a},b={self.b},c={self.c},d={self.d},e={self.e})"
    
    @staticmethod
    def get_nromal_instance():
        return A(1, 1.3, 'hello', [1,2], {'a': 1, 'b': 2})
    pass
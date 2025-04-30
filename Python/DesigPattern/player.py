
from abc import abstractmethod, ABC

class Player(ABC):
    def __init__(self, name ,role):
        self.name = name
        self.role = role

    @abstractmethod
    def action(self):
        """球员动作"""

    def __str__(self):
        return f'name={self.name}, role={self.role}'

class Forward(Player):
    def action(self):
        print(f'{self.name} 带球突破后卫，转身，倒挂金钩！')

class MiddleField(Player):
    def action(self):
        print(f'{self.name} 控球，虚晃摆脱对手，精准长传！')

class DefenseField(Player):
    def action(self):
        print(f'{self.name} 一个滑铲，抢走球权！')

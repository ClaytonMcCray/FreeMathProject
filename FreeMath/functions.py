# This class will house various methods for evaluating mathematical
# functions
from typing import List, Union, NewType

scalar = NewType('scalar', Union[float, int])


class Function:
    def __init__(self, func: str):
        self.func = func

    def get_function(self):
        return self.func

    def evaluate(self, args: List) -> scalar:
        sentence = self.get_function()
        for var in args:
            sentence = sentence.replace(var[0], str(var[1]))
        return eval(sentence)


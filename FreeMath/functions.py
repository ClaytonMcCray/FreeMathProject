# This class will house various methods for evaluating mathematical
# functions
from typing import List, Union, NewType

scalar = NewType('scalar', Union[float, int])


# functions should be passed as strings containing variables if desired. As in, 'x ** 2'.
# Strings should follow standard python mathematical notation.
class Function:
    def __init__(self, func: str):
        self.func = func

    def get_function(self) -> str:
        return self.func

    # variables should be provided in a nested list: [['x', 2]] would evaluate the sentence
    # for x = 2. The double nesting should be used even if only a single pair of arguments is passed.
    # for more arguments, just extend the list: [['x', 2], ['y', 3], ['z', 4]].
    def evaluate(self, args: List) -> scalar:
        sentence = self.get_function()
        for var in args:
            sentence = sentence.replace(var[0], str(var[1]))
        try:
            return eval(sentence)
        except (NameError, SyntaxError):  # pretty sure most issues arising from inserted gibberish will be this type
            print('Error: Mathematical Sentences must be in native Python 3.x Format!')
            exit(1)

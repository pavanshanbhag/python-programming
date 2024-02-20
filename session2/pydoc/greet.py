"""Module level doc string example

from the terminal run the below command :
python -m pydoc greet # generates documentation for greet and displays on the terminal
python -m pydoc -w greet # to generate html doc for the given module greet

"""


def greet(name):
    """ greet function
        arg:
            name - str : takes name as the input
    """
    print(f"Hello {name}")
Implement two decorators that form a small DSL that allows you to turn regular functions into interactive programs. Decorator asks adds a description of one of the arguments of the function being converted. A separate asks call will be needed for each argument. Important: the order in which the requests appear during the dialog with the user must match the order of the decorators in the file (not the order in which they are actually applied). After all the arguments of the function being converted have been described using asks, the interactive decorator is applied. After it is applied, the resulting function stops accepting arguments and returning a result (None is eventually returned, of course), but it starts communicating with the user.

Example:
>>> @interactive('Calculator')
... @asks('x', 'Enter first number: *)
... @asks('y', 'Enter second number: *)
... def calc(x, y):
...
return int(x) + int (y)
...
>>> calc
Calculator
Enter first number: 42
Enter second number: 57
99
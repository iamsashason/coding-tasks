Implement a function called compose that takes two other one-argument functions as input and returns a new function. This new function should also take one argument and apply the original functions to it in the correct order: for functions f and g, the order of application should be f(g(x)).

Examples:
The following examples will help you understand how the function should work:
    def add5(x):
        return x + 5
    def mul3(x):
        return x * 3
    compose(mul3, add5)(1)
    18
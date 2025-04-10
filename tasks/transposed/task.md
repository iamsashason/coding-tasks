Matrix transposition is an operation in which the columns of the matrix become rows, and the rows become columns. Let's imagine a two-dimensional matrix

1 2 3
4 5 6
7 8 9

After transposition, the matrix will look

1 4 7
2 5 8
3 6 9

The transposition was performed along the main diagonal, that is, 1, 5 and 9 remained in their places, and the matrix itself turned out to be rotated 180 degrees relative to this imaginary diagonal axis.

Implement a transposed function that should accept a matrix as a list of lists and return the transposed matrix (a new list of lists).
Keep in mind that although in mathematics only square matrices are transposed, your transposed function should be more "omnivorous": it should be able to flip rectangular matrices too!

Examples:

>>> transposed([[1]])
[[1]]
>>> transposed([[1, 2], [3, 4]])
[[1, 3], [2, 4]]
>>> transposed([[1, 2], [3, 4], [5, 6]])
[[1, 3, 5], [2, 4, 6]]
>>> transposed(transposed([[1, 2]])) == [[1, 2]]
True
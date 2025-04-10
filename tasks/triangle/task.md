Pascal's triangle is an infinite table of binomial coefficients that has a triangular shape. The triangle has 1s at the top and on each side. Each number is the sum of the two numbers above it. The rows of the triangle are symmetrical about the vertical axis.

0:     1
1:    1 1
2:   1 2 1
3:  1 3 3 1
4: 1 4 6 4 1

Write a function triangle() that returns a specified row of Pascal's triangle as a list.

Example:
››› triangle(0)
[1]
››› triangle(4)
[1, 4, 6, 4, 1]
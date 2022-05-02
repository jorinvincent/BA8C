For this assignment your code should expect a file named input that contains two types of information:

A header (the first line) which contains two numbers k and n - k is the number of clusters we are seeking, n is the number of dimensions of the space within which the points are defined.
A list of points, one per line, each line containing exactly n floating point numbers - the coordinates along each dimension.
An example is:

2 4
1.5 3.2 2.5 4.1
12.9 4.6 11.8 3.9
This is a file that indicates we are looking for k=2 clusters of points occurring in n=4 dimensions. The file contains exactly 2 points, each represented as 4 floating point numbers.

Your program must create a file called "output" which contains exactly k lines, each representing one of the centers of the k clusters.  In the simple example above, there are, of course, only two centers that are also the points:

1.5 3.2 2.5 4.1
12.9 4.6 11.8 3.9
IMPORTANT: For your code to be guaranteed to pass the tests, you must run Lloyd's algorithm until it converges, and start the execution by selecting the first k points in the file as the initial guesses for the centers.

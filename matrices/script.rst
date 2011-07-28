.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to 

.. 1. Create matrices using data.
.. #. Create matrices from lists.
.. #. Basic matrix operations.
.. #. Use ``inv()`` function to find inverse of a matrix.
.. #. Use ``det()`` function to find determinant of a matrix.
.. #. Use ``eig()`` and ``eigvals()`` functions to find eigen values
      and vectors
.. #. Use ``norm()`` function to find norm of a matrix.
.. #. Use ``svd()`` function to find singular value decomposition of a
      matrix.


.. Prerequisites
.. -------------

..   1. should have ``ipython`` and ``pylab`` installed. 
..   #. getting started with ``ipython``.
..   #. getting started with lists.
..   #. getting started with arrays.
..   #. accessing part of arrays.

     
.. Author              : Anoop Jacob Thomas <anoop@fossee.in>
   Internal Reviewer   : Puneeth
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <11-11-2010, Anand, OK> [2010-10-05]


========
Matrices
========

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on 'Matrices'.

.. L2

{{{ switch to slide with objectives }}}

.. R2

At the end of this tutorial, you will be able to, 

 1. Create matrices using data.
 #. Create matrices from lists.
 #. Do basic matrix operations like addition,multiplication.
 #. Perform operations to find out the --
    - inverse of a matrix.
    - determinant of a matrix.
    - eigen values and eigen vectors of a matrix.
    - norm of a matrix.
    - singular value decomposition of a matrix.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with lists", "Getting started with arrays",
"Accessing parts of arrays".

.. R4

Let us start our ipython interpreter with pylab loaded

.. L4
::

    ipython -pylab

.. R5

All matrix operations are done using arrays. Thus all the operations
on arrays are valid on matrices also. A matrix may be created as,

.. L5
::

    m1 = array([1,2,3,4])

.. R6

Using the method ``shape``, we can find out the shape or size of the
matrix,

.. L6
::

    m1.shape

.. R7

Since it is a one row four column matrix it returned a tuple, one by
four.

A list can also be converted to a matrix as follows,

.. L7
::

    l1 = [[1,2,3,4],[5,6,7,8]]
    m2 = array(l1)

.. R8

Pause the video here, try out the following exercise and resume the video.

.. L8

.. L9

{{{ switch to slide, exercise 1 }}}

.. R9

Create a two dimensional matrix m3 of order 2 by 4 with
elements 5, 6, 7, 8, 9, 10, 11, 12.

.. R10

Switch to terminal for solution.
m3 can be created as,

.. L10

{{{ Switch to terminal }}}
::

    m3 = array([[5,6,7,8],[9,10,11,12]])

.. R11

Let us now move to matrix operations.
We can do matrix addition and subtraction easily.
m3+m2 does element by element addition, that is matrix addition.
Note that both the matrices should be of the same order.

.. L11
::

    m3 + m2

.. R12

Similarly,m3-m2 does matrix subtraction, that is element by element
subtraction.

.. L12
::

    m3 - m2

.. R13

Now let us try,matrix multiplication

.. L13
::

    m3 * m2

.. R14

Note that in arrays ``m3 * m2`` does element wise multiplication and not
matrix multiplication,

Matrix multiplication in matrices are done using the function ``dot()``

.. L14
::

    dot(m3, m2)

.. R15

Due to size mismatch, the multiplication could not be done and it
returned an error.

Now let us see an example for matrix multiplication. For doing matrix
multiplication we need to have two matrices of the order n by m and m
by r and the resulting matrix will be of the order n by r. Thus let us
first create two matrices which are compatible for multiplication.

.. L15
::

    m1.shape

.. R16

matrix m1 is of the shape one by four, let us create another one, of
the order four by two,

.. L16
::

    m4 = array([[1,2],[3,4],[5,6],[7,8]])
    dot(m1, m4)

.. R17

Thus the ``dot()`` function is used for matrix multiplication.

.. L17

.. L18

{{{ switch to next slide, recall from arrays }}}

.. R18

As we already learnt in arrays, the function ``identity()`` which
creates an identity matrix of the order n by n, the function ``zeros()`` 
which creates a matrix of the order m by n with all zeros, the function 
``zeros_like()`` which creates a matrix with zeros with the shape of 
the matrix passed, the function ``ones()`` which creates a matrix of 
order m by n with all ones, the function ``ones_like()`` which creates a 
matrix with ones with the shape of the matrix passed; all these 
functions can also be used with matrices.

.. R19

Let us now see, how to find out the transpose of a matrix we can do,

.. L19

{{{ Switch to the terminal }}}
::

    print m4
    m4.T

.. R20

As you saw, Matrix name dot capital T will give the transpose of a matrix

Pause the video here, try out the following exercise and resume the video.

.. L20

.. L21

{{{ switch to next slide, exercise 2:Frobenius norm & inverse }}}

.. R21

Find out the Frobenius norm of inverse of a 4 by 4
matrix, the matrix being,
    m5 = arange(1,17).reshape(4,4)

The Frobenius norm of a matrix is defined as,
the square root of the sum of the absolute squares of its elements

.. R22

Switch to terminal for the solution
Let us create the matrix m5 by using the data provided in the question

.. L22

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    m5 = arange(1,17).reshape(4,4)
    print m5

.. R23

The inverse of a matrix A, A raise to minus one, is also called the
reciprocal matrix, such that A multiplied by A inverse will give 1. The
Frobenius norm of a matrix is defined as square root of sum of squares
of elements in the matrix. The inverse of a matrix can be found using the 
function ``inv(A)``.

.. L23
::

    im5 = inv(m5)

.. R24

And the Frobenius norm of the matrix ``im5`` can be found out as,

.. L24
::

    sum = 0
    for each in im5.flatten():
        sum += each * each
    print sqrt(sum)

.. R25

Thus we have successfully obtained the Frobenius norm of the matrix m5

Pause the video here, try out the following exercise and resume the video.

.. L25

.. L26

{{{ switch to next slide,exercise 3: infinity norm }}}

.. R26

Find out the infinity norm of the matrix im5. 
The infinity norm of a matrix is defined as the maximum value of sum of 
the absolute of elements in each row. 

.. R27

Switch to terminal for the solution

.. L27

{{{continue from paused state}}}
{{{ Switch to the terminal }}}
::

    sum_rows = []
    for i in im5:
        sum_rows.append(abs(i).sum())
    print max(sum_rows)

.. R28

Well! to find the Frobenius norm and Infinity norm we have an even easier
method, and let us see that now.

.. L28

{{{ switch to slide the ``norm()`` method }}}

.. R29

The norm of a matrix can be found out using the method
``norm()``. 

.. L29

.. R30

In order to find out the Frobenius norm of the matrix im5,
we do,

.. L30

{{{ Switch to the terminal }}}
::

    norm(im5)

.. R31

And to find out the Infinity norm of the matrix im5, we do,

.. L31
::

    norm(im5,ord=inf)

.. R32

This is easier when compared to the code we wrote. Read the documentation 
of ``norm`` to read up more about ``ord`` and the possible type of norms
the norm function produces.

Now let us find out the determinant of a the matrix m5. 

The determinant of a square matrix can be obtained by using the function
``det()`` and the determinant of m5 can be found out as,

.. L32
::

    det(m5)

.. R33

Hence we get the determinant.
Let us now move on to eigen vectors and eigen values

.. L33

.. L34

{{{ switch to next slide, eigen vectors and eigen values }}}

.. R34

The eigen values and eigen vector of a square matrix can be computed
using the function ``eig()`` and ``eigvals()``.

.. R35

Let us find out the eigen values and eigen vectors of the matrix
m5. We find them as,

.. L35

{{{ Switch to the terminal }}}
::

    eig(m5)

.. R36

Note that it returned a tuple of two matrices. The first element in
the tuple are the eigen values and the second element in the tuple are
the eigen vectors. Thus the eigen values are given by,

.. L36
::

    eig(m5)[0]

.. R37

and the eigen vectors are given by,

.. L37
::

    eig(m5)[1]

.. R38

The eigen values can also be computed using the function ``eigvals()`` as,

.. L38
::

    eigvals(m5)

.. L39

{{{ switch to next slide, singular value decomposition }}}

.. R39

Now let us learn how to do the singular value decomposition or S V D
of a matrix.

Suppose M is an m×n matrix, whose entries come from the field K, which
is either the field of real numbers or the field of complex
numbers. Then there exists a factorization of the form

    M = U\Sigma V star

where U is an (m by m) unitary matrix over K, the matrix \Sigma is an
(m by n) diagonal matrix with non-negative real numbers on the
diagonal, and V* is an (n by n) unitary matrix over K,which denotes the
conjugate transpose of V. Such a factorization is called the
singular-value decomposition of M.

.. R40

The SVD of matrix m5 can be found as

.. L40

{{{ Switch to the terminal }}}
::

    svd(m5)

.. R41

Notice that it returned a tuple of 3 elements. The first one U the
next one Sigma and the third one V star.
 
.. L41

.. L42
   
{{{ switch to summary slide }}}

.. R42

This brings us to the end of the end of this tutorial.In this tutorial, 
we have learnt to, 

 1. Create matrices using arrays.
 #. Add,subtract and multiply the elements of matrix.
 #. Find out the inverse of a matrix,using the function ``inv()``.
 #. Use the function ``det()`` to find the determinant of a matrix.
 #. Calculate the norm of a matrix using the for loop and also using 
    the function ``norm()``.
 #. Find out the eigen vectors and eigen values of a matrix, using 
    functions ``eig()`` and ``eigvals()``.
 #. Calculate singular value decomposition(SVD) of a matrix using the 
    function ``svd()``.

.. L43

{{{Show self assessment questions slide}}}

.. R43

Here are some self assessment questions for you to solve

1. A and B are two array objects. Element wise multiplication in
   matrices are done by,

   - A * B
   - ``multiply(A, B)``
   - ``dot(A, B)``
   - ``element_multiply(A,B)``

2. ``eig(A)[1]`` and ``eigvals(A)`` are the same.

   - True
   - False

3. ``norm(A,ord='fro')`` is the same as ``norm(A)`` ?

   - True
   - False

.. L44

{{{solution of self assessment questions on slide}}}

.. R44

And the answers,

1. Element wise multiplication between two matrices, A and B is done as,
   A * B

2. False.
   ``eig(A)[0]`` and ``eigvals(A)`` are same, that is both will give the 
   eigen values of matrix A.

3. ``norm(A,ord='fro')`` and ``norm(A)`` are same, since the order='fro' 
   stands for Frobenius norm. Hence true.

.. L45

{{{ switch to Thank you slide }}}

.. R45

Hope you have enjoyed this tutorial and found it useful.
Thank you!



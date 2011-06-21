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

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

Hello friends and welcome to the tutorial on 'Matrices'.

{{{ switch to slide with objectives }}}

At the end of this tutorial, you will be able to, 

 1. Create matrices using data.
 #. Create matrices from lists.
 #. Do basic matrix operations like addition,multiplication.
 #. Perform operations to find out the --
    - inverse of a matrix
    - determinant of a matrix
    - eigen values and eigen vectors of a matrix
    - norm of a matrix
    - singular value decomposition of a matrix.

{{{ Switch to the pre-requisite slide }}}

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with lists", "Getting started with arrays",
"Accessing parts of arrays".

All matrix operations are done using arrays. Thus all the operations
on arrays are valid on matrices also. A matrix may be created as,
::

    ipython -pylab
    m1 = array([1,2,3,4])

Using the method ``shape``, we can find out the shape or size of the
matrix,
::

    m1.shape

Since it is a one row four column matrix it returned a tuple, one by
four.

A list can be converted to a matrix as follows,
::

    l1 = [[1,2,3,4],[5,6,7,8]]
    m2 = array(l1)

Pause the video here, try out the following exercise and resume the video.

{{{ switch to slide, exercise 1}}}

Create a two dimensional matrix m3 of order 2 by 4 with
elements 5, 6, 7, 8, 9, 10, 11, 12.

m3 can be created as,
::

    m3 = array([[5,6,7,8],[9,10,11,12]])

{{{ switch to next slide, matrix operations }}}

We can do matrix addition and subtraction easily.
::

    m3 + m2

m3+m2 does element by element addition, that is matrix addition.

Similarly,
::

    m3 - m2

Similarly,m3-m2 does matrix subtraction, that is element by element
subtraction.
Now let us try,matrix multiplication
::

    m3 * m2

Note that in arrays ``m3 * m2`` does element wise multiplication and not
matrix multiplication,

And matrix multiplication in matrices are done using the function ``dot()``
::

    dot(m3, m2)

but due to size mismatch the multiplication could not be done and it
returned an error,

Now let us see an example for matrix multiplication. For doing matrix
multiplication we need to have two matrices of the order n by m and m
by r and the resulting matrix will be of the order n by r. Thus let us
first create two matrices which are compatible for multiplication.
::

    m1.shape

matrix m1 is of the shape one by four, let us create another one, of
the order four by two,
::

    m4 = array([[1,2],[3,4],[5,6],[7,8]])
    dot(m1, m4)

thus the function ``dot()`` can be used for matrix multiplication.

{{{ switch to next slide, recall from arrays }}}

As we already learnt in arrays, the function ``identity()`` which
creates an identity matrix of the order n by n, the function ``zeros()`` 
which creates a matrix of the order m by n with all zeros, the function 
``zeros_like()`` which creates a matrix with zeros with the shape of 
the matrix passed, the function ``ones()`` which creates a matrix of 
order m by n with all ones, the function ``ones_like()`` which creates a 
matrix with ones with the shape of the matrix passed; all these 
functions can also be used with matrices.

To find out the transpose of a matrix we can do,
::

    print m4
    m4.T

Matrix name dot capital T will give the transpose of a matrix

{{{ switch to next slide, Frobenius norm of inverse of matrix }}}

Now let us try to find out the Frobenius norm of inverse of a 4 by 4
matrix, the matrix being,
::

    m5 = arange(1,17).reshape(4,4)
    print m5

The inverse of a matrix A, A raise to minus one, is also called the
reciprocal matrix, such that A multiplied by A inverse will give 1. The
Frobenius norm of a matrix is defined as square root of sum of squares
of elements in the matrix. The inverse of a matrix can be found using the 
function ``inv(A)``.

And here is the solution, first let us find the inverse of matrix m5.
::

    im5 = inv(m5)

And the Frobenius norm of the matrix ``im5`` can be found out as,
::

    sum = 0
    for each in im5.flatten():
        sum += each * each
    print sqrt(sum)

{{{ switch to next slide, infinity norm }}}

Now let us move on to find out the infinity norm of the matrix im5. 
The infinity norm of a matrix is defined as the maximum value of sum of 
the absolute of elements in each row. Pause here and try to solve the
problem yourself.


The solution for the problem is,
::

    sum_rows = []
    for i in im5:
        sum_rows.append(abs(i).sum())
    print max(sum_rows)

{{{ switch to slide the ``norm()`` method }}}

Well! to find the Frobenius norm and Infinity norm we have an even easier
method, and let us see that now.

The norm of a matrix can be found out using the method
``norm()``. Inorder to find out the Frobenius norm of the matrix im5,
we do,
::

    norm(im5)

And to find out the Infinity norm of the matrix im5, we do,
::

    norm(im5,ord=inf)

This is easier when compared to the code we wrote. Read the documentation 
of ``norm`` to read up more about ord and the possible type of norms
the norm function produces.

Now let us find out the determinant of a the matrix m5. 

The determinant of a square matrix can be obtained by using the function
``det()`` and the determinant of m5 can be found out as,
::

    det(m5)

Hence we get the determinant.

{{{ switch to next slide, eigen vectors and eigen values }}}

The eigen values and eigen vector of a square matrix can be computed
using the function ``eig()`` and ``eigvals()``.

Let us find out the eigen values and eigen vectors of the matrix
m5. We find them as,
::

    eig(m5)

Note that it returned a tuple of two matrices. The first element in
the tuple are the eigen values and the second element in the tuple are
the eigen vectors. Thus the eigen values are given by,
::

    eig(m5)[0]

and the eigen vectors are given by,
::

    eig(m5)[1]

The eigen values can also be computed using the function ``eigvals()`` as,
::

    eigvals(m5)

{{{ switch to next slide, singular value decomposition }}}

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

The SVD of matrix m5 can be found as
::

    svd(m5)

Notice that it returned a tuple of 3 elements. The first one U the
next one Sigma and the third one V star.
    
{{{ switch to summary slide }}}

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

{{{Show self assessment questions slide}}}

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

{{{solution of self assessment questions on slide}}}

And the answers,

1. Element wise multiplication between two matrices, A and B is done as,
   A * B

2. False.
   ``eig(A)[0]`` and ``eigvals(A)`` are same, that is both will give the 
   eigen values of matrrix A.

3. ``norm(A,ord='fro')`` and ``norm(A)`` are same, since the order='fro' 
   stands for frobenius norm. Hence true.


{{{ switch to Thank you slide }}}

Hope you have enjoyed this tutorial and found it useful.
Thank you!



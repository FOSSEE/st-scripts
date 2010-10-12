.. 4.3 LO: Matrices (3) [anoop] 
.. -----------------------------
.. * creating matrices 
..   + direct data 
..   + list conversion 
..   + builtins - identitiy, zeros, 
.. * matrix operations 
..   + + - * / 
..   + dot 
..   + inv 
..   + det 
..   + eig 
..   + norm 
..   + svd 

========
Matrices
========
{{{ show the welcome slide }}}

Welcome to the spoken tutorial on Matrices.

{{{ switch to next slide, outline slide }}}

In this tutorial we will learn about matrices, creating matrices using
direct data, by converting a list, matrix operations. Finding inverse
of a matrix, determinant of a matrix, eigen values and eigen vectors
of a matrix, norm and singular value decomposition of matrices.

{{{ creating a matrix }}}

All matrix operations are done using arrays. Thus all the operations
on arrays are valid on matrices also. A matrix may be created as,
::

    m1 = matrix([1,2,3,4])

Using the tuple ``m1.shape`` we can find out the shape or size of the
matrix,
::

    m1.shape

Since it is a one row four column matrix it returned a tuple, one by
four.

A list can be converted to a matrix as follows,
::

    l1 = [[1,2,3,4],[5,6,7,8]]
    m2 = matrix(l1)

Note that all matrix operations are done using arrays, so a matrix may
also be created as
::

    m3 = array([[5,6,7,8],[9,10,11,12]])

{{{ switch to next slide, matrix operations }}}

We can do matrix addition and subtraction as,
::

    m3 + m2

does element by element addition, thus matrix addition.

Similarly,
::

    m3 - m2

it does matrix subtraction, that is element by element
subtraction. Now let us try,

{{{ Switch to next slide, Matrix multiplication }}}
::

    m3 * m2

Note that in arrays ``array(A) star array(B)`` does element wise
multiplication and not matrix multiplication, but unlike arrays, the
operation ``matrix(A) star matrix(B)`` does matrix multiplication and
not element wise multiplication. And in this case since the sizes are
not compatible for multiplication it returned an error.

And element wise multiplication in matrices are done using the
function ``multiply()``
::

    multiply(m3,m2)

{{{ switch to next slide, Matrix multiplication (cont'd) }}}

Now let us see an example for matrix multiplication. For doing matrix
multiplication we need to have two matrices of the order n by m and m
by r and the resulting matrix will be of the order n by r. Thus let us
first create two matrices which are compatible for multiplication.
::

    m1.shape

matrix m1 is of the shape one by four, let us create another one of
the order four by two,
::

    m4 = matrix([[1,2],[3,4],[5,6],[7,8]])
    m1 * m4

thus unlike in array object ``star`` can be used for matrix multiplication
in matrix object.

{{{ switch to next slide, recall from arrays }}}

As we already saw in arrays, the functions ``identity()`` which
creates an identity matrix of the order n by n, ``zeros()`` which
creates a matrix of the order m by n with all zeros, ``zeros_like()``
which creates a matrix with zeros with the shape of the matrix passed,
``ones()`` which creates a matrix of order m by n with all ones,
``ones_like()`` which creates a matrix with ones with the shape of the
matrix passed. These functions can also be used with matrices.

{{{ switch to next slide, more matrix operations }}}

To find out the transpose of a matrix we can do,
::

    print m4
    m4.T

Matrix name dot capital T will give the transpose of a matrix

{{{ switch to next slide, Frobenius norm of inverse of matrix }}}

Now let us try to find out the Frobenius norm of inverse of a 4 by 4
matrix, the matrix being,
::

    m5 = matrix(arange(1,17).reshape(4,4))
    print m5

The inverse of a matrix A, A raise to minus one is also called the
reciprocal matrix such that A multiplied by A inverse will give 1. The
Frobenius norm of a matrix is defined as square root of sum of squares
of elements in the matrix. Pause here and try to solve the problem
yourself, the inverse of a matrix can be found using the function
``inv(A)``.

And here is the solution, first let us find the inverse of matrix m5.
::

    im5 = inv(m5)

And the Frobenius norm of the matrix ``im5`` can be found out as,
::

    sum = 0
    for each in array(im5.flatten())[0]:
        sum += each * each
    print sqrt(sum)

{{{ switch to next slide, infinity norm }}}

Now try to find out the infinity norm of the matrix im5. The infinity
norm of a matrix is defined as the maximum value of sum of the
absolute of elements in each row. Pause here and try to solve the
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

This is easier when compared to the code we wrote. Do ``norm``
question mark to read up more about ord and the possible type of norms
the norm function produces.

{{{ switch to next slide, determinant }}}

Now let us find out the determinant of a the matrix m5. 

The determinant of a square matrix can be obtained using the function
``det()`` and the determinant of m5 can be found out as,
::

    det(m5)

{{{ switch to next slide, eigen vectors and eigen values }}}

The eigen values and eigen vector of a square matrix can be computed
using the function ``eig()`` and ``eigvals()``.

Let us find out the eigen values and eigen vectors of the matrix
m5. We can do it as,
::

    eig(m5)

Note that it returned a tuple of two matrices. The first element in
the tuple are the eigen values and the second element in the tuple are
the eigen vectors. Thus the eigen values are,
::

    eig(m5)[0]

and the eigen vectors are,
::

    eig(m5)[1]

The eigen values can also be computed using the function ``eigvals()`` as,
::

    eigvals(m5)

{{{ switch to next slide, singular value decomposition }}}

Now let us learn how to do the singular value decomposition or S V D
of a matrix.

Suppose M is an m×n matrix whose entries come from the field K, which
is either the field of real numbers or the field of complex
numbers. Then there exists a factorization of the form

    M = U\Sigma V star

where U is an (m by m) unitary matrix over K, the matrix \Sigma is an
(m by n) diagonal matrix with nonnegative real numbers on the
diagonal, and V*, an (n by n) unitary matrix over K, denotes the
conjugate transpose of V. Such a factorization is called the
singular-value decomposition of M.

The SVD of matrix m5 can be found as
::

    svd(m5)

Notice that it returned a tuple of 3 elements. The first one U the
next one Sigma and the third one V star.
    
{{{ switch to next slide, recap slide }}}

So this brings us to the end of this tutorial. In this tutorial, we
learned about matrices, creating matrices, matrix operations, inverse
of matrices, determinant, norm, eigen values and vectors and singular
value decomposition of matrices.

{{{ switch to next slide, thank you }}}

Thank you!

..  Author: Anoop Jacob Thomas <anoop@fossee.in>
    Reviewer 1:
    Reviewer 2:
    External reviewer:

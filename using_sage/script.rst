.. Objectives
.. ----------

.. By the end of this tutorial you will --

.. 1. Get an idea of the range of things for which Sage can be used. 
.. #. Know some of the functions for Calculus
.. #. Get some insight into Graphs in Sage. 


.. Prerequisites
.. -------------

.. Getting Started -- Sage  
     
.. Author              : Puneeth 
   Internal Reviewer   : Anoop Jacob Thomas<anoop@fossee.in>
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <06-11-2010, Anand, OK> [2010-10-05]

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and  Welcome to the tutorial on 'Using Sage'.

.. L2

{{{ show the slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Learn the range of things for which Sage can be used. 
 #. Know the functions used for Calculus in Sage.
 #. Learn about graph theory and number theory using Sage.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Sage".  

Let us begin with Calculus. We shall be looking at limits,
differentiation, integration, and Taylor polynomial.

.. L4

{{{ open sage notebook }}}

.. R4

We have our Sage notebook running. In case, you don't have it running,
start is using the command, ``sage --notebook``.

.. R5

To find the limit of the function x*sin(1/x), at x=0, we say

.. L5
::

    lim(x*sin(1/x), x=0)

.. R6

We get the limit to be 0, as expected. 

It is also possible to the limit at a point from one direction. For
example, let us find the limit of 1/x at x=0, when approaching from
the positive side.

.. L6
::

    lim(1/x, x=0, dir='right')

.. R7

To find the limit from the negative side, we say,

.. L7
::

    lim(1/x, x=0, dir='left')   

.. R8

Let us now see how to perform differentiation, using Sage. We shall 
find the differential of the expression ``exp(sin(x^2))/x`` w.r.t ``x``.
For this, we shall first define the expression, and then use the ``diff`` 
function to obtain the differential of the expression.

.. L8
::

    var('x')
    f = exp(sin(x^2))/x
    diff(f, x)

.. R9

We can also obtain the partial differentiation of an expression w.r.t
one of the variables. Let us differentiate the expression
``exp(sin(y - x^2))/x`` w.r.t x and y.

.. L9
::

    var('x y')
    f = exp(sin(y - x^2))/x

    diff(f, x)

    diff(f, y)

.. R10

Thus we get our partial differential solution.
Now, let us look at integration. We shall use the expression obtained
from the differentiation that we did before, ``diff(f, y)`` which gave us 
the expression ---``e^(sin(-x^2 + y))*cos(-x^2 + y)/x``. 
The ``integrate`` command is used to obtain the integral of an 
expression or function.

.. L10
::

    integrate(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y)

.. R11

As we can see,we get back the correct expression. The minus sign being 
inside or outside the ``sin`` function doesn't change much. 

Now, let us find the value of the integral between the limits 0 and
pi/2. 

.. L11
::

    integral(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y, 0, pi/2)

.. R12

Hence we get our solution for the definite integration.
Let us now see how to obtain the Taylor expansion of an expression
using sage. Let us obtain the Taylor expansion of ``(x + 1)^n`` up to
degree 4 about 0.

.. L12
::

    var('x n')
    taylor((x+1)^n, x, 0, 4)

.. R13

We easlily got the Taylor expansion,using the function ``taylor()``.
This brings us to the end of the features of Sage for Calculus, that
we will be looking at. For more, look at the Calculus quick-ref from
the Sage Wiki. 

.. L13

.. L14

{{{ show the equation on the slides }}}

.. R14

Next let us move on to Matrix Algebra. 
Let us begin with solving the equation ``Ax = v``, where A is the
matrix ``matrix([[1,2],[3,4]])`` and v is the vector
``vector([1,2])``. 

.. R15

To solve the equation, ``Ax = v`` we simply say

.. L15

{{{ Switch back to sage notebook page }}}
::

    A = matrix([[1,2],
                [3,4]])
 
    v = vector([1,2])
    x = A.solve_right(v)
    x

.. R16

To solve the equation, ``xA = v`` we simply say

.. L16
::

    x = A.solve_left(v)
    x

.. R17

The left and right here, denote the position of ``A``, relative to x. 

Now, let us look at Graph Theory in Sage. 

We shall look at some ways to create graphs and some of the graph
families available in Sage. 

The simplest way to define an arbitrary graph is to use a dictionary
of lists. We create a simple graph by using the ``Graph()`` function.

.. L17
::

    G = Graph({0:[1,2,3], 2:[4]})

.. R18

to view the visualization of the graph, we say 

.. L18
::

    G.show()

.. R19

Similarly, we can obtain a directed graph using the ``DiGraph``
function. 

.. L19
::

    G = DiGraph({0:[1,2,3], 2:[4]})

.. R20

Sage also provides a lot of graph families which can be viewed by
typing ``graph.<tab>``. Let us obtain a complete graph with 5 vertices
and then show the graph. 

.. L20
::

    G = graphs.CompleteGraph(5)

    G.show()

.. R21

Sage provides other functions for Number theory and
Combinatorics. Let's have a glimpse of a few of them.  
``prime_range`` gives primes in the range 100 to 200. 

.. L21
::

    prime_range(100, 200)

.. R22

``is_prime`` checks if 1999 is a prime number or not. 

.. L22
::

    is_prime(1999) 

.. R23

``factor(2001)`` gives the factorized form of 2001. 

.. L23
::

    factor(2001)

.. R24

The ``Permutations()`` gives the permutations of ``[1, 2, 3, 4]``

.. L24
::

    C = Permutations([1, 2, 3, 4])
    C.list()

.. R25

And the ``Combinations()`` gives all the combinations of ``[1, 2, 3, 4]``

.. L25
::

    C = Combinations([1, 2, 3, 4])
    C.list()

.. L26

{{{ Show summary slide }}} 

.. R26

This brings us to the end of the tutorial.In this tutorial, 
we have learnt to,

 1. Use functions for calculus like --
    - lim()-- to find out the limit of a function
    - diff()-- to find out the differentiation of an expression
    - integrate()-- to integrate over an expression  
    - integral()-- to find out the definite integral of an 
      expression by specifying the limits
    - solve()-- to solve a function, relative to it's position. 
 #. Create Both a simple graph and a directed graph, using the 
    functions ``graph`` and ``digraph`` respectively.
 #. Use functions for Number theory.For eg: 
    - primes_range()-- to find out the prime numbers within the 
      specified range
    - factor()-- to find out the factorized form of the number specified
    - Permutations(), Combinations()-- to obtain the required permutation 
      and combinations for the given set of values.  

.. L27

{{{Show self assessment questions slide}}}

.. R27

Here are some self assessment questions for you to solve

1. How do you find the limit of the function ``x/sin(x)`` as ``x`` tends 
   to ``0`` from the negative side.


2. List all the primes between 2009 and 2900


3. Solve the system of linear equations
     
    x-2y+3z = 7
    2x+3y-z = 5
    x+2y+4z = 9

.. L28

{{{solution of self assessment questions on slide}}}

.. R28

And the answers,  

1. To find out the limit of an expression from the negative side,we add 
   an argument dir="left" as
::

    lim(x/sin(x), x=0, dir="left")

2. The prime numbers from 2009 and 2900 can be obtained as,
::

    prime_range(2009, 2901)

3. We shall first write the equations in matrix form and then use the 
   solve() function
::

    A = Matrix([[1, -2, 3], 
                [2, 3, -1], 
                [1, 2, 4]])

    b = vector([7, 5, 9])

    x = A.solve_right(b)

To view the ouput type x
::
    
    x 

.. L29

{{{ Switch to thankyou slide }}}

.. R29

Hope you have enjoyed this tutorial and found it useful.
Thank you!


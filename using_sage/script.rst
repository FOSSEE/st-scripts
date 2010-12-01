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

{{{ show the welcome slide }}}

Hello Friends. Welcome to this tutorial on using Sage.

{{{ show the slide with outline }}} 

In this tutorial we shall quickly look at a few examples of using Sage
for Linear Algebra, Calculus, Graph Theory and Number theory.

{{{ show the slide with Calculus outline }}} 

Let us begin with Calculus. We shall be looking at limits,
differentiation, integration, and Taylor polynomial.

{{{ show sage notebook }}}

We have our Sage notebook running. In case, you don't have it running,
start is using the command, ``sage --notebook``.

To find the limit of the function x*sin(1/x), at x=0, we say
::

   lim(x*sin(1/x), x=0)

We get the limit to be 0, as expected. 

It is also possible to the limit at a point from one direction. For
example, let us find the limit of 1/x at x=0, when approaching from
the positive side.
::

    lim(1/x, x=0, dir='above')

To find the limit from the negative side, we say,
::

    lim(1/x, x=0, dir='below')   

Let us now see how to differentiate, using Sage. We shall find the
differential of the expression ``exp(sin(x^2))/x`` w.r.t ``x``. We
shall first define the expression, and then use the ``diff`` function
to obtain the differential of the expression.
::

    var('x')
    f = exp(sin(x^2))/x

    diff(f, x)

We can also obtain the partial differentiation of an expression w.r.t
one of the variables. Let us differentiate the expression
``exp(sin(y - x^2))/x`` w.r.t x and y.
::

    var('x y')
    f = exp(sin(y - x^2))/x

    diff(f, x)

    diff(f, y)

Now, let us look at integration. We shall use the expression obtained
from the differentiation that we did before, ``diff(f, y)`` ---
``e^(sin(-x^2 + y))*cos(-x^2 + y)/x``. The ``integrate`` command is
used to obtain the integral of an expression or function.
::

    integrate(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y)

We get back the correct expression. The minus sign being inside or
outside the ``sin`` function doesn't change much. 

Now, let us find the value of the integral between the limits 0 and
pi/2. 
::

    integral(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y, 0, pi/2)

Let us now see how to obtain the Taylor expansion of an expression
using sage. Let us obtain the Taylor expansion of ``(x + 1)^n`` up to
degree 4 about 0.
::

    var('x n')
    taylor((x+1)^n, x, 0, 4)

This brings us to the end of the features of Sage for Calculus, that
we will be looking at. For more, look at the Calculus quick-ref from
the Sage Wiki. 

Next let us move on to Matrix Algebra. 

{{{ show the equation on the slides }}}

Let us begin with solving the equation ``Ax = v``, where A is the
matrix ``matrix([[1,2],[3,4]])`` and v is the vector
``vector([1,2])``. 

To solve the equation, ``Ax = v`` we simply say
::

    x = solve_right(A, v)

To solve the equation, ``xA = v`` we simply say
::

    x = solve_left(A, v)

The left and right here, denote the position of ``A``, relative to x. 

#[Puneeth]: any suggestions on what more to add?

Now, let us look at Graph Theory in Sage. 

We shall look at some ways to create graphs and some of the graph
families available in Sage. 

The simplest way to define an arbitrary graph is to use a dictionary
of lists. We create a simple graph by
::

  G = Graph({0:[1,2,3], 2:[4]})

We say 
::

  G.show()

to view the visualization of the graph. 

Similarly, we can obtain a directed graph using the ``DiGraph``
function. 
::

  G = DiGraph({0:[1,2,3], 2:[4]})


Sage also provides a lot of graph families which can be viewed by
typing ``graph.<tab>``. Let us obtain a complete graph with 5 vertices
and then show the graph. 
::

  G = graphs.CompleteGraph(5)

  G.show()


Sage provides other functions for Number theory and
Combinatorics. Let's have a glimpse of a few of them.  


::

  prime_range(100, 200)

gives primes in the range 100 to 200. 

::

  is_prime(1999) 

checks if 1999 is a prime number or not. 

::

  factor(2001)

gives the factorized form of 2001. 

::

  C = Permutations([1, 2, 3, 4])
  C.list()

gives the permutations of ``[1, 2, 3, 4]``

::

  C = Combinations([1, 2, 3, 4])
  C.list()

gives all the combinations of ``[1, 2, 3, 4]``
  
That brings us to the end of this session showing various features
available in Sage. 

.. #[[Anoop: I feel we should add more slides, a possibility is to add
   the code which they are required to type in, I also feel we should
   add some review problems for them to try out.]]

{{{ Show summary slide }}}

We have looked at some of the functions available for Linear Algebra,
Calculus, Graph Theory and Number theory.   

This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you!


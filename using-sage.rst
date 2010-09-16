========
 Script
========

{{{ show the welcome slide }}}

Welcome to this tutorial on using Sage.

{{{ show the slide with outline }}} 

In this tutorial we shall quickly look at a few examples of the areas
(name the areas, here) in which Sage can be used and how it can be
used.

{{{ show the slide with Calculus outline }}} 

Let us begin with Calculus. We shall be looking at limits,
differentiation, integration, and Taylor polynomial.

{{{ show sage notebook }}}

We have our Sage notebook running. In case, you don't have it running,
start is using the command, ``sage --notebook``.

To find the limit of the function x*sin(1/x), at x=0, we say::

   lim(x*sin(1/x), x=0)

We get the limit to be 0, as expected. 

It is also possible to the limit at a point from one direction. For
example, let us find the limit of 1/x at x=0, when approaching from
the positive side.::

    lim(1/x, x=0, dir='above')

To find the limit from the negative side, we say,::

    lim(1/x, x=0, dir='above')   

Let us now see how to differentiate, using Sage. We shall find the
differential of the expression ``exp(sin(x^2))/x`` w.r.t ``x``. We
shall first define the expression, and then use the ``diff`` function
to obtain the differential of the expression.::

    var('x')
    f = exp(sin(x^2))/x

    diff(f, x)

We can also obtain the partial differentiation of an expression w.r.t
one of the variables. Let us differentiate the expression
``exp(sin(y - x^2))/x`` w.r.t x and y.::

    var('x y')
    f = exp(sin(y - x^2))/x

    diff(f, x)

    diff(f, y)

Now, let us look at integration. We shall use the expression obtained
from the differentiation that we did before, ``diff(f, y)`` ---
``e^(sin(-x^2 + y))*cos(-x^2 + y)/x``. The ``integrate`` command is
used to obtain the integral of an expression or function.::

    integrate(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y)

We get back the correct expression. The minus sign being inside or
outside the ``sin`` function doesn't change much. 

Now, let us find the value of the integral between the limits 0 and
pi/2. ::

    integral(e^(sin(-x^2 + y))*cos(-x^2 + y)/x, y, 0, pi/2)

Let us now see how to obtain the Taylor expansion of an expression
using sage. Let us obtain the Taylor expansion of ``(x + 1)^n`` up to
degree 4 about 0.::

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

To solve the equation, ``Ax = v`` we simply say::

    x = solve_right(A, v)

To solve the equation, ``xA = v`` we simply say::

    x = solve_left(A, v)

The left and right here, denote the position of ``A``, relative to x. 



Now, let us look at Graph Theory in Sage. 

Graph: G = Graph({0:[1,2,3], 2:[4]})
Directed Graph: DiGraph(dictionary)
Graph families: graphs. tab
Invariants: G.chromatic polynomial(), G.is planar()
Paths: G.shortest path()
Visualize: G.plot(), G.plot3d()
Automorphisms: G.automorphism group(), G1.is isomorphic(G2), G1.is subgraph(G2)

Now let us look at bits and pieces of Number theory, combinatorics, 


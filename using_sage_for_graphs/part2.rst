########## Break Here ##########

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

To view the output type x
::
    
    x 


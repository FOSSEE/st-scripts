.. Objectives
.. ----------

.. Plotting a least square fit line

.. Prerequisites
.. -------------

..   1. Basic Plotting
..   2. Arrays
..   3. Loading data from files 
     
.. Author              : Nishanth Amuluru
   Internal Reviewer   : Punch
   External Reviewer   :
   Language Reviewer   : Bhanukiran
   Checklist OK?       : <put date stamp here, not OK> [2010-10-05]


Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on 'Least Square Fit'.

.. L2

{{{ Show the slide containing objectives }}}

.. R2

At the end of this tutorial, you will be able to,

 1. Generate the least square fit line for a
    given set of points.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using plot interactively", "Loading data from files"
and "Getting started with arrays".

Let us start this tutorial with the help of an example.

.. L4

{{{ Show the slide containing exercise 1 }}}

.. R4

Generate a least square fit line for l v/s t^2 using the data in the 
file 'pendulum.txt'.

.. L5

{{{ Open the file 'pendulum.txt' and show }}}

.. R5

We have an input file generated from a simple pendulum experiment.

It contains two columns of data. The first column is the length 
of the pendulum and the second is the corresponding time period 
of the pendulum.

As we know, the square of time period of a pendulum is directly 
proportional to its length, we shall plot l vs t^2 and verify this. 

To read the input file and parse the data, we are going to use the
loadtxt function.Switch to the terminal.

.. L6
::
 
    ipython -pylab
    l, t = loadtxt("/home/fossee/pendulum.txt", unpack=True)
    l
    t

.. R6

We can see that l and t are two sequences containing length and time 
values correspondingly.

Let us first plot l vs t^2.

.. L7
::

    tsq = t * t
    plot(l, tsq, 'bo')

{{{ switch to the plot window }}}

.. R7

We can see that there is a visible linear trend, but we do not get a
straight line connecting them. We shall, therefore, generate a least
square fit line.

We will first generate the two matrices tsq and A. 
Then we will use the ``lstsq`` function to find the
values of m and c.

.. L8

{{{ Switch to the terminal }}}

.. R8

let us now generate the A matrix with l values.
We shall first generate a 2 x 90 matrix with the first row as l values 
and the second row as ones. Then take the transpose of it. Type

.. L9
::

    inter_mat = array((l, ones_like(l)))
    inter_mat

.. R9

We see that we have intermediate matrix. Now we need the transpose. 
Type

.. L10
::

    A = inter_mat.T
    A

.. R10

Now we have both the matrices A and tsq. We only need to use 
the ``lstsq``
Type

.. L11
::

    result = lstsq(A, tsq)

.. R11

The result is a sequence of values. The first item in this sequence,
is the matrix p i.e., the values of m and c. 

.. L12
::

    m, c = result[0]
    m
    c

.. R12

Now that we have m and c, we need to generate the fitted values of t^2. 
Type

.. L13
::

    tsq_fit = m * l + c
    plot(l, tsq, 'bo')
    plot(l, tsq_fit, 'r')

.. R13

We get the least square fit of l vs t^2.

.. L14

{{{ Show summary slide }}}

.. R14

This brings us to the end of the tutorial.In this tutorial,
we have learnt to,

 1. Generate a least square fit using matrices.
 #. Use the function ``lstsq()`` to generate a least square fit line.

.. L15

{{{Show self assessment questions slide}}}

.. R15

Here are some self assessment questions for you to solve

1. What does ones_like([1, 2, 3]) produce

   - array([1, 1, 1])
   - [1, 1, 1]
   - [1.0, 1.0, 1.0]
   - Error
   
2. The plot of ``u`` vs ``v`` is a bunch of scattered points that show a
   linear trend. How do you find the least square fit line 
   of ``u`` vs ``v``.

.. L16

{{{solution of self assessment questions on slide}}}

.. R16

And the answers,

1. The function ``ones_like([1, 2, 3])`` will generate 'array([1, 1, 1])'.

2. The following set of commands will produce the least square fit 
   line of ``u`` vs ``v``
::

    A = array(u, ones_like(u)).T
    result = lstsq(A, v)
    m, c = result[0]
    lst_line = m * u + c

.. L17

{{{ Show the thank you slide }}}

.. R17

Hope you have enjoyed this tutorial and found it useful.
Thank you!


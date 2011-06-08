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

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

Hello friends and welcome to the tutorial on 'Least Square Fit'.

{{{ Show the slide containing objectives }}}

At the end of this tutorial, you will be able to,

 1. Generate the least square fit line for a
    given set of points.

{{{ Switch to the pre-requisite slide }}}

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Using plot interactively", "Loading data from files"
and "Getting started with arrays".

Let us start this tutorial with the help of an example.

{{{ Show the slide containing exercise 1 }}}

We have an input file generated from a simple pendulum experiment.

{{{ Open the file 'pendulum.txt' and show }}}

It contains two columns of data. The first column is the length of the
pendulum and the second is the corresponding time period of the pendulum.

As we know, the square of time period of a pendulum is directly proportional to
its length, we shall plot l vs t^2 and verify this. 

To read the input file and parse the data, we are going to use the
loadtxt function.Switch to the terminal.
::
 
    ipython -pylab
    l, t = loadtxt("/home/fossee/pendulum.txt", unpack=True)
    l
    t

We can see that l and t are two sequences containing length and time values
correspondingly.

Let us first plot l vs t^2.
::

    tsq = t * t
    plot(l, tsq, 'bo')

{{{ switch to the plot window }}}

We can see that there is a visible linear trend, but we do not get a
straight line connecting them. We shall, therefore, generate a least
square fit line.

We will first generate the two matrices tsq and A. 
Then we will use the ``lstsq`` function to find the
values of m and c.

{{{ Switch to the terminal }}}

let us now generate the A matrix with l values.
We shall first generate a 2 x 90 matrix with the first row as l values and the
second row as ones. Then take the transpose of it. Type

::

    inter_mat = array((l, ones_like(l)))
    inter_mat

We see that we have intermediate matrix. Now we need the transpose. Type
::

    A = inter_mat.T
    A

Now we have both the matrices A and tsq. We only need to use the ``lstsq``
Type
::

    result = lstsq(A, tsq)

The result is a sequence of values. The first item in this sequence,
is the matrix p i.e., the values of m and c. Hence, 
::

    m, c = result[0]
    m
    c

Now that we have m and c, we need to generate the fitted values of t^2. Type
::

    tsq_fit = m * l + c
    plot(l, tsq, 'bo')
    plot(l, tsq_fit, 'r')

We get the least square fit of l vs t^2.

{{{ Show summary slide }}}

This brings us to the end of the tutorial.In this tutorial,
we have learnt to,

 1. Generate a least square fit using matrices.
 #. Use the function ``lstsq()`` to generate a least square fit line.

{{{Show self assessment questions slide}}}

Here are some self assessment questions for you to solve

1. What does ones_like([1, 2, 3]) produce

   - array([1, 1, 1])
   - [1, 1, 1]
   - [1.0, 1.0, 1.0]
   - Error
   
2. The plot of ``u`` vs ``v`` is a bunch of scattered points that show a
    linear trend. How do you find the least square fit line of ``u`` vs ``v``.


{{{solution of self assessment questions on slide}}}

And the answers,

1. The function ``ones_like([1, 2, 3])`` will generate 'array([1, 1, 1])'.

2. The following set of commands will produce the least square fit line of ``u`` vs ``v``
::

    A = array(u, ones_like(u)).T
    result = lstsq(A, v)
    m, c = result[0]
    lst_line = m * u + c

{{{ Show the thank you slide }}}

Hope you have enjoyed this tutorial and found it useful.
Thank you!


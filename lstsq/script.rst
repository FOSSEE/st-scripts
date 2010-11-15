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


.. #[Puneeth: Add pre-requisites.]

Script
------

Hello friends and welcome to the tutorial on Least Square Fit

{{{ Show the slide containing title }}}

{{{ Show the slide containing the outline slide }}}

In this tutorial, we shall look at generating the least square fit line for a
given set of points.

First let us have a look at the problem.

{{{ Show the slide containing problem statement. }}}

We have an input file generated from a simple pendulum experiment.

It contains two columns of data. The first column is the length of the
pendulum and the second is the corresponding time period of the pendulum.

As we know, the square of time period of a pendulum is directly proportional to
its length, we shall plot l vs t^2 and verify this. 

.. #[Puneeth:] removed the explanation about loadtxt and unpack
..  option. It's been done in another LO already. simple dependency 
..  should work?

To read the input file and parse the data, we are going to use the
loadtxt function.  Type 
::

    l, t = loadtxt("/home/fossee/pendulum.txt", unpack=True)
    l
    t

We can see that l and t are two sequences containing length and time values
correspondingly.

Let us first plot l vs t^2. Type
::

    tsq = t * t
    plot(l, tsq, 'bo')

{{{ switch to the plot window }}}

.. #[Puneeth:] Moved explanation of least square fit here. seems more
.. apt. 

We can see that there is a visible linear trend, but we do not get a
straight line connecting them. We shall, therefore, generate a least
square fit line.

{{{ show the slide containing explanation on least square fit }}}

As shown in the slide, we are first going to generate the two matrices
tsq and A. Then we are going to use the ``lstsq`` function to find the
values of m and c.

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

We get the least square fit of l vs t^2

{{{ Pause here and try out the following exercises }}}

%% 2 %% change the label on y-axis to "y" and save the lines of code
        accordingly

{{{ continue from paused state }}}

{{{ Show summary slide }}}

This brings us to the end of the tutorial.
we have learnt

 * how to generate a least square fit

{{{ Show the "sponsored by FOSSEE" slide }}}

.. #[Nishanth]: Will add this line after all of us fix on one.
.. This tutorial was created as a part of FOSSEE project, NME ICT, MHRD India

Hope you have enjoyed and found it useful.
Thank you


.. 
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: nil
   fill-column: 75
   End:
